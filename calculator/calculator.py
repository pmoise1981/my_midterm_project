import logging
from calculator.history_manager import HistoryManager

class Calculator:
    def __init__(self):
        self.history_manager = HistoryManager()

    def evaluate(self, expression):
        try:
            result = eval(expression)
            logging.info(f"Evaluating expression: {expression} = {result}")
            return result
        except Exception as e:
            logging.error(f"Error evaluating expression: {expression}, Error: {str(e)}")
            return None

    def get_history(self):
        return self.history_manager.load_history()

