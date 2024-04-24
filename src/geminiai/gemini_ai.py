from .coder_prompt import CoderPrompt

import os
import google.generativeai as genai

class LoadHistory:
    """
    contains methods to load prompts for the chat 
    """
    
    history = [CoderPrompt.PROMPT]

    @classmethod
    def load_src_code_in_history(cls, docs):
        """
        loads the source code in the chat history

        param docs: contains the source code
        type docs: list
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
        loads the prompts and source code in history and starts a new chat

        param docs: the source code to be included in history
        type docs: list
        """
        history = LoadHistory.load_src_code_in_history(docs=docs)
        chat = self.model.start_chat(history=history)

        return chat
    

    def ask(self, question, docs):
        """
        returns the response to the chat

        param question: the question to be asked to AI
        type question: str

        param docs: the source code to be included in question
        type docs: list
        """
        chat = self.start_new_chat(docs=docs)
        response = chat.send_message(content=question)

        return response