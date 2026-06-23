import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError


def test_default_history_file():
    config = CalculatorConfig()
    assert config.history_file == "calculator_history.csv"


def test_history_file_exists():
    config = CalculatorConfig()
    assert isinstance(config.history_file, str)


def test_validate_success():
    config = CalculatorConfig()
    config.validate()


def test_empty_history_file():
    config = CalculatorConfig()
    config.history_file = ""

    with pytest.raises(ConfigurationError):
        config.validate()