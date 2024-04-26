from .coder_prompt import CoderPrompt

import os
import google.generativeai as genai

class LoadHistory:
    """
    A class to manage chat history and loading source code into it. 
    """
    
    history = [CoderPrompt.PROMPT]

    @classmethod
    def load_src_code_in_history(cls, docs:list) -> list:
        """
        Load source code into chat history

        param docs: List of documents containing source code.
        type docs: list

        return: Updated chat history including the source code.
        rtype: list
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
    """
    A class for interacting with a generative AI model for chatting
    """

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    model = genai.GenerativeModel('gemini-pro')

    def start_new_chat(self, docs:list) -> genai.generative_models.ChatSession:
        """
        Start a new chat session.

        param docs: List of documents containing source code.
        type docs: list

        return: Chat session object
        rtype: genai.generative_models.ChatSession
        """
        history = LoadHistory.load_src_code_in_history(docs=docs)
        chat = self.model.start_chat(history=history)

        return chat
    

    def ask(self, question: str, docs: list) -> str:
        """
        Ask a question to the AI model.

        param question: The question to be asked to AI
        type question: str

        param docs: List of documents containing source code
        type docs: list

        return: Response from the AI model
        rtype: str
        """
        chat = self.start_new_chat(docs=docs)
        response = chat.send_message(content=question)

        return response