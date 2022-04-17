from tkinter import *
from sqlite3 import dbapi2
import sqlite3
from tkinter import messagebox


def executar():
    try:
        
        cpfcand = cpf_cand.get()
        ncandidato = nome_cand.get()
        scandidato = sobrenome_cand.get()
        dnasc = data_nascimento.get()
        cx = dbapi2.connect('candidatos.db')
        cursor = cx.cursor() 
        cursor.execute('''insert into candidato (id, nome, sobrenome, nascimento, ) values (?,?,?,?)''', (cpfcand, ncandidato, scandidato, dnasc))
        cx.commit()  
        messagebox.showinfo('Cadastro', f'O cadastro do(a) candidato(a) {ncandidato} foi realizado com sucesso!')
        
    except sqlite3.DatabaseError as erro:        
        messagebox.showinfo('Cadastro', 'Cadastro do(a) candidato(a) não foi realizado.')
        cx.rollback()
    finally:
        cursor.close()
        cx.close()     
  
janela_adicionar = Tk()
janela_adicionar.title('Cadastro de Candidatos - QWA')
janela_adicionar.geometry('250x380')
janela_adicionar.config(bg = 'black')



label1 = Label(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text= 'Informe o CPF:')
label1.grid(row= 0, column=0) 
cpf_cand = Entry(janela_adicionar)
cpf_cand.grid(row= 1, column=0, pady = 2)  



label2 = Label(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text= 'Informe o nome do candidato:')
label2.grid(row= 2, column=0) 
nome_cand = Entry(janela_adicionar)
nome_cand.grid(row= 3, column=0, pady = 2)



label3 = Label(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text= 'Informe o sobrenome:')
label3.grid(row= 4, column=0) 
sobrenome_cand = Entry(janela_adicionar)
sobrenome_cand.grid(row= 5, column=0, pady = 2)



label4 = Label(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text= 'Informe a data de nascimento:\n(DD/MM/AAAA)')
label4.grid(row= 6, column=0)
data_nascimento = Entry(janela_adicionar)
data_nascimento.grid(row= 7, column=0, pady = 2)  
  
  

botao = Button(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text= 'Adicionar candidato', command= executar)
botao.grid(row= 8, column=0, pady = 10)



botao2 = Button(janela_adicionar,
                bg = 'black',
                fg = 'white', 
                text = 'Fechar',
                command = janela_adicionar.destroy)
botao2.grid(row=9, column=0)



janela_adicionar.mainloop()