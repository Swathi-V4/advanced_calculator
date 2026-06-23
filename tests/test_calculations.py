import pytest
from app.calculation import Calculation, Calculator


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 1, 2, 3),
        ("subtract", 10, 4, 6),
        ("multiply", 3, 5, 15),
        ("divide", 8, 2, 4),
        ("power", 3, 2, 9),
        ("root", 16, 2, 4),
    ],
)
def test_calculation_execute(operation, a, b, expected):
    calc = Calculation(operation, a, b)
    assert calc.execute() == pytest.approx(expected)
    assert calc.result == pytest.approx(expected)


def test_calculator_facade():
    calculator = Calculator()
    assert calculator.calculate("add", 2, 2) == 4