"""
The provided code is creating a logging setup in Python. 
It sets up a logger that outputs to a file named with the current date and time, and is located in a "logs" directory.
Each log message includes the time it was logged, the line number where the logging call was made, the logger's name,
the level of the log (INFO, WARNING, ERROR, etc.), and the actual log message.

"""

import logging
import os
from datetime import datetime

# Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Generate path for the log directory inside the current working directory
logs_dir = os.path.join(os.getcwd(), "logs")

# Create the logs directory if it doesn't exist
os.makedirs(logs_dir, exist_ok=True)

# Get full path to the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging module. Set the filename to the log file path, 
# specify the format of log messages, and set the log level to INFO.
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

if __name__ == "__main__":
    logging.info("Logging has started")


