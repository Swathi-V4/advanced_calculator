from app.calculator_repl import CalculatorREPL


def test_repl_creation():
    repl = CalculatorREPL()

    assert repl is not None
    assert hasattr(repl, "calculator")