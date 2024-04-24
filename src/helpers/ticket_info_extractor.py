
from logger.custom_logger import Logger

class TicketInfoExtractor:
    """
    extracts the information from the ticket
    """

    def __init__(self, ticket):
        """
        extracts key, summary, description and type of ticket

        param ticket: ticket to extract information from
        type ticket: TicketModel   
        """

        Logger.info(message="Retrieving Ticket Information", stage="START")

        self.ticket_key = ticket.issue.get("key", None)
        self.ticket_summary = ticket.issue.get("fields", {}).get("summary", None)
        self.ticket_desc = ticket.issue.get("fields", {}).get("description", None)
        self.ticket_type = ticket.issue.get("fields", {}).get("issuetype", {}).get("namedValue", None)
        
        Logger.info(message="Retrieved Ticket Information", stage="END")