idade=int(input("Informe a idade: "))
if(idade<13):
    print("Criança")
elif(idade>=13 and idade<18):
    print("Adolescente")
elif(idade>=18 and idade<60):
    print("Adulto")
else:
    print("Idoso")
