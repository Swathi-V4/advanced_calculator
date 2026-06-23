from app.operations import OperationFactory


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


class Calculator:
    """Facade class that simplifies calculator operations."""

    def calculate(self, operation_name, a, b):
        calculation = Calculation(operation_name, a, b)
        return calculation.execute()