
from pydantic import BaseModel

class TicketModel(BaseModel):
    """
    """
    
    issue: dict
    user: dict
    timestamp: int