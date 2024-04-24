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

