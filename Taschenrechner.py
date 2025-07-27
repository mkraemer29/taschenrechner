# Programm:    Taschenrechner
# Version:     0.1.0
# Autor:       Michael Kraemer
# Datum:       27.07.2025
#
# Zweck:       Testprogramm eines Taschenrechners für die vier Grundrechenarten
#              um das Einrichten eines github-Projekts einzuüben
#
# Sprache:     Python3
#
#

def addiere(a, b):
    return a + b

def subrahiere(a, b):
    return a - b

def multipliziere(a, b):
    return a * b

def dividiere(a, b):
    if b == 0:
        return "Fehler: Division durch Null!"
    return a / b

if __name__ == "__main__":
    print("Taschenrechner")
    a = float(input("Erste Zahl: "))
    b = float(input("Zweite Zahl: "))
    op = input("Operation (+, -, *, /): ")

    if op == "+":
        print(addiere(a, b))
    elif op == "-":
        print(subtrahiere(a, b))
    elif op == "*":
        print(multipliziere(a, b))
    elif op == "/":
        print(dividiere(a, b))
    else:
        print("Unbekannte Operation")

