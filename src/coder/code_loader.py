
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PythonLoader


class SourceCodeLoader:
    """
    A class responsible for loading source code files from a directory.
    """

    docs = []

    @classmethod
    def loader(cls) -> list:
        """
        This method initializes a DirectoryLoader object with the specified parameters and 
        uses it to load source code files from the directory.

        return: A list containing the loaded source code files
        rtype: list
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

