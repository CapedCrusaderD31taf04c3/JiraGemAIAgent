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

class CoderPrompt:
    """
    Prepares the prompt for updating source code
    """

    INPUT_PREPARATION = """You are an Expert Software Engineer I am providing source code of a project in some next messages after the given example of output, please consider them all together as a whole project 
	In message, location of file is provided in the first line or comment of file, Don't consider it as part of source code,
	source code of that file is after comment on first line.
	"""

    WORK_INSTRUCTION = """I will ask you to update the given source code as required with respect of the given task,
	whatever the code you will update make sure you don't create unwanted bugs in it,
	There will be 3 situations while updating the project to complete the task,
	Old file needs to be updated then to_update=true, to_create=false, to_delete=false.
	New file needs to be created then to_create=true, to_update=false, to_delete=false.
	Unwanted file needs to be deleted then to_delete=true, to_update=false, to_create=false.
	"""

    OUTPUT_SPECIFICATION = """Provide reply message in given format with same keynames only, 
	for reference consider below example
	"""

    OUPUT_EXAMPLES = """
	Q: {
        "heading": "add todo_main function",
        "info": "change name of main function to todo_main function"
    }
	A: [
		{
		"file_location": "E:/Dummy_Project/todo_app/src/main.py",
		"source_code": "# Testing\nfrom Todo import TodoApp\n\ndef main() -> None:\n  app: TodoApp = TodoApp()\n    app.start()\n\nif __name__ == "__main__":\n		main()",
		"to_update": true,
		"to_create": false,
		"to_delete": false
		}
	]
	"""

    PROMPT = (
		f"{INPUT_PREPARATION}\n"
		f"{WORK_INSTRUCTION}\n"
		f"{OUTPUT_SPECIFICATION}\n"
		f"{OUPUT_EXAMPLES}\n"
	)

    SOURCE_CODE_COMING_MSG = "I am giving the messages one by one  in which source code is exist and I will let you know when I gave all the source code"
    
    SOURCE_CODE_ARRIVED_MSG = "I gave all the messages with source code in it, now I'll give you task"