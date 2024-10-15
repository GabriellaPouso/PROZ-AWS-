import customtkinter as login

app = login.CTk()
app.geometry("300x300")
app.title("Talento Cloud")


def cliqueEntrar():
    appHome=login.CTkToplevel(app)
    appHome.geometry("300x300")
    appHome.title("Home")
    def fechar():
        appHome.destroy()
        appHome.update()
    textHome=login.CTkLabel(appHome,text="Seja bem vindo(a)")
    textHome.pack(padx=10, pady=10)
    button=login.CTkButton(appHome, text="entrar",command=fechar)
    button.pack(padx=10,pady=10)
    

texto = login.CTkLabel(app, text="Login").pack(padx=10, pady=10)
email = login.CTkEntry(app, placeholder_text="E-mail").pack(padx=10, pady=10)
senha = login.CTkEntry(app, placeholder_text="Senha").pack(padx=10, pady=10)
checkbox = login.CTkCheckBox(app, text="Lembrar senha?").pack(padx=10, pady=10)
button = login.CTkButton(
    app, text="Entrar", command=cliqueEntrar).pack(padx=10, pady=10)
app.mainloop()
