
import sys
from src.brain_mri.logger import logger


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"Error: {error}"

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno

    return (
        f"Error occurred in Python script: [{file_name}] "
        f"at line number: [{line_number}] "
        f"Error message: [{error}]"
    )


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_detail(
            error_message, error_detail
        )
        super().__init__(self.error_message)

        logger.error(self.error_message)
