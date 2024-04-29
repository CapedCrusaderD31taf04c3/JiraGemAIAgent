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

from coder.code_loader import SourceCodeLoader
from coder.code_updater import CodeUpdater
from git_integrator.git_activities import GitActivity
from geminiai.gemini_ai import GenerativeAI
from json import JSONDecodeError
from git.exc import GitCommandError
from logger.custom_logger import Logger

class Develop:
    """
    A class that perform as developer
    """

    # For Github Activities
    git_bot = GitActivity()

    def perform(self, extract, question: str):
        """
        Perform a sequential operations

        param extract:
        type extract: 

        param question: Question which will be asked to AI
        type question: str
        """
        try:

            Logger.info(message=f"{extract.ticket_key} Creating a New branch", stage="START")

            self.git_bot.create_new_branch(
                ticket_id=extract.ticket_key, 
                ticket_title=extract.ticket_summary
            ).checkout_to_branch(self.git_bot.branch_name)

            Logger.info(message="Checkd out to new branch", stage="END")

            Logger.info(message="Loading Source Code", stage="START")
            src = SourceCodeLoader.loader()
            Logger.info(message="Source Code Loaded", stage="END")

            Logger.info(message="Asking to AI", stage="START")
            answer = GenerativeAI().ask(question=question, docs=src)  
            Logger.info(message="AI Replied", stage="END")

            Logger.info(message="Updating the source code from local repo", stage="START")
            CodeUpdater(answer.text).update()
            Logger.info(message="Source Code Updated", stage="END")

            Logger.info(message="Staging commiting and pushing the changes", stage="START")
            self.git_bot.stage_changes().commit_changes(
                commit_message=f"{extract.ticket_key}-commited by JiraGemAIAgent"
            ).push_changes()
            Logger.info(message="Staged, commited and pushed", stage="END")

            Logger.info(message="Creating Pull request", stage="START")
            self.git_bot.create_pr(description=extract.ticket_desc)
            Logger.info(message=f"{extract.ticket_key} Pull request Created", stage="END")

        except GitCommandError as git_err:
            self.git_bot.safe_eject()
            Logger.error(message= f"Something wrong with Local Github Setup : {str(git_err)}")
        except JSONDecodeError as json_err:
            self.git_bot.safe_eject()
            Logger.error(message= f"Wrong AI Reply, Response From AI is not able to Convert to valid json because {str(json_err)}")
        except Exception as err:
            self.git_bot.safe_eject()
            Logger.error(message= f"Error Occurred - {str(err)}")