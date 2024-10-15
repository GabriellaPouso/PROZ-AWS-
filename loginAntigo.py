import tkinter  # importa o framework

janelaLogin = tkinter.Tk()  # chamamento da função

# largura versus altura
janelaLogin.geometry("600x500")
janelaLogin.title("Talento Cloud")

def cliqueEntrar():
    print("Logado")


texto = tkinter.Label(janelaLogin, text="Login")
texto.pack(padx=10, pady=10)

email=tkinter.Entry(janelaLogin, text="Seu e-mail ou login")
email.pack(padx=10,pady=10)

senha=tkinter.Entry(janelaLogin, text="Sua senha")
senha.pack(padx=10,pady=10)

checkbox=tkinter.Checkbutton(janelaLogin,text="Continuar conectado")
checkbox.pack(padx=10,pady=10)

button=tkinter.Button(janelaLogin,text="Entrar",command=cliqueEntrar)
button.pack(padx=10,pady=10)

janelaLogin.mainloop()
