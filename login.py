from tkinter import *
from tkinter import ttk

tk = Tk()
tk.title("Login")
tk.geometry("380x380")
tk.configure(bg="#0d1117")

frame = Frame(tk, bg="#161b22", padx=25, pady=40)
Label(frame, width=18, anchor="w", bg="#161b22", fg="#c9d1d9", text="Usuário:", font=('Lucida font', 12)).pack(ipadx=16)
Entry(frame, width=20, insertbackground="#f0f6fc", font=('Lucida font', 12), bg="#0d1117", fg="#f0f6fc", highlightthickness=1, highlightbackground="#30363d", highlightcolor="#30363d").pack(ipadx=3, ipady=3)
Label(frame, width=18, anchor="w", bg="#161b22", fg="#c9d1d9", text="Senha:", font=('Lucida font', 12)).pack(ipadx=16, pady=(10, 0))
Entry(frame, width=20, insertbackground="#f0f6fc", font=('Lucida font', 12), bg="#0d1117", fg="#f0f6fc", highlightthickness=1, highlightbackground="#30363d", highlightcolor="#30363d").pack(ipadx=3, ipady=3)
btnSubmit = Button(frame, width=18, highlightthickness=0, highlightbackground="#238636", highlightcolor="#238636", bg="#238636", fg="#ffffff", font=('Lucida font', 12), text="Entrar", activebackground="#2ea043", activeforeground="#ffffff")
btnSubmit.pack(pady=(20, 0), ipadx=2)
frame.pack(pady=(68, 62))

tk.mainloop()