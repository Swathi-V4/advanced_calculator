from app.exceptions import CalculatorError, ConfigurationError, ValidationError


def test_calculator_error():
    error = CalculatorError("Base error")
    assert str(error) == "Base error"


def test_configuration_error():
    error = ConfigurationError("Config error")
    assert str(error) == "Config error"
    assert isinstance(error, CalculatorError)


def test_validation_error():
    error = ValidationError("Validation error")
    assert str(error) == "Validation error"
    assert isinstance(error, CalculatorError)