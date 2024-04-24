
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PythonLoader


class SourceCodeLoader:
    """
    contains method to load source code
    """

    docs = []

    @classmethod
    def loader(cls):
        """
        loads source code from the directory
        """

        loader = DirectoryLoader(
            "E:/Dummy_Project/todo_app/src", 
            glob="**/*.py",
            exclude=["*.pyc"],
            recursive=True,
            loader_cls=PythonLoader
        )

        cls.docs = loader.load()

        return cls.docs

