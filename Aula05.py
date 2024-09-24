with open("","r") as arquivo:
    texto = arquivo.read()
listaTexto = (texto.split())
print(listaTexto)
for lista in listaTexto:
    valor = float(lista)
    soma = soma + valor
print(soma)
