import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("Calculator")
app.geometry("600x250")
app.iconbitmap("ico-icon-ghost.ico")
app.grid_columnconfigure((0), weight=1)


numero1 = customtkinter.CTkEntry(app, placeholder_text="0")
numero1.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=4)

#linha 2
button = customtkinter.CTkButton(app, text="7", command=button_callback)
button.grid(row=2, column=0, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="8", command=button_callback)
button.grid(row=2, column=1, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="9", command=button_callback)
button.grid(row=2, column=2, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="+", command=button_callback)
button.grid(row=2, column=3, padx=10, pady=(0, 10), sticky="w")


#linha 3
button = customtkinter.CTkButton(app, text="4", command=button_callback)
button.grid(row=3, column=0, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="5", command=button_callback)
button.grid(row=3, column=1, padx=10, pady=(0, 10), sticky="n")

button = customtkinter.CTkButton(app, text="6", command=button_callback)
button.grid(row=3, column=2, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="-", command=button_callback)
button.grid(row=3, column=3, padx=10, pady=(0, 10), sticky="w")


#linha 4
button = customtkinter.CTkButton(app, text="1", command=button_callback)
button.grid(row=4, column=0, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="2", command=button_callback)
button.grid(row=4, column=1, padx=10, pady=(0, 10), sticky="n")

button = customtkinter.CTkButton(app, text="3", command=button_callback)
button.grid(row=4, column=2, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="*", command=button_callback)
button.grid(row=4, column=3, padx=10, pady=(0, 10), sticky="w")

#linha 4
button = customtkinter.CTkButton(app, text="0", command=button_callback)
button.grid(row=5, column=0, padx=10, pady=(0, 10), sticky="ew", columnspan=2)



button = customtkinter.CTkButton(app, text="=", command=button_callback)
button.grid(row=5, column=2, padx=10, pady=(0, 10), sticky="w")

button = customtkinter.CTkButton(app, text="/", command=button_callback)
button.grid(row=5, column=3, padx=10, pady=(0, 10), sticky="w")


app.mainloop()