from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox



def cadastrar_Vaga():
    try:
        idvaga = id_vaga.get()
        nvaga = nome_vaga.get()
        cx = dbapi2.connect('candidatos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into vagas(id, nome_vaga) values (?,?)''',(idvaga, nvaga))
        cx.commit()  
        messagebox.showinfo('Cadastrar Vaga', f'O cadastro da vaga de {nvaga} foi realizado com sucesso!')
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastrar', 'Cadastro da vaga não foi realizado.')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()  


Janela_cadastroVaga = Tk()
Janela_cadastroVaga.title('Criar Nova Vaga')
Janela_cadastroVaga.geometry('400x310')
Janela_cadastroVaga.config(bg = 'black')


label = Label(Janela_cadastroVaga,
              bg = 'black',
              fg = 'white', 
              text='Informe o ID da vaga')
label.pack()
id_vaga = Entry(Janela_cadastroVaga)
id_vaga.pack()


label2 = Label(Janela_cadastroVaga,
               bg = 'black',
               fg = 'white', 
               text='Informe o nome da vaga')
label2.pack()
nome_vaga = Entry(Janela_cadastroVaga)
nome_vaga.pack()

botao = Button(Janela_cadastroVaga,
               bg = 'black',
               fg = 'white', 
               text= 'Criar Nova Vaga',
               command= cadastrar_Vaga)
botao.pack(pady = 10)

botao2 = Button(Janela_cadastroVaga,
                bg = 'black',
                fg = 'white', 
                text = 'Fechar',
                command = Janela_cadastroVaga.destroy)
botao2.pack()

Janela_cadastroVaga.mainloop()