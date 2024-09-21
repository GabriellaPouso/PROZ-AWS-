def operacao(num_lim, incre):
  contador = 0
  for i in range(0, num_lim, incre):
    contador = contador + 1
    return contador
num_lim=30
incre=48
resultado = operacao(num_lim, incre)
print(resultado)
