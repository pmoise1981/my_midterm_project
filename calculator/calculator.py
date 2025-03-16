import pandas as pd
from calculator.history_manager import HistoryManager

class Calculator:
    def __init__(self):
        self.history_manager = HistoryManager()  # Initialize HistoryManager

    def evaluate(self, expression: str):
        # Evaluate the expression (simplified)
        result = eval(expression)
        self.history_manager.add_to_history(expression, result)  # Add to history
        return result

    def get_history(self):
        return self.history_manager.get_history()  # Get history from HistoryManager

