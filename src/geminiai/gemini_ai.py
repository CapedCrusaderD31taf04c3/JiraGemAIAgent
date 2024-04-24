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

import google.generativeai as genai
import os


class LoadHistory:
    """
    """
    
    history = []

    @classmethod
    def get_content(cls, role: str, text: str) -> ContentDict:
        """
        """

        return ContentDict(role=role, parts=[PartDict(text=CoderPrompt.PROMPT)])


    @classmethod
    def load_intro_msg_in_history(cls):
        """
        """
        cls.history.append(cls.get_content(role="user", text=CoderPrompt.PROMPT))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.INTRO_MSG_RECEIVED))

    @classmethod
    def load_src_code_in_history(cls, docs):
        """
        """

        cls.load_intro_msg_in_history()

        cls.history.append(cls.get_content(role="user", text=CoderPrompt.SOURCE_CODE_COMING_MSG))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.SRC_CODE_COMING))
        for doc in docs:
            source_code = (
                f"# file_location = {doc.metadata['source']}\n"
                f"{doc.page_content}"
            )

            cls.history.append(cls.get_content(role="user", text=source_code))
            cls.history.append(cls.get_content(role="model", text=ModelResponse.TXT_OF_SRC_FILE_RECEIVED))

        cls.history.append(cls.get_content(role="user", text=CoderPrompt.SOURCE_CODE_ARRIVED_MSG))
        cls.history.append(cls.get_content(role="model", text=ModelResponse.ALL_SRC_CODE_RECEIVED))
        
        return cls.history


class GenerativeAI:

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    model = genai.GenerativeModel('gemini-pro')

    def start_new_chat(self, docs):
        """
        """
        history = LoadHistory.load_src_code_in_history(docs=docs)
        chat = self.model.start_chat(history=history)

        return chat
    

    def ask(self, question, docs):
        """
        """
        chat = self.start_new_chat(docs=docs)
        response = chat.send_message(content=question)

        return response