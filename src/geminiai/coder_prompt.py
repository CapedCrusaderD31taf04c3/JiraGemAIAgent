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

    OUTPUT_SPECIFICATION = """Provide answer in valid string format only do not provide json codeblock like "```json" , the given answer string must successfully load with loads() method from json module in python, 
	for reference consider below examples for output format, under this examples Question is given infront pf Q:
    and answer is given infront of A:
    In answer keep same key names and format, answer must of string datatype,
    I am giving sample examples now
	"""

    OUPUT_EXAMPLES_COMING_MSG = """Your answers should be provided in a valid JSON string format only. 
    Refer to the examples below for the output format:
	"""

    OUPUT_EXAMPLES_ARRIVED_MSG = """Your answers should be provided in a valid JSON string format only. 
    Refer to the examples below for the output format:
	"""

    INTRODUCTION_PROMPT = (
		f"{INPUT_PREPARATION}\n"
		f"{WORK_INSTRUCTION}\n"
		f"{OUTPUT_SPECIFICATION}\n"
	)

    SOURCE_CODE_COMING_MSG = "I will provide the messages containing the source code one by one. You will be informed once all the source code messages have been provided."
    
    SOURCE_CODE_ARRIVED_MSG = "All messages containing the necessary source code have been provided. Now I will give you task"


    @classmethod
    def prepare_output_examples(cls):
        """
        Preparing examples from example.json file
        """

        with open(Path(__file__).parent / "examples.json", "r") as fr:
            json_data = json.load(fr)
        

        output_examples: str = ""
        
        for example in json_data.get("examples", []):
            output_examples += f"""\nQ: {example["Q"]},\nA: {example["A"]}"""
            
        return output_examples