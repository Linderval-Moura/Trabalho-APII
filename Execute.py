from Interface import Painel
from tkinter.constants import END
from Interface import *
import Banco as core

app = None

def view_command():
    rows = core.view(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get(),  app.txtTelefone.get())
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)

def search_command():
    app.listClientes.delete(0, END)
    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get(),   app.txtTelefone.get(), app.txtSenha.get())
    for r in rows:
        app.listClientes.insert(END, r)
#insert
def insert_command():
    core.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get(),app.txtTelefone.get(), app.txtSenha.get())
    view_command()

def update_command():
    core.update(selected[0],app.txtNome.get(),app.txtSobrenome.get(),app.txtEmail.get(), app.txtCPF.get(),app.txtTelefone.get(), app.txtSenha.get())
    view_command()

def del_command():
    id = selected[0]
    core.delete(id)
    view_command()

def login_command():
    app.listClientes.delete(0, END)
    rows = core.login(app.txtNome.get(), app.txtSenha.get())
    for r in rows:
        app.listClientes.insert(END)

def limpar():
    app.entNome.delete(0, 'end')
    app.entSobrenome.delete(0, 'end')
    app.entEmail.delete(0, 'end')
    app.entCPF.delete(0, 'end')
    app.entTelefone.delete(0, 'end')
    app.entSenha.delete(0, 'end')
    


def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entSobrenome.delete(0, END)
    app.entSobrenome.insert(END, selected[2])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[3])
    app.entCPF.delete(0, END)
    app.entCPF.insert(END, selected[4])
    app.entTelefone.delete(0, END)
    app.entTelefone.insert(END, selected[5])
    app.entSenha.delete(0, END)
    #app.entSenha.insert(END, selected[6])
    return selected
#btnInserir

if __name__ == "__main__":
    app = Painel()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnPesquisar.configure(command=search_command)
    app.btnCadastrar.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnLimpar.configure(command=limpar)
    app.btnClose.configure(command=app.janela1.destroy)
    app.btnLogin.configure(command=login_command)

    app.run()
