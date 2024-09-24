idade=int(input("Digite a sua idade: "))
if idade>=18:
    print("Maior de idade")
else:
    idade<18
    print("Menor de idade")

idade=int(input("Digite a sua idade: "))
result = "Maior de idade" if idade>=18 and "Menor de idade" else idade<18

i=0
while(i<=10):
    if(i % 2 ==1):
        print(f"É impar {i}")
    if(i % 2 ==0):
        print(f"É par {i}")
    i=i+1

i=0
while(i<=10):
    if(i % 2 ==1):
        print(f"É impar {i}")
    if(i % 2 ==0):
        print(f"É par {i}")
    i=i+1

i = 1
a = 2
print("Adição")
while(i <= 10):
    print(f"{a} + {i} = {a+i}")
    i = i + 1
print("Multiplicação")
i = 1
while(i <= 10):
    print(f"{a} * {i} = {a*i}")
    i = i + 1
    
    i = 1
op = 's'
while (op == 's'):
    nome = input("Nome: ")
    print("O nome informado foi: ", nome)
    op = input("Deseja Continuar: ")
    i = i+1
    
a=2
b="2"
print(a == b) #compara type

for i in range(0,11):
    print(i)
    
lista = ["Gabriella", "Thiago", "Anna Luíza"]
for i in range(3):
    print(i, lista)
    
for i in "Gabriella":
    print(i)
    
produtos = {
  "faca": 10,
  "garfo": 10,
  "panela": 200,
  "frigideira": 50,
  "flavorstone": 300,
}
for lista in produtos:
  print(lista, produtos[lista])
