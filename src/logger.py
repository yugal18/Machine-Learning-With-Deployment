import logging
import os
from datetime import datetime



# Define the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path
logs_dir = os.path.join(os.getcwd(), "logs")

# Ensure the logs directory exists
os.makedirs(logs_dir, exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(levelname)s - %(message)s",
    level=logging.INFO,  # Set the logging level
)


