
import json
from pathlib import Path

class CodeUpdater:
    """
    contains methods to update source code, create/delete files wherever required
    """

    def __init__(self, answer) -> None:
        """
        initialises the solution with the answer received

        param answer: answer given from AI
        type answer: dict
        """

        self.solutions = json.loads(answer)

    # File update
    def file_updater(self, file_location, file_data):
        """
        updates the file with the given data

        param file_location: location of the file to be updated
        type file_location: str

        param file_data: updated data to write in the file
        type file_data: str
        """

        if file_location.exists():
            with open(file_location, "w") as fw:
                fw.write(file_data)

    def file_creater(self, file_location, file_data):
        """
        creates a file in the given file location with the given file data

        param file_location: location of the file
        type file_location: str

        param file_data: data to be written in the file
        type file_data: str
        """

        if not file_location.parent.exists():
            file_location.parent.mkdir(parents=True)
        with open(file_location, "w") as fw:
            fw.write(file_data)

    def file_deleter(self, file_location):
        """
        deletes the file in the given location

        param file_location: location of file to be deleted
        type file_location: str
        """

        if file_location.exists():
            # If the file exists, delete it
            file_location.unlink()
        
        are_files_exists = [item.is_file() for item in file_location.parent.iterdir()]

        if not any(are_files_exists):
            file_location.parent.rmdir()
	
    def update(self):
        """
        updates/creates/deletes the file based on the solution 
        """

        for solution in self.solutions:
            if solution["to_update"]:
                self.file_updater(
                    file_location=Path(solution["file_location"]),
                    file_data=solution["source_code"]
                )

            elif solution["to_create"]:
                self.file_creater(
                    file_location=Path(solution["file_location"]),
                    file_data=solution["source_code"]
                )

            elif solution["to_delete"]:
                self.file_deleter(
                    file_location=Path(solution["file_location"])
                )
