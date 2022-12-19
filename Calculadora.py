from colorama import Fore, Style

def sum(num1, num2):

    print(Fore.GREEN + "\nResult: " + str(float(num1) + float(num2)))
    print(Style.RESET_ALL, end="")

def subtract(num1, num2):
    
    print(Fore.GREEN + "\nResult: " + str(float(num1) - float(num2)))
    print(Style.RESET_ALL, end="")

def multiply(num1, num2):

    print(Fore.GREEN + "\nResult: " + str(float(num1)* float(num2)))
    print(Style.RESET_ALL, end="")    

def divide(num1, num2):
    
    print(Fore.GREEN + "\nResult: " + str(float(num1) / float(num2)))
    print(Style.RESET_ALL, end="")

def main():

    num1 = ""
    num2 = ""
    operator = ""

    print(Fore.YELLOW + "\n##############")
    print(Fore.YELLOW + "# CALCULATOR #")
    print(Fore.YELLOW + "##############\n")
    print(Style.RESET_ALL, end="")

    while not num1.isdigit():
        print("Introduce first number: ", end="")
        num1 = input()
        if not num1.isdigit():
            print(Fore.RED + "Error. Debes introducir un numero.\n")
            print(Style.RESET_ALL, end="")

    while not num2.isdigit():
        print("Introduce second number: ", end="")
        num2 = input()
        if not num2.isdigit():
            print(Fore.RED + "Error. Debes introducir un numero.\n")
            print(Style.RESET_ALL, end="")

    while operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Introduce operator: ", end="")
        operator = input()
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print(Fore.RED + "Error. Debes introducir uno de los siguientes operadores: + , - , * , /\n")
            print(Style.RESET_ALL, end="")

    if operator == "+":
        sum(num1, num2)
    elif operator == "-":
        subtract(num1, num2)
    if operator == "*":
        multiply(num1, num2)
    elif operator == "/":
        divide(num1, num2)

if __name__ == "__main__":

    main()