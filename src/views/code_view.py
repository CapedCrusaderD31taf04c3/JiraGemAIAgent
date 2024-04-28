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

from fastapi import APIRouter
from json import JSONDecodeError
from git.exc import GitCommandError

from models.ticket_model import TicketModel
from helpers.ticket_info_extractor import TicketInfoExtractor
from logger.custom_logger import Logger
from coder.code_loader import SourceCodeLoader
from coder.code_updater import CodeUpdater
from git_integrator.git_activities import GitActivity
from geminiai.gemini_ai import GenerativeAI



code_router = APIRouter()

class CodeView:
    """
    A class representing views for handling code-related operations.
    """
    
    @code_router.post("/code/")
    async def write_code(ticket: TicketModel) -> dict: # NOTE: SCA warning suppressed Python:S5720
        """
        Endpoint for writing code based on ticket information.

        param ticket: The ticket information.
        type ticket: TicketModel

        return: A dictionary containing the response message and data.
        rtype: dict
        """

        try:

            extract = TicketInfoExtractor(ticket)
            Logger.info(message=f"Detected Ticket category : \"{extract.ticket_type}\"")
            
            Logger.info(message="Preparing AI Query", stage="START")
            question = (
                "Q:{"
                f""" "heading": "{extract.ticket_summary}" """
                f""" "info" : "{extract.ticket_desc}" """
                "}"
                "A:"
            )
            
            # For Github Activities
            git_bot = GitActivity()
            git_bot.create_new_branch(
                ticket_id=extract.ticket_key, 
                ticket_title=extract.ticket_summary
            ).checkout_to_branch(git_bot.branch_name)

            src = SourceCodeLoader.loader()

            answer = GenerativeAI().ask(question=question, docs=src)  

            CodeUpdater(answer.text).update()

            git_bot.stage_changes().commit_changes(
                commit_message=f"{extract.ticket_key}-commited by JiraGemAIAgent"
            ).push_changes()

            git_bot.create_pr(description=extract.ticket_desc)

            response =  {
                "message": "Success",
                "status": 200
            }
        except JSONDecodeError as json_err:
            GitActivity().safe_eject()
            response =  {
                "message": "Wrong AI Reply, Response From AI is not able to Convert to valid json",
                "status": 500,
                "data": str(json_err)
            }
        except Exception as err:
            GitActivity().safe_eject()
            response =  {
                "message": "Error",
                "status": 500,
                "data": str(err)
            }
        
        return response