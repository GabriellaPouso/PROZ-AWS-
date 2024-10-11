lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas)
# Imprimirá: ['maçã', 'banana', 'pera']

lista_frutas = ['maçã', 'banana', 'pera']
# 'maçã' tem o índice 0
# 'banana' tem o índice 1
# 'pera' tem o índice 2

lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas[0])
# Imprimirá: 'maçã'

lista_frutas = ['maçã', 'banana', 'pera']
fruta_preferida = lista_frutas[2]
print(fruta_preferida)
print(lista_frutas)
# O primeiro print() imprimirá: 'pera'
# O segundo print() imprimirá: ['maçã', 'banana', 'pera']

lista_frutas = ['maçã', 'banana', 'pera']
quantidade_frutas = len(lista_frutas)
print(quantidade_frutas)
# Imprimirá o número 3, pois lista_frutas tem três elementos

lista_frutas = ['maçã', 'banana', 'pera']
print(len(lista_frutas))
# Também imprimirá o número 3

lista_musicos=['Djavan','Roberto Carlos','Elis Regina','Tom Jobim','Milton Nascimento','Chico Buarque','Nara Leão','Pitty','Simonal','Moacir Santos','Caetano Veloso','Elza Soares','Paulinho da Viola','Yamandú Costa','Gal Costa']
print(len(lista_musicos))
print(lista_musicos[2],lista_musicos[9],lista_musicos[14])
print(lista_musicos[2])
print(lista_musicos[9])
print(lista_musicos[14])

lista_frutas = ['maçã', 'banana', 'pera']
print(lista_frutas[0])
print(lista_frutas[1])
print(lista_frutas[2])
# Imprimirá:
# maçã
# banana
# pera

lista_frutas = ['maçã', 'banana', 'pera']
for i in range(3):
    print(lista_frutas[i])
# Imprimirá:
# maçã
# banana
# pera

lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]
for i in range(15):
    print(lista_num[i])
    
lista_num = [2, 45, 65, 78, 126, 987, 457, 345, 679, 107, 2345, 452, 3, 34, 560]
for i in range(len(lista_num)):
    print(lista_num[i])

