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

    INPUT_PREPARATION = """You are an Expert Software Engineer tasked with updating source code provided in subsequent messages as part of a larger project. 
    The location of each file within the project will be specified in the first commented line with 'file_location'. 
    Disregard this location information as part of the source code. The actual source code for each file will follow the comment on the first line. 
    Ensure to consider all provided messages as components of the entire project. Your goal is to understand and update the code accordingly.
	"""

    WORK_INSTRUCTION = """During the process of updating the provided source code to complete the task, you may encounter three situations:
	1.If an existing file requires modification, indicate to_update=true.
	2.If a new file needs to be created, specify to_create=true.
	3.If an unwanted file should be deleted, specify to_delete=true. In this case, if source code is not provided, it is acceptable.
	Ensure that any modifications made to the code are implemented without introducing unintended bugs.
	"""

    OUTPUT_SPECIFICATION = """Provide answer in valid string format only do not provide json codeblock like "```json" , 
	for reference consider below examples for output format, under this examples Question is given infront pf Q:
    and answer is given infront of A:
    In answer keep same key names and format, answer must of string datatype,
    I am giving sample examples now
	"""

    OUPUT_EXAMPLES_COMING_MSG = """Your answers should be provided in a valid JSON string format only. 
    Refer to the examples below for the output format:
	"""

    OUPUT_EXAMPLES_ARRIVED_MSG = """ 
    Refer to the examples below for the output format:
	"""

    INTRODUCTION_PROMPT = (
		f"{INPUT_PREPARATION}\n"
		f"{WORK_INSTRUCTION}\n"
		f"{OUTPUT_SPECIFICATION}\n"
	)

    SOURCE_CODE_COMING_MSG = "I will provide the messages containing the source code one by one. You will be informed once all the source code messages have been provided."
    
    SOURCE_CODE_ARRIVED_MSG = """All messages containing the necessary source code have been provided. 
    Note: Provide answer in valid string format only do not provide json codeblock like "```json" , the given answer string must successfully load with loads() method from json module in python, 
    Do not affect existing behaviour of code unnecessary,
    Now I will give you task"""


    OUTPUT_EXAMPLES = """
    Q: {
        "heading": "add todo_main function",
        "info": "change name of main function to todo_main function"
    }
    A: '[{"file_location": "E:/Dummy_Project/todo_app/src/main.py", "source_code": "from Todo import TodoApp\\n\\ndef todo_main() -> None:\\n    app: TodoApp = TodoApp()\\n    app.start()\\n\\nif __name__ == \\"__main__\\":\\n    todo_main()", "to_update": true}]'
    Q: {
        "heading": "Add proper documentation in source code",
        "info": "Add descriptive docstrings wherever they are necessary"
    }
    A: '[{"file_location": "E:/Dummy_Project/todo_app/src/main.py", "source_code": "from Todo import TodoApp\\n\\ndef todo_main() -> None:\\n    \\"\\"\\" Main Function For ToDo App \\"\\"\\"\\napp: TodoApp = TodoApp()\\n    app.start()\\n\\nif __name__ == \\"__main__\\":\\n    todo_main()", "to_update": true}]'
    Q: {
        "heading":"Introduce date manipulation utility",
        "info": "The project needs a new utility module for date manipulation."
    }
    A: '[{"file_location": "E:/Dummy_Project/todo_app/src/utils/date_utils.py", "source_code": "from datetime import datetime\\n\\ndef get_current_date() -> str:\\n return datetime.now().strftime(\\"%Y-%m-%d\\")\\n", "to_create": true}, {"file_location": "E:/Dummy_Project/todo_app/src/main.py", "source_code": "from Todo import TodoApp\\nfrom date_utils import get_current_date\\ndef todo_main() -> None:\\n    \\"\\"\\" Main Function For ToDo App \\"\\"\\"\\napp: TodoApp = TodoApp()\\n    app.start()\\n\\nif __name__ == \\"__main__\\":\\n    todo_main()", "to_update": true}]'
    Q: {
        "heading": "Unit Test for User input Function",
        "info": "Write unit test with pytest for user_input method "
    }
    A: '[{"file_location": "E:/Dummy_Project/todo_app/tests/test_user_input.py", "source_code": "from user_input import user_input\\n\\ndef test_user_input():\\n # Test input 1\\n assert user_input(\\"1\\") == 1\\n # Test input 2\\n assert user_input(\\"2\\") == 2\\n # Test input 3\\n assert user_input(\\"3\\") == 3\\n # Test other input\\n assert user_input(\\"4\\") == \\"4\\"\\n # Test exception handling\\n assert user_input(\\"abc\\") == None\\n", "to_create": true}]'
    Q: {
        "heading": "Extend support for user_input",
        "info": "Add support of user inputs to 4 and 5 in user_input method"
    }
    A: '[{"file_location": "E:/Dummy_Project/todo_app/src/user_input.py", "source_code": "def user_input():\\n user_input = input()\\n try:\\n if user_input == \\"1\\":\\n print(\\"This is 1\\")\\n return 1\\n elif user_input == \\"2\\":\\n print(\\"This is 2\\")\\n return 2\\n elif user_input == \\"3\\":\\n print(\\"This is 3\\")\\n return 3\\n elif user_input == \\"4\\":\\n print(\\"This is 4\\")\\n return 4\\n elif user_input == \\"5\\":\\n print(\\"This is 5\\")\\n return 5\\n else:\\n print(f\\"This is {user_input}\\")\\n return user_input\\n except Exception as err:\\n print(\\"Error Occurred\\")\\n", "to_update": true}]'
    Q: {
        "heading": "date manipulation utility not required",
        "info": "remove the support of date manipulation utility"
    }
    A: '[{"file_location": "E:/Dummy_Project/todo_app/src/utils/date_utils.py", "to_delete": true}, {"file_location": "E:/Dummy_Project/todo_app/src/main.py", "source_code": "from Todo import TodoApp\\n\\ndef todo_main() -> None:\\n    \\"\\"\\" Main Function For ToDo App \\"\\"\\"\\napp: TodoApp = TodoApp()\\n    app.start()\\n\\nif __name__ == \\"__main__\\":\\n    todo_main()", "to_update": true}]'
    """