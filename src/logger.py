import datetime
import logging
import os

FILE_NAME = f"{datetime.datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs", FILE_NAME)
os.makedirs(logs_dir, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_dir, FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s in %(module)s at %(funcName)s:%(lineno)d - %(message)s thread: %(threadName)s, process_id: %(process)d process_name: %(processName)s",  # noqa
    level=logging.INFO,
)


if __name__ == "__main__":
    logging.info("Logging has started.")
