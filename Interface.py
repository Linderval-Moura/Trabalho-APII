from tkinter import *


class Painel():
    """Classe que define a interface gráfica da aplicação
    """
    x_pad = 5
    y_pad = 3
    width_entry = 30


    #janela...
    janela1 = Tk()  # Cria janela com as caracteristicas do Tkinter
    janela1.wm_title("Cadastro de Clientes")
    janela1['bg'] = "MIDNIGHTBLUE"
    janela1.attributes("-alpha", 0.9)


    # variáveis 
    txtNome         = StringVar()
    txtSobrenome    = StringVar()
    txtEmail        = StringVar()
    txtCPF          = StringVar()
    txtTelefone     = StringVar()
    txtSenha        = StringVar()


    # objetos que estarão na janela...
    lblnome        = Label(janela1, text="Nome",font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    lblsobrenome   = Label(janela1, text="Sobrenome",font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    lblemail       = Label(janela1, text="Email",font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    lblcpf         = Label(janela1, text="CPF",font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    lblTelefone    = Label(janela1, text="Telefone",font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")
    lblSenha       = Label(janela1, text="Senha ",font=("Century Gothic",9), background="MIDNIGHTBLUE",foreground="white")

    entNome        = Entry(janela1, textvariable=txtNome, width=width_entry)
    entSobrenome   = Entry(janela1, textvariable=txtSobrenome, width=width_entry)
    entEmail       = Entry(janela1, textvariable=txtEmail, width=width_entry)
    entCPF         = Entry(janela1, textvariable=txtCPF, width=width_entry)
    entTelefone    = Entry(janela1, textvariable=txtTelefone, width=width_entry)
    entSenha       = Entry(janela1, textvariable=txtSenha, width=width_entry, show = "•")

    listClientes   = Listbox(janela1, width=100)
    scrollClientes = Scrollbar(janela1)

    btnViewAll     = Button(janela1, text="Listar Todos",bd=5,relief='ridge')
    btnPesquisar   = Button(janela1, text="Pesquisar",bd=5,relief='ridge')
    btnCadastrar   = Button(janela1, text="Cadastrar",bd=5,relief='ridge')
    btnUpdate      = Button(janela1, text="Atualizar Selecionados",bd=5,relief='ridge')
    btnDel         = Button(janela1, text="Deletar Selecionados",bd=5,relief='ridge')
    btnLimpar      = Button(janela1, text="Limpar",bd=5,relief='ridge')
    btnClose       = Button(janela1, text="Fechar",bd=5,relief='ridge')
    btnLogin       = Button(janela1, text="Logar")



    #A grid da janela...
    lblnome.grid(row=0,column=0)
    lblsobrenome.grid(row=1,column=0)
    lblemail.grid(row=2,column=0)
    lblcpf.grid(row=3, column=0)
    lblTelefone.grid(row=4, column=0)
    lblSenha.grid(row=5, column=0)

    entNome.grid(row=0, column=1, padx=50, pady=50)
    entSobrenome.grid(row=1, column=1)
    entEmail.grid(row=2, column=1)
    entCPF.grid(row=3, column=1)
    entTelefone.grid(row=4, column=1)
    entSenha.grid(row=5, column=1)

    listClientes.grid(row=0, column=2, rowspan=10)

    scrollClientes.grid(row=0, column=6, rowspan=10)

    btnViewAll.grid(row=6, column=0, columnspan=2)
    btnPesquisar.grid(row=7, column=0, columnspan=2)
    btnCadastrar.grid(row=8, column=0, columnspan=2)
    btnUpdate.grid(row=9, column=0, columnspan=2)
    btnDel.grid(row=10, column=0, columnspan=2)
    btnLimpar.grid(row=11, column=0, columnspan=2)
    btnClose.grid(row=12, column=0, columnspan=2)
    btnLogin.grid(row=12, column=0, columnspan=2)


    # Scrollbar com a Listbox...
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)


    # SWAG na interface...
    for child in janela1.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')




    def run(self):
        Painel.janela1.mainloop()