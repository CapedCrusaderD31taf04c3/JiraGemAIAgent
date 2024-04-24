
from fastapi import APIRouter, status

home_router = APIRouter()

class HomeView:
    """
    contains method for home view
    """
    @home_router.get("/")
    async def home():
        """
        returns response for home view
        """

        return {
            "message": "Success",
            "status": 200,
            "data": {
                "msg" : "This is response of Home View"
            }
        }