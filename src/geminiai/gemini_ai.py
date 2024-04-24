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

import os
import google.generativeai as genai

class LoadHistory:
    """
    """
    
    history = [CoderPrompt.PROMPT]

    @classmethod
    def load_src_code_in_history(cls, docs):
        """
        """
        cls.history.append(CoderPrompt.SOURCE_CODE_COMING_MSG)
        
        for doc in docs:
            source_code = (
                f"# file_location : {doc.metadata['source']}\n"
                f"#####\n{doc.page_content}"
            )

            cls.history.append(source_code)

        cls.history.append(CoderPrompt.SOURCE_CODE_ARRIVED_MSG)

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