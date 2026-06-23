from app.calculator_memento import HistoryCaretaker


def test_save_and_undo():
    caretaker = HistoryCaretaker()

    caretaker.save(10)
    caretaker.save(20)

    assert caretaker.undo() == 20
    assert caretaker.undo() == 10


def test_undo_empty():
    caretaker = HistoryCaretaker()

    assert caretaker.undo() is None