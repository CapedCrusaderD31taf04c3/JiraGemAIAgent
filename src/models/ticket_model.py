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

from pydantic import BaseModel

class IssueTypeModel(BaseModel):
    """
    Specifies pydantic model for issuetype sub object
    """
    namedValue: str

class FieldModel(BaseModel):
    """
    Specifies pydantic model for field sub object
    """
    summary: str
    description: str
    issuetype: IssueTypeModel


class IssueModel(BaseModel):
    """
    Specifies pydantic model for issue sub object
    """
    key: str
    fields: FieldModel

class TicketModel(BaseModel):
    """
    Specifies the pydantic model for the ticket webhook
    """
    
    issue: IssueModel
    user: dict
    timestamp: int