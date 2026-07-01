# pragma: no cover
from colorama import Fore, Style, init

from app.calculation import Calculator, AutoSaveObserver
from app.calculator_config import CalculatorConfig
from app.calculator_memento import HistoryCaretaker
from app.input_validators import validate_number

init(autoreset=True)


class CalculatorREPL:
    """Interactive calculator command-line interface."""

    def __init__(self):
        self.config = CalculatorConfig()
        self.calculator = Calculator()
        self.caretaker = HistoryCaretaker()
        self.last_result = None

        self.calculator.add_observer(
            AutoSaveObserver(self.calculator.history)
        )

    def show_help(self):
        print(Fore.CYAN + "Available Commands:")
        print("  help      - Show this help menu")
        print("  history   - Display calculation history")
        print("  clear     - Clear history")
        print("  undo      - Undo last calculation")
        print("  redo      - Redo last calculation")
        print("  save      - Save history")
        print("  load      - Load history")
        print("  exit      - Exit calculator")

        print(Fore.YELLOW + "\nAvailable Operations:")
        print("  add")
        print("  subtract")
        print("  multiply")
        print("  divide")
        print("  power")
        print("  root")
        print("  modulus")
        print("  int_divide")
        print("  percent")
        print("  abs_diff")

    def show_history(self):
        print(self.calculator.history.get_history())

    def clear_history(self):
        self.calculator.history.clear()
        print(Fore.YELLOW + "History cleared.")

    def save_history(self):
        self.calculator.history.save(self.config.history_file)
        print(Fore.GREEN + "History saved.")

    def load_history(self):
        self.calculator.history.load(self.config.history_file)
        print(Fore.GREEN + "History loaded.")

    def undo(self):
        result = self.caretaker.undo()
        self.last_result = result
        print(Fore.YELLOW + f"Undo result: {result}")

    def redo(self):
        result = self.caretaker.redo()
        self.last_result = result
        print(Fore.YELLOW + f"Redo result: {result}")

    def process_command(self, command):
        command = command.strip().lower()

        if command == "help":
            self.show_help()
            return True

        if command == "history":
            self.show_history()
            return True

        if command == "clear":
            self.clear_history()
            return True

        if command == "save":
            self.save_history()
            return True

        if command == "load":
            self.load_history()
            return True

        if command == "undo":
            self.undo()
            return True

        if command == "redo":
            self.redo()
            return True

        if command == "exit":
            print(Fore.CYAN + "Goodbye!")
            return False

        return None

    def run(self):
        print(Fore.CYAN + "Advanced Calculator")
        self.show_help()

        while True:
            operation = input("\nOperation or command: ")

            command_result = self.process_command(operation)

            if command_result is False:
                break

            if command_result is True:
                continue

            try:
                a = validate_number(input("First number: "))
                b = validate_number(input("Second number: "))

                result = self.calculator.calculate(operation, a, b)

                self.caretaker.save(result)
                self.last_result = result

                print(Fore.GREEN + f"Result: {result}")

            except Exception as error:
                print(Fore.RED + f"Error: {error}")


if __name__ == "__main__":
    CalculatorREPL().run()