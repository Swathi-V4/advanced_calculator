class CalculatorMemento:
    """Stores a saved calculator state."""

    def __init__(self, state):
        self.state = state


class HistoryCaretaker:
    """Manages undo and redo states using the Memento pattern."""

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, state):
        self.undo_stack.append(CalculatorMemento(state))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return None

        memento = self.undo_stack.pop()
        self.redo_stack.append(memento)
        return memento.state

    def redo(self):
        if not self.redo_stack:
            return None

        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento.state