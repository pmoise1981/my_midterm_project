import pandas as pd

class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=["expression", "result"])  # Use Pandas DataFrame to store history

    def add_to_history(self, expression, result):
        # Add the new entry to history
        self.history = self.history.append({"expression": expression, "result": result}, ignore_index=True)

    def get_history(self):
        return self.history  # Return the DataFrame

