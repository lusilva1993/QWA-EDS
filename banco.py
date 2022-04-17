import sqlite3
from sqlite3 import dbapi2

def criandoTabelas():
            
    tb_vagas = '''
        CREATE TABLE IF NOT EXISTS vagas(
            id INTEGER PRIMARY KEY,
            nome_vaga VARCHAR(50) NOT NULL
            );''' 
            
    tb_candidato = '''
        CREATE TABLE IF NOT EXISTS candidato(
            id INTEGER PRIMARY KEY, 
            nome VARCHAR(15) not null,
            sobrenome VARCHAR(50) not null,
            nascimento VARCHAR(5) not null,
            );''' 
                    
    tb_candidaturas = '''
        CREATE TABLE IF NOT EXISTS candidaturas(
            id_vaga INTEGER NOT NULL PRIMARY KEY REFERENCES vagas(id),
            id INTEGER NOT NULL REFERENCES candidato(id),
            nome VARCHAR(15) not null candidato(nome),    
            
        );'''    

criandoTabelas()










