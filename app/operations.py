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


class ModulusStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot calculate modulus by zero.")
        return a % b


class IntegerDivisionStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a // b


class PercentStrategy(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot calculate percentage with zero as the second value.")
        return (a / b) * 100


class AbsoluteDifferenceStrategy(OperationStrategy):
    def execute(self, a, b):
        return abs(a - b)


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
            "modulus": ModulusStrategy(),
            "int_divide": IntegerDivisionStrategy(),
            "percent": PercentStrategy(),
            "abs_diff": AbsoluteDifferenceStrategy(),
        }

        if name not in operations:
            raise ValueError(f"Unsupported operation: {name}")

        return operations[name]