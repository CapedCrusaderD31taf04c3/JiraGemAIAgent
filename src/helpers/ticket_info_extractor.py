
from logger.custom_logger import Logger

class TicketInfoExtractor:
    """
    """

    def __init__(self, ticket):
        """
        """

        Logger.info(message="Retrieving Ticket Information", stage="START")

        self.ticket_key = ticket.issue.get("key", None)
        self.ticket_summary = ticket.issue.get("fields", {}).get("summary", None)
        self.ticket_desc = ticket.issue.get("fields", {}).get("description", None)
        self.ticket_type = ticket.issue.get("fields", {}).get("issuetype", {}).get("namedValue", None)
        
        Logger.info(message="Retrieved Ticket Information", stage="END")