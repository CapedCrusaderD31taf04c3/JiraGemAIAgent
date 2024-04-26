
from logger.custom_logger import Logger
from models.ticket_model import TicketModel

class TicketInfoExtractor:
    """
    A class for extracting information from a ticket object.
    """

    def __init__(self, ticket: TicketModel) -> None:
        """
        Initialize TicketInfoExtractor object and retrieve ticket information.

        param ticket: The ticket object from which information will be extracted.
        type ticket: TicketModel   
        """

        Logger.info(message="Retrieving Ticket Information", stage="START")

        self.ticket_key = ticket.issue.get("key", None)
        self.ticket_summary = ticket.issue.get("fields", {}).get("summary", None)
        self.ticket_desc = ticket.issue.get("fields", {}).get("description", None)
        self.ticket_type = ticket.issue.get("fields", {}).get("issuetype", {}).get("namedValue", None)
        
        Logger.info(message="Retrieved Ticket Information", stage="END")