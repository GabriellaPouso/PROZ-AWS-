def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("\nSelecione o número da operação desejada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha=input("\nDigite sua opção (1, 2, 3 ou 4): ")

num1=float(input("\nDigite o primeiro número: "))
num2=float(input("\nDigite o segunda número: "))
print("\n")
if escolha=="1":
    print(num1, "+", num2, "=", add(num1, num2))
elif escolha=="2":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif escolha=="3":
    print(num1, "x", num2, "=", multiply(num1, num2))
elif escolha=="4":
    print(num1, ":", num2, "=", divide (num1, num2))
