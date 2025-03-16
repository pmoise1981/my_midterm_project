import logging
from calculator.logging_setup import setup_logging

def test_logging():
    setup_logging()
    logger = logging.getLogger()
    assert logger.level == logging.INFO

