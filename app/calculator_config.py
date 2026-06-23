import os
from dotenv import load_dotenv

from app.exceptions import ConfigurationError


class CalculatorConfig:
    """Loads and validates application configuration."""

    def __init__(self):
        load_dotenv()

        self.history_file = os.getenv(
            "HISTORY_FILE",
            "calculator_history.csv"
        )

        self.validate()

    def validate(self):
        if not self.history_file:
            raise ConfigurationError(
                "HISTORY_FILE cannot be empty."
            )