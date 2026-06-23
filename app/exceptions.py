class CalculatorError(Exception):
    """Base exception for calculator errors."""


class ConfigurationError(CalculatorError):
    """Raised when configuration is invalid."""


class ValidationError(CalculatorError):
    """Raised when user input is invalid."""