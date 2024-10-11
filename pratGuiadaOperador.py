numero=5
print(numero)
tipo=type(numero)
print(tipo)

bebidaFavorita="Guaraná"
print(bebidaFavorita)
print(type(bebidaFavorita))

bebidaPreco=5.99
print(bebidaPreco)
print(type(bebidaPreco))

bebidaAlcoolica=False
print(bebidaAlcoolica)
print(type(bebidaAlcoolica))

#Prática guiada curso

print(5+8)
print(5-8)
print(5*8)
print(5/8)


num1=10
num2=2
print(num1/num2)

almocoFavorito="Feijoada"
almocoPreco=34.99
print('{:.2f}'.format(almocoPreco+bebidaPreco)) #decimal 2 casas

sobremesaFavorita="Churros"
sobremesaPreco=18.99
convidados=4

valorTotal=(almocoPreco*4)+(bebidaPreco*3)+(sobremesaPreco*2)
print(valorTotal)
valorPorPessoa=valorTotal/convidados
print("Cada um pagará R$",'{:.2f}'.format(valorTotal/convidados))

#Estruturas Relacionais

print(5>2)
print(5<2)
print(5>=2)
print(5<=2)
print(5!=2)
print(5==2)

num1=8
print(num1>2)
print(num1<2)
print(num1>=2)
print(num1<=2)
print(num1!=2)
print(num1==2)

texto="pão"
print(texto=="pão")
print(texto=="Pão")

booleano=False
print(booleano==True)
print(booleano!=True)

#Estuturas condicionais

orcamento=float(input("Qual seu orçamento? "))
bomAmigo=True
if(orcamento>=valorPorPessoa):
    print("Consigo pagar!")
elif(bomAmigo==True):
    print("Obrigado por me ajudar a pagar!")
else:
    print("Pedir ajuda a outro amigo!")

orcamento=float(input("Qual seu orçamento? "))
bomAmigo=False
if(orcamento>=valorPorPessoa):
    print("Consigo pagar!")
elif(bomAmigo==True):
    print("Obrigado por me ajudar a pagar!")
else:
    print("Pedir ajuda a outro amigo!")
