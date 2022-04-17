from tkinter import *
from sqlite3 import dbapi2
from tkinter import ttk



def lerListaCandidaturas():
    
    try:
        cx = dbapi2.connect('candidatos.db')
        cursor = cx.cursor() 
        dados_Candidatos = cursor.execute('select * from candidaturas;')
        rows =  dados_Candidatos.fetchall()
        for row in rows:
            tree.insert('', END, values = row)
    finally:
        cursor.close()
        cx.close()

janela_listarCandidaturas = Tk()
janela_listarCandidaturas.title('Lista das Candidaturas realizadas - QWA')
janela_listarCandidaturas.config(bg = 'LightSlateGray', bd = 10)

tree = ttk.Treeview(janela_listarCandidaturas,
                    column=('c1', 'c2', 'c3', 'c4','c5'),
                    show ='headings')  
tree.column('#1')
tree.heading('#1',
             text = 'Código da Vaga')
tree.column('#2')
tree.heading('#2',
             text = 'CPF do Candidato')
tree.column('#3')
tree.heading('#3',
             text = 'Código da Vaga')


tree.pack()

button = Button(janela_listarCandidaturas, text ='Ver lista de Candidaturas',
                bg = 'white',
                fg = 'black',
                bd = 0,
                command = lerListaCandidaturas)
button.pack(pady = 10)

button1 = Button(janela_listarCandidaturas, text='Fechar',
                 bg = 'white',
                 fg = 'black',
                 bd = 0,
                 command= janela_listarCandidaturas.destroy).pack()

janela_listarCandidaturas.mainloop()