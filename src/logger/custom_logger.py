import logging


class Logger:
    """
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
            cls.logger.info(message)
        else:
            if stage == "START":
                cls.logger.info(f"\033[32;40m<START>\033[0;0m - {message}")
            elif stage == "END":
                cls.logger.info(f"\033[31;40m<END>\033[0;0m   - {message}")
        

    @classmethod
    def debug(cls, message):
        """
        """

        cls.logger.debug(message)

    @classmethod
    def error(cls, message):
        """
        """

        cls.logger.error(f"\033[31;40m{message}\033[0;0m")

    @classmethod
    def warning(cls, message):
        """
        """

        cls.logger.warning(message)

    @classmethod
    def critical(cls, message):
        """
        """

        cls.logger.critical(message)

    