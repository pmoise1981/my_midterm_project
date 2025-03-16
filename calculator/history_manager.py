import pandas as pd
import os

class HistoryManager:
    def __init__(self, history_file='history.csv'):
        self.history_file = history_file

    def save_history(self, expression, result):
        df = self.load_history()
        new_entry = pd.DataFrame({'expression': [expression], 'result': [result]})
        df = pd.concat([df, new_entry], ignore_index=True)
        df.to_csv(self.history_file, index=False)

    def load_history(self):
        if os.path.exists(self.history_file):
            return pd.read_csv(self.history_file)
        return pd.DataFrame(columns=['expression', 'result'])

    def clear_history(self):
        if os.path.exists(self.history_file):
            os.remove(self.history_file)

