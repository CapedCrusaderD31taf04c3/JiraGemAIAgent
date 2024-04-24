

class CoderPrompt:
    """
    prepares the prompt for updating source code
    """

    INPUT_PREPARATION = """we are providing source code of a project in some next messages after the given example of output, please consider them as a whole project 
	In message location of file is provided with file_location variable, Don't consider it as part of source code,
	source code of that file is after 5 Hashtags.
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