def calculadora(num1, num2, operacao):
    if(operacao == 1):
        return num1+num2
    elif(operacao == 2):
        return num1-num2
    elif(operacao == 3):
        return num1*num2
    elif(operacao == 4):
        return num1/num2
    else:
        return 0
exec = True
while(exec == True):
    print("Qual operação quer realizar?")
    print("1: Soma; 2: Subtração; 3: Multiplicação; 4: Divisão; 0: Sair")
    operacao = float(input())
    if(operacao < 0) or (operacao > 4):
        print("Essa operação não existe")
    elif(operacao == 0):
        exec = False
    else:
        num1=float(input("Insira o primeiro número da operação: "))
        num2=float(input("Insira o segundo número da operação: "))
        resultado = calculadora(num1, num2, operacao)
        print("O resultado é:", resultado)