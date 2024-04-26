
from pydantic import BaseModel

class TicketModel(BaseModel):
    """
    Specifies the pydantic model for the ticket
    """
    
    issue: dict
    user: dict
    timestamp: int