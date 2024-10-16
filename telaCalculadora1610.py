import customtkinter as janela
from PIL import Image
main=janela.CTk()
main.geometry("300x500")
main.iconbitmap("ico-icon-ghost.ico")
main.title("Calculadora Proz")

img=janela.CTkImage(Image.open("ico-icon-ghost.ico"), size=(150,115))

imagem = janela.CTkLabel(main, image = img, text="")
imagem.pack(padx=10,pady=10)

texto1 = janela.CTkLabel(main, text="Primeiro Número: ")
texto1.pack()

numero1 = janela.CTkEntry(main, placeholder_text="Numero")
numero1.pack(padx=0,pady=10)

texto2 = janela.CTkLabel(main, text="Segundo Número: ")
texto2.pack()

numero2 = janela.CTkEntry(main,placeholder_text="Número")
numero2.pack(padx=10,pady=10)

valor_btn = janela.StringVar()
valor = janela.CTkLabel(main, textvariable=valor_btn, text_color="#FF7E06").pack()

def soma():
    soma = int(numero1.get()) + int(numero2.get())
    valor_btn.set(soma)
    print(soma)
    
def sub():
    sub = int(numero1.get()) - int(numero2.get())
    valor_btn.set(sub)
    print(sub)
    
def multi():
    multi = int(numero1.get()) * int(numero2.get())
    valor_btn.set(multi)
    print(multi)
    
def divi():
    divi = int(numero1.get()) / int(numero2.get())
    valor_btn.set(divi)
    print(divi)

btn = janela.CTkButton(main, text="+", fg_color="#FF7E06",text_color="#000",hover_color="", command=soma)
btn.pack(padx=5,pady=5)
btn = janela.CTkButton(main, text="-", fg_color="#FF7E06", text_color="#000",command=sub)
btn.pack(padx=5,pady=5)
btn = janela.CTkButton(main, text="x", fg_color="#FF7E06",text_color="#000", command=multi)
btn.pack(padx=5,pady=5)
btn = janela.CTkButton(main, text="/", fg_color="#FF7E06", text_color="#000",command=divi)
btn.pack(padx=5,pady=5)

    
main.mainloop()