idade=int(input("Digite a sua idade: "))
if idade>=18:
    print("Maior de idade")
else:
    idade<18
    print("Menor de idade")

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

i = 1       #dá pra colocar um i=int(input("Digite o número: "))
a = 2       #dá pra colocar um a=int(input("Digite o número: "))
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
    op = input("Deseja Continuar(s|n)?: ")
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
  print(lista, "R$",produtos[lista])
 
def soma(nomes, numeros):
    print(f"Lista de nomes: {nomes}")
    print(f"Vetor de números: {numeros}")
 
lista_nomes = ["Alice", "Bob", "Carlos", "Diana", "Eva"]
vetor_numeros = [1, 2, 3, 4, 5]
soma(lista_nomes, vetor_numeros)

soma = 0
with open("dados/soma.txt","r") as arquivo:
    texto = arquivo.read()
listaTexto = (texto.split())
print(listaTexto)
for lista in listaTexto:
    valor = float(lista)
    soma = soma + valor
print(soma)

def lista():
    nlista= []
    while(True):
        valor=input("Informe um valor (sair = s): ")
        if(valor == "s"):
            return nlista
        nlista.append(valor)
list = lista()
print(list)