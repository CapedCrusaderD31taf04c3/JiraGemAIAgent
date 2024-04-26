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

from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
from views.home_view import home_router
from views.code_view import code_router
from logger.custom_logger import Logger

import uvicorn


class LoadEnvVars:
    """
    A class for loading environment variables.
    """
    @staticmethod
    def load_env_vars() -> None:
        """
        Load environment variables from the .env file.
        """

        Logger.info(message="Loading Env Vars", stage="START")

        env_path = Path(__file__).parent.parent / ".env"
        load_dotenv(dotenv_path=env_path)

        Logger.info(message="Loaded Env Vars", stage="End")


class InitiateAIServer:
    """
    A class for initiating the FastAPI server.
    """
    
    app = FastAPI()
    
    @classmethod
    def include_routers(cls) -> None:
        """
        Include routers in the FastAPI application.
        """
        routers = [
            home_router,
            code_router
        ]

        Logger.info(message="Including URL Routers", stage="START")

        for router in routers:
            cls.app.include_router(router)
        
        Logger.info(message="Included URL Routers", stage="END")
            
    @classmethod
    def get_app(cls) -> FastAPI:
        """
        Get the configured FastAPI application.

        return: The configured FastAPI application
        rtype: FastAPI
        """

        Logger.info(message="Server Configuring", stage="START")
        
        # Adding all Routers
        cls.include_routers()
        
        Logger.info(message="Server Configured", stage="END")

        return cls.app

# Run the FastAPI application
if __name__ == "__main__":
    """
    Main block for running the FastAPI application.
    """
    try:
        Logger.info(message="Initiating Env Var Loader", stage="START")
        LoadEnvVars.load_env_vars()

        Logger.info(message="Initiating Server", stage="START")
        app = InitiateAIServer.get_app()
        
        uvicorn.run(app, host="0.0.0.0", port=8000)
    
    except Exception as err:
        Logger.error(message=str(err))