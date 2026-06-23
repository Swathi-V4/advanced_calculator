import pytest
from app.calculation import (
    Calculation,
    Calculator,
    LoggingObserver,
    AutoSaveObserver,
)


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


def test_logging_observer():
    calculator = Calculator()
    logger = LoggingObserver()
    calculator.add_observer(logger)

    calculator.calculate("add", 2, 3)

    assert len(logger.logs) == 1
    assert "add" in logger.logs[0]


def test_auto_save_observer():
    calculator = Calculator()
    auto_save = AutoSaveObserver(calculator.history)
    calculator.add_observer(auto_save)

    calculator.calculate("multiply", 3, 4)

    history = calculator.history.get_history()
    assert len(history) == 1
    assert history.iloc[0]["operation"] == "multiply"
    assert history.iloc[0]["result"] == 12