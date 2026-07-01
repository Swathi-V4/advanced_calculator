import pandas as pd
from datetime import datetime


class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(
            columns=["operation", "a", "b", "result", "timestamp"]
        )

    def add_record(self, operation, a, b, result):
        self.history.loc[len(self.history)] = [
            operation,
            a,
            b,
            result,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ]

    def clear(self):
        self.history = pd.DataFrame(
            columns=["operation", "a", "b", "result", "timestamp"]
        )

    def save(self, filename="history.csv"):
        self.history.to_csv(filename, index=False)

    def load(self, filename="history.csv"):
        self.history = pd.read_csv(filename)

    def get_history(self):
        return self.history