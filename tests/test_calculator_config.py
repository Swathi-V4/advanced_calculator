import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError


def test_default_precision():
    config = CalculatorConfig()
    assert config.get("precision") == 2


def test_set_value():
    config = CalculatorConfig()
    config.set("precision", 5)

    assert config.get("precision") == 5


def test_save_and_load(tmp_path):
    file_path = tmp_path / "config.json"

    config = CalculatorConfig()
    config.set("precision", 4)
    config.save(file_path)

    loaded = CalculatorConfig()
    loaded.load(file_path)

    assert loaded.get("precision") == 4


def test_load_missing_file():
    config = CalculatorConfig()

    with pytest.raises(ConfigurationError):
        config.load("does_not_exist.json")