from app.calculation import Calculator


class CalculatorREPL:
    def __init__(self):
        self.calculator = Calculator()

    def run(self): # pragma: no cover
        print("Advanced Calculator")
        print("Type 'exit' to quit")

        while True:
            operation = input("Operation: ").strip().lower()

            if operation == "exit":
                print("Goodbye!")
                break

            try:
                a = float(input("First number: "))
                b = float(input("Second number: "))

                result = self.calculator.calculate(operation, a, b)
                print(f"Result: {result}")

            except Exception as e:
                print(f"Error: {e}")