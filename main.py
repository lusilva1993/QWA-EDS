from tkinter import *
from sqlite3 import *



def cadPessoa():
    import cadastroCandidato
def cadVaga():    
    import cadastroVaga
def listarCandits():    
    import listaCandidaturas


menuprincipal = Tk()
menuprincipal.title('QWA Solutions - TRAINEE 2022')
menuprincipal.geometry('500x280')
menuprincipal.resizable(False, False)
menuprincipal.config(bg = 'black')

botao = Button(menuprincipal,
               text='SISTEMA DE CADASTRO',
               bg = 'black',
               fg = 'white',
               borderwidth = 1,
               width='20',
               height='2',
               bd = 0,
               pady=1)
botao.grid(row=0, column=0, pady = 10, padx = 10)

botao1 = Button(menuprincipal,
               text='Cadastrar Candidato',
               bg = 'black',
               fg = 'white',
               borderwidth = 1,
               width='20',
               height='2',
               command=cadPessoa,
               pady=1)
botao1.grid(row=1, column=0, pady = 10, padx = 10)

botao2 = Button(menuprincipal, text='Cadastrar Vaga',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20', 
                height='2',
                command=cadVaga)
botao2.grid(row=1, column=1, pady=10, padx= 10)

botao3 = Button(menuprincipal, text='Lista de Candidaturas',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                width='20', 
                height='2',
                command=listarCandits)
botao3.grid(row=1, column=2, pady=10, padx= 10)

botao_fechar = Button(menuprincipal, text='Fechar',
                bg = 'black',
                fg = 'white',
                borderwidth = 1,
                      width='20',
                      height='2', 
                      command= menuprincipal.destroy)
botao_fechar.grid(row=2, column= 1, pady=10)

menuprincipal.mainloop()


