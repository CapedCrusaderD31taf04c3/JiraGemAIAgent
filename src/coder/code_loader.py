
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PythonLoader


class SourceCodeLoader:
    """
    """

    docs = []

    @classmethod
    def loader(cls):
        """
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

