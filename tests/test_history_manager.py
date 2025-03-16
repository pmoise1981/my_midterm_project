import os
import pytest
from calculator.history_manager import HistoryManager

def test_history_manager():
    history_manager = HistoryManager()
    history_manager.save_history("3 + 5", 8)
    history = history_manager.load_history()
    assert history.shape[0] == 1
    assert history.loc[0, 'expression'] == "3 + 5"
    assert history.loc[0, 'result'] == 8

