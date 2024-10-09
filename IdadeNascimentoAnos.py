print("Digite seu nome: ")
nome=input()
executar=True
while(executar==True):
    print("Digite o ano de seu nascimento: ")
    try:
        ano=int(input())
        if(ano<1922) or (ano>2023):
            print("O ano precisa ser entre 1922 e 2023")
        else:
            idade = 2024 - ano
            print("O usuário", nome, "completou ou completará", idade, "anos de idade em 2024")
            executar=False
    except:
        print("O ano deve ser digitado com 4 números inteiros")