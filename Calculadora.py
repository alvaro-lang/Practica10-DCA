from colorama import Fore, Style

# Funcion de suma
def sum(num1, num2):

    print(Fore.GREEN + "\nResultado: " + str(float(num1) + float(num2)))
    print(Style.RESET_ALL, end="")

# Funcion de resta
def subtract(num1, num2):
    
    print(Fore.GREEN + "\nResultado: " + str(float(num1) - float(num2)))
    print(Style.RESET_ALL, end="")

# Funcion de multiplicacion
def multiply(num1, num2):

    print(Fore.GREEN + "\nResultado: " + str(float(num1)* float(num2)))
    print(Style.RESET_ALL, end="")    

# Funcion de division
def divide(num1, num2):
    
    print(Fore.GREEN + "\nResultado: " + str(float(num1) / float(num2)))
    print(Style.RESET_ALL, end="")

# Funcion main
def main():

    num1 = ""
    num2 = ""
    operator = ""

    print(Fore.YELLOW + "\n##############")
    print(Fore.YELLOW + "# CALCULADORA #")
    print(Fore.YELLOW + "##############\n")
    print(Style.RESET_ALL, end="")

    while not num1.isdigit():
        print("Introduce primer numero: ", end="")
        num1 = input()
        if not num1.isdigit():
            print(Fore.RED + "Error. Debes introducir un numero.\n")
            print(Style.RESET_ALL, end="")

    while not num2.isdigit():
        print("Introduce segundo numero: ", end="")
        num2 = input()
        if not num2.isdigit():
            print(Fore.RED + "Error. Debes introducir un numero.\n")
            print(Style.RESET_ALL, end="")

    while operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Introduce operador: ", end="")
        operator = input()
        if operator != "+" and operator != "-" and operator != "*" and operator != "/":
            print(Fore.RED + "Error. Debes introducir uno de los siguientes operadores: + , - , * , /\n")
            print(Style.RESET_ALL, end="")

    if operator == "+":
        sum(num1, num2)
    elif operator == "-":
        sum(num1, num2)
    if operator == "*":
        multiply(num1, num2)
    elif operator == "/":
        divide(num1, num2)

if __name__ == "__main__":

    main()
