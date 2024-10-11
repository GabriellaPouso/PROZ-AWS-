#Estruturas de Repetição
#Variável contadora
#Condição de Parada
#Incremento
i=0
while(i<3):
    print("Olá, Mundo")
    i=i+1   #ou "i+=1"

for i in range(3):
    print("Nova frase")

for i in range(6):
    plantaAtual=str(i)
    print("Rega a planta "+plantaAtual)
    
def multiplicar(a,b):
    multi=a*b
    return multi
a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))
res=multiplicar(a,b)
print("O resultado de",a,"x", b, "é igual a", res)