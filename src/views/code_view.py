

from fastapi import APIRouter
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
    """
    @code_router.post("/code/")
    async def write_code(ticket: TicketModel):
        """
        """
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

        CodeUpdater(answer.content).update()

        git_bot.stage_changes().commit_changes(
            commit_message="This is a Commit Message"
        ).push_changes()

        git_bot.create_pr(description=extract.ticket_desc)

        response =  {
                "message": "Success",
                "status": 200,
                "data": answer
            }
        
        return response