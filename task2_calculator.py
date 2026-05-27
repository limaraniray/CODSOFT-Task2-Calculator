"""
CODSOFT Python Internship - Task 2
Calculator Application
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Division by zero is not allowed!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "❌ Error: Division by zero is not allowed!"
    return a % b

def power(a, b):
    return a ** b

def show_menu():
    print("\n" + "="*40)
    print("         🧮 CALCULATOR APP")
    print("="*40)
    print("1. Addition       (+)")
    print("2. Subtraction    (-)")
    print("3. Multiplication (*)")
    print("4. Division       (/)")
    print("5. Modulus        (%)")
    print("6. Power          (**)")
    print("7. Exit")
    print("="*40)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the Calculator App!")
    while True:
        show_menu()
        choice = input("Choose an operation (1-7): ").strip()

        if choice == "7":
            print("👋 Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5", "6"):
            print("❌ Invalid choice. Please select 1-7.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        operations = {
            "1": (add,      "+"),
            "2": (subtract, "-"),
            "3": (multiply, "*"),
            "4": (divide,   "/"),
            "5": (modulus,  "%"),
            "6": (power,    "**"),
        }

        func, symbol = operations[choice]
        result = func(num1, num2)

        if isinstance(result, float) and result == int(result):
            result_display = int(result)
        else:
            result_display = result

        print(f"\n✅ Result: {num1} {symbol} {num2} = {result_display}")

        again = input("\nPerform another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("👋 Goodbye!")
            break

if __name__ == "__main__":
    main()
