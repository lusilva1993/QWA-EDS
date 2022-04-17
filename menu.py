from tkinter import *
import tkinter

def menu():
    import main

menu_principal = Tk()
menu_principal.title('Programa de TRAINEE QWA') 
menu_principal.geometry('600x300') 
menu_principal.resizable(False, False)
menu_principal.config(background = "#708090") 


botao1 =  Button(menu_principal,
                 text = " ENTRAR ",
                 font = ("Arial Black", 15),
                 bg = "#4682B4",
                 fg = 'white',
                 bd = 40,
                 highlightthickness = 0,
                 command = menu,) 

botao1.grid(row = 1, column= 0, padx = (150, 0), pady = (80,0))

menu_principal.mainloop()
