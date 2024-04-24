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

import logging


class Logger:
    """
    """

    cust_logger = logging.getLogger("Jira-App")
    logging.basicConfig(
            level=logging.INFO, 
            format="%(levelname)s:     %(message)s"
        )
    def __init__(self) -> None:
        """
        """
        
        pass

    @classmethod
    def config_logger(
            cls, 
            level=logging.INFO, 
            format="%(levelname)s:      %(message)s"
        ):
        """
        """

        logging.basicConfig(
            level=level, 
            format=format
        )

    @classmethod
    def info(cls, message, stage=None):
        """
        """
        if not stage:
            cls.cust_logger.info(message)
        else:
            if stage == "START":
                cls.cust_logger.info(f"\033[32;40m<START>\033[0;0m - {message}")
            elif stage == "END":
                cls.cust_logger.info(f"\033[31;40m<END>\033[0;0m   - {message}")
        

    @classmethod
    def debug(cls, message):
        """
        """

        cls.cust_logger.debug(message)

    @classmethod
    def error(cls, message):
        """
        """

        cls.cust_logger.error(f"\033[31;40m{message}\033[0;0m")

    @classmethod
    def warning(cls, message):
        """
        """

        cls.cust_logger.warning(message)

    @classmethod
    def critical(cls, message):
        """
        """

        cls.cust_logger.critical(message)

    