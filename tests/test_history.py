import pandas as pd
from app.history import HistoryManager


def test_add_record():
    history = HistoryManager()
    history.add_record("add", 2, 3, 5)

    assert len(history.get_history()) == 1


def test_clear():
    history = HistoryManager()
    history.add_record("add", 1, 1, 2)

    history.clear()

    assert len(history.get_history()) == 0


def test_save_and_load(tmp_path):
    file_path = tmp_path / "history.csv"

    history = HistoryManager()
    history.add_record("multiply", 2, 4, 8)
    history.save(file_path)

    loaded = HistoryManager()
    loaded.load(file_path)

    assert len(loaded.get_history()) == 1
    assert loaded.get_history().iloc[0]["result"] == 8