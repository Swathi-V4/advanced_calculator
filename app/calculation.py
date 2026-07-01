from app.operations import OperationFactory
from app.history import HistoryManager
from app.logger import setup_logger


class Calculation:
    """Represents one calculator operation."""

    def __init__(self, operation_name, a, b):
        self.operation_name = operation_name
        self.a = a
        self.b = b
        self.result = None

    def execute(self):
        operation = OperationFactory.create_operation(self.operation_name)
        self.result = operation.execute(self.a, self.b)
        return self.result


class CalculationObserver:
    """Base observer for calculation events."""

    def update(self, calculation):
        pass  # pragma: no cover


class LoggingObserver(CalculationObserver):
    """Observer that logs calculations to a file and stores them in memory."""

    def __init__(self):
        self.logs = []
        self.logger = setup_logger()

    def update(self, calculation):
        message = (
            f"{calculation.operation_name}: "
            f"{calculation.a}, {calculation.b} = {calculation.result}"
        )
        self.logs.append(message)
        self.logger.info(message)


class AutoSaveObserver(CalculationObserver):
    """Observer that automatically saves calculations to history."""

    def __init__(self, history_manager):
        self.history_manager = history_manager

    def update(self, calculation):
        self.history_manager.add_record(
            calculation.operation_name,
            calculation.a,
            calculation.b,
            calculation.result,
        )


class Calculator:
    """Facade class that simplifies calculator operations."""

    def __init__(self):
        self.history = HistoryManager()
        self.observers = []

        # Register the logging observer automatically
        self.add_observer(LoggingObserver())

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation)

    def calculate(self, operation_name, a, b):
        calculation = Calculation(operation_name, a, b)
        calculation.execute()
        self.notify_observers(calculation)
        return calculation.result