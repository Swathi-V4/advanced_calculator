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


def test_redo():
    caretaker = HistoryCaretaker()

    caretaker.save(10)
    caretaker.save(20)

    assert caretaker.undo() == 20
    assert caretaker.redo() == 20


def test_redo_empty():
    caretaker = HistoryCaretaker()

    assert caretaker.redo() is None


def test_save_clears_redo_stack():
    caretaker = HistoryCaretaker()

    caretaker.save(10)
    caretaker.undo()
    caretaker.save(30)

    assert caretaker.redo() is None