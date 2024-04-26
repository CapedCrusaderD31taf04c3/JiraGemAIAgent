
from fastapi import APIRouter, status

home_router = APIRouter()

class HomeView:
    """
    A class representing views for the home endpoint.
    """
    @home_router.get("/")
    async def home() -> dict:
        """
        Endpoint for the home view.

        return: A dictionary containing the response message and data.
        rtype: dict
        """

        return {
            "message": "Success",
            "status": 200,
            "data": {
                "msg" : "This is response of Home View"
            }
        }