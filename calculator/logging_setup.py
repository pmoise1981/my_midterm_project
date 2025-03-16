import logging
import os

def setup_logging():
    # Set logging level from environment variable (default to INFO)
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()  # Default to INFO if not set
    logging.basicConfig(level=log_level)
    logger = logging.getLogger()

    # Log an example message
    logger.info("Logging setup complete.")

    return logger

