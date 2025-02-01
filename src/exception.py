import sys
from typing import Any

from src.logger import logging


def error_message_detail(error: Exception, error_detail: Any) -> str:
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"An error encountered in: {file_name} at line: {exc_tb.tb_lineno}. Error {error}"  # noqa
    return error_message


class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detail: Any) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        return self.error_message


if __name__ == "__main__":
    try:
        1 / 0
    except Exception as e:
        logging.info("Error here")
        raise CustomException(e, sys)
