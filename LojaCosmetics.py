lista_produtos=['máscaras faciais','batons','esmaltes','perfumes','loções','xampus','sabonetes','delineadores']
for i in range(len(lista_produtos)):
    print("Temos",lista_produtos[i],"à venda!")

lista_produtos[1]="rímel"
lista_produtos[4]="cremes hidratantes"
lista_produtos.pop()
lista_produtos.append("bases")
lista_produtos.append("protetores solares")
for i in range(len(lista_produtos)):
    print("Temos",lista_produtos[i],"à venda!")