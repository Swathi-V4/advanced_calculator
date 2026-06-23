from abc import ABC, abstractmethod
import math


class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class AddStrategy(OperationStrategy):
    def execute(self, a, b):
        return a + b


class SubtractStrategy(OperationStrategy):
    def execute(self, a, b):
        return a - b


class MultiplyStrategy(OperationStrategy):
    def execute(self, a, b):
        return a * b


class DivideStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class PowerStrategy(OperationStrategy):
    def execute(self, a, b):
        return a ** b


class RootStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root cannot be zero.")
        return math.pow(a, 1 / b)


class OperationFactory:
    @staticmethod
    def create_operation(name):
        operations = {
            "add": AddStrategy(),
            "subtract": SubtractStrategy(),
            "multiply": MultiplyStrategy(),
            "divide": DivideStrategy(),
            "power": PowerStrategy(),
            "root": RootStrategy(),
        }

        if name not in operations:
            raise ValueError(f"Unsupported operation: {name}")

        return operations[name]