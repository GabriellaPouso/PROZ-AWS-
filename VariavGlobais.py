def media_aluno(notal, nota2):
    media = (notal + nota2) / 2
    return media
notal = float(input("Qual a nota 1? "))
nota2 = float(input("Qual a nota 2? "))
resultado = media_aluno(notal, nota2)
print(resultado)

def ant_e_suc(num):
  ant = num - 1
  suc = num + 1
  return ant, suc

antecessor, sucessor = ant_e_suc(5)
print(antecessor)
print(sucessor)

def calculadoraImc(peso, altura):
  imc = peso/(altura*altura)
  if(imc<=18.5): return "Magreza"
  elif(imc>18.5) and (imc<=24.9): return "Saudavel"
  elif(imc>=25) and (imc<=29.9): return "Sobrepeso"
  elif(imc>30) and (imc<=39.9): return "Obesidade grau 1"
  elif(imc>35) and (imc<=39.9): return "Obesidade grau 2"
  else: return "Obesidade mórbida grau 3"
peso = float(input("Qual seu peso? "))
altura = float(input("Qual sua altura? "))
resultado = calculadoraImc(peso, altura)
print(resultado)

def aprovacao(nota1, nota2, nota3):
  media = (nota1 + nota2 + nota3)/3
  if(media>=7):
    res="Aprovado"
  else:
    res="Reprovado"
  return res
nota1=float(input("Qual a nota 1? "))
nota2=float(input("Qual a nota 2? "))
nota3=float(input("Qual a nota 3? "))
resultado=aprovacao(nota1, nota2, nota3)
print(resultado)
  
def operacao(num_lim, incre):
  contador = 0
  for i in range(0, num_lim, incre):
    contador = contador + 1
    return contador
num_lim=30
incre=48
resultado = operacao(num_lim, incre)
print(resultado)