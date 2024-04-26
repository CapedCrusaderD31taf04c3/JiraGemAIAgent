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

import json
from pathlib import Path

class CodeUpdater:
    """
    This class parses a JSON answer containing solutions and performs actions such as updating,
    creating, or deleting files based on the provided information.
    """

    def __init__(self, answer:dict):
        """
        Initialises the solution with the answer received

        param answer: Answer given from AI
        type answer: dict
        """

        self.solutions = json.loads(answer)

    # File update
    def file_updater(self, file_location: Path, file_data: str) -> None:
        """
        Update a file with new data.

        param file_location: Location of the file to be updated
        type file_location: Path

        param file_data: New data to write to the file
        type file_data: str
        """

        if file_location.exists():
            with open(file_location, "w") as fw:
                fw.write(file_data)

    def file_creater(self, file_location: Path, file_data: str) -> None:
        """
        Create a new file with specified data

        param file_location: Location where the new file should be created
        type file_location: Path

        param file_data: Data to write to the new file
        type file_data: str
        """

        if not file_location.parent.exists():
            file_location.parent.mkdir(parents=True)
        with open(file_location, "w") as fw:
            fw.write(file_data)

    def file_deleter(self, file_location: Path) -> None:
        """
        Delete a file and its parent directory if it becomes empty.

        param file_location: location of file to be deleted
        type file_location: Path
        """

        if file_location.exists():
            # If the file exists, delete it
            file_location.unlink()
        
        are_files_exists = [item.is_file() for item in file_location.parent.iterdir()]

        if not any(are_files_exists):
            file_location.parent.rmdir()
	
    def update(self) -> None:
        """
        Execute the update process based on provided solutions.
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
