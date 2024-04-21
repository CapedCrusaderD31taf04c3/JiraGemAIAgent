
from fastapi import APIRouter, status

home_router = APIRouter()

class HomeView:
    """
    """
    @home_router.get("/")
    async def home():
        """
        """

        return {
            "message": "Success",
            "status": 200,
            "data": {
                "msg" : "This is response of Home View"
            }
        }