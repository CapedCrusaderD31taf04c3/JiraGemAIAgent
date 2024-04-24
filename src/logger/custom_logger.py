import logging


class Logger:
    """
    contains methods for different kinds of loggers
    """

    logger = logging.getLogger("Jira-App")
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
        basic config for the logging system
        """

        logging.basicConfig(
            level=level, 
            format=format
        )

    @classmethod
    def info(cls, message, stage=None):
        """
        logger for info message

        param message: the info message
        type message: str

        param stage: specifies the stage of logging
        type stage: str
        """
        if not stage:
            cls.logger.info(message)
        else:
            if stage == "START":
                cls.logger.info(f"\033[32;40m<START>\033[0;0m - {message}")
            elif stage == "END":
                cls.logger.info(f"\033[31;40m<END>\033[0;0m   - {message}")
        

    @classmethod
    def debug(cls, message):
        """
        logger for debug message

        param message: the debug message
        type message: str
        """

        cls.logger.debug(message)

    @classmethod
    def error(cls, message):
        """
        logger for error message

        param message: the error message
        type message: str
        """

        cls.logger.error(f"\033[31;40m{message}\033[0;0m")

    @classmethod
    def warning(cls, message):
        """
        logger for warnings

        param message: the warning message
        type message: str
        """

        cls.logger.warning(message)

    @classmethod
    def critical(cls, message):
        """
        logger for critical message

        param message: the critical message
        type message: str
        """

        cls.logger.critical(message)

    