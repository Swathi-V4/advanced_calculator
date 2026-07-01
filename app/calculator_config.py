import os
from dotenv import load_dotenv

from app.exceptions import ConfigurationError


class CalculatorConfig:
    """Loads and validates calculator configuration from .env."""

    def __init__(self):
        load_dotenv()

        self.log_dir = os.getenv("CALCULATOR_LOG_DIR", ".")
        self.history_dir = os.getenv("CALCULATOR_HISTORY_DIR", ".")

        self.log_file = os.getenv(
            "CALCULATOR_LOG_FILE",
            "calculator.log"
        )

        self.history_file = os.getenv(
            "CALCULATOR_HISTORY_FILE",
            os.getenv("HISTORY_FILE", "calculator_history.csv")
        )

        self.max_history_size = int(
            os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "100")
        )

        self.auto_save = os.getenv(
            "CALCULATOR_AUTO_SAVE",
            "true"
        ).lower() == "true"

        self.precision = int(
            os.getenv("CALCULATOR_PRECISION", "2")
        )

        self.max_input_value = float(
            os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1000000")
        )

        self.default_encoding = os.getenv(
            "CALCULATOR_DEFAULT_ENCODING",
            "utf-8"
        )

        self.validate()

    def validate(self):
        if not self.log_dir:
            raise ConfigurationError("CALCULATOR_LOG_DIR cannot be empty.")

        if not self.history_dir:
            raise ConfigurationError("CALCULATOR_HISTORY_DIR cannot be empty.")

        if not self.log_file:
            raise ConfigurationError("CALCULATOR_LOG_FILE cannot be empty.")

        if not self.history_file:
            raise ConfigurationError("CALCULATOR_HISTORY_FILE cannot be empty.")

        if self.max_history_size <= 0:
            raise ConfigurationError(
                "CALCULATOR_MAX_HISTORY_SIZE must be greater than zero."
            )

        if self.precision < 0:
            raise ConfigurationError(
                "CALCULATOR_PRECISION cannot be negative."
            )

        if self.max_input_value <= 0:
            raise ConfigurationError(
                "CALCULATOR_MAX_INPUT_VALUE must be greater than zero."
            )

        if not self.default_encoding:
            raise ConfigurationError(
                "CALCULATOR_DEFAULT_ENCODING cannot be empty."
            )