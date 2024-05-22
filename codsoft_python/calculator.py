from colorama import init, Fore

init(autoreset=True)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def main():
    print(Fore.MAGENTA + "╔════════════════════════════════╗")
    print("║        Simple Calculator       ║")
    print("╚════════════════════════════════╝")

    while True:
        print("Operations:")
        print("1. " + Fore.CYAN + "Addition " + Fore.MAGENTA + "(+)")
        print("2. " + Fore.CYAN + "Subtraction " + Fore.MAGENTA + "(-)")
        print("3. " + Fore.CYAN + "Multiplication " + Fore.MAGENTA + "(*)")
        print("4. " + Fore.CYAN + "Division " + Fore.MAGENTA + "(/)")
        print("5. " + Fore.YELLOW + "Exit")

        choice = input(Fore.YELLOW + "Enter operation number (1-5): ")

        if choice == '5':
            print(Fore.MAGENTA + "Exiting the calculator.")
            break

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input(Fore.YELLOW + "Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                    print(Fore.GREEN + f"Result: {num1} + {num2} = {result}")
                elif choice == '2':
                    result = subtract(num1, num2)
                    print(Fore.GREEN + f"Result: {num1} - {num2} = {result}")
                elif choice == '3':
                    result = multiply(num1, num2)
                    print(Fore.GREEN + f"Result: {num1} * {num2} = {result}")
                elif choice == '4':
                    result = divide(num1, num2)
                    if isinstance(result, str):
                        print(Fore.RED + result)
                    else:
                        print(Fore.GREEN + f"Result: {num1} / {num2} = {result}")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter numeric values.")
        else:
            print(Fore.RED + "Invalid input. Please enter a valid operation number (1-5).")

if __name__ == "__main__":
    main()

