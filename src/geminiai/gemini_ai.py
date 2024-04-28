# -*- coding: utf-8 -*-
# Copyright 2024 JiraGemAIAgent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .coder_prompt import CoderPrompt
from .model_responses import ModelResponse
from google.generativeai.types.content_types import ContentDict, PartDict
from google.generativeai.generative_models import ChatSession
from google.generativeai.types.generation_types import GenerateContentResponse
import google.generativeai as genai
import os


class LoadHistory:
    """
    A class to manage chat history and loading source code into it. 
    """
    
    history = []

    @classmethod
    def get_content(cls, role: str, text: str) -> ContentDict:
        """
        Get Content For Chat History

        param role: Role of speaker
        type role: str

        param text: message
        type text: str

        return: Structured Content
        rtype: ContentDict
        """

        return ContentDict(role=role, parts=[PartDict(text=text)])


    @classmethod
    def load_intro_msg_in_history(cls) -> None:
        """
        Loading introduction message into history
        """
        
        introduction_text = f"""
        {CoderPrompt.INTRODUCTION_PROMPT}
        {CoderPrompt.OUPUT_EXAMPLES_COMING_MSG}
        {CoderPrompt.OUTPUT_EXAMPLES}
        {CoderPrompt.OUPUT_EXAMPLES_ARRIVED_MSG}
        """

        cls.history.append(cls.get_content(role="user", text=introduction_text))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.INTRO_MSG_RECEIVED))

    @classmethod
    def load_src_code_in_history(cls, docs:list) -> list:
        """
        Load source code into chat history

        param docs: List of documents containing source code.
        type docs: list

        return: Updated chat history including the source code.
        rtype: list
        """

        cls.load_intro_msg_in_history()

        cls.history.append(cls.get_content(role="user", text=CoderPrompt.SOURCE_CODE_COMING_MSG))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.SRC_CODE_COMING))
        
        src_code_parts = []
        for doc in docs:
            path = doc.metadata['source'].replace('\\\\', '/')
            source_code = (
                f"# file_location = {path}\n"
                f"{doc.page_content}"
            )

            src_code_parts.append(PartDict(text=source_code))

        cls.history.append(ContentDict(role="user", parts=src_code_parts))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.TXT_OF_SRC_FILE_RECEIVED))

        cls.history.append(cls.get_content(role="user", text=CoderPrompt.SOURCE_CODE_ARRIVED_MSG))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.ALL_SRC_CODE_RECEIVED))
        
        return cls.history


class GenerativeAI:
    """
    A class for interacting with a generative AI model for chatting
    """

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config={
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 0, 
            "max_output_tokens": 1048576,
        }
    )

    def start_new_chat(self, docs:list) -> ChatSession:
        """
        Start a new chat session.

        param docs: List of documents containing source code.
        type docs: list

        return: Chat session object
        rtype: ChatSession
        """
        history = LoadHistory.load_src_code_in_history(docs=docs)
        chat = self.model.start_chat(history=history)

        return chat
    

    def ask(self, question: str, docs: list) -> GenerateContentResponse:
        """
        Ask a question to the AI model.

        param question: The question to be asked to AI
        type question: str

        param docs: List of documents containing source code
        type docs: list

        return: Response from the AI model
        rtype: GenerateContentResponse
        """
        chat = self.start_new_chat(docs=docs)
        response = chat.send_message(content=question)

        return response