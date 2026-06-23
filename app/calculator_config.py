import json
from app.exceptions import ConfigurationError


class CalculatorConfig:
    def __init__(self):
        self.settings = {
            "precision": 2
        }

    def get(self, key):
        return self.settings.get(key)

    def set(self, key, value):
        self.settings[key] = value

    def save(self, filename):
        with open(filename, "w") as f:
            json.dump(self.settings, f)

    def load(self, filename):
        try:
            with open(filename, "r") as f:
                self.settings = json.load(f)
        except Exception as e:
            raise ConfigurationError(str(e))