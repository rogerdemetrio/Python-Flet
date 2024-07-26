import flet as ft
import classes as c

# Dicionario dos itens que formam a tela principal e auxiliam no banco de dados
lista = {
    0 : {
        "tit":ft.Text("Cadastro de Produtos",size=20),
        "col":{
            0:"nm_prod",
            1:"vl_prod",
            2:"desc_prod",
            3:"marca"
            },
        "inputs":{
            0 : c.InputField(label="Nome do produto"),
            1 : c.InputField(label="Valor do produto"),
            2 : c.InputField(label="Descrição do produto"),
            3 : c.InputField(label="marca do produto"),
            }
        },
    1 : {  
        "tit":ft.Text("Cadastro de Pessoas",size=20),
        "col":{
            0:"nm_pessoa",
            1:"sob_pessoa",
            },
        "inputs":{
            0 : c.InputField(label="nome da pessoa"),
            1 : c.InputField(label="sobrenome da pessoa")
            }
        },
    2 : {
        "tit":ft.Text("Cadastro de Pesquisa",size=20),
        "col":{
            0:"nome_conc",
            1:"vl_conc",
            2:"marca_conc",
            3:"dias_conc",
            4:"obs",
            },
        "inputs":{
            0 : c.InputField(label="nome do produto concorrente"),
            1 : c.InputField(label="valor do produto concorrente"),
            2 : c.InputField(label="marca do produto concorrente"),
            3 : c.InputField(label="Tempo que compra o produto no concorrente"),
            4 : c.InputField(label="observação",multiline=True,min_lines=3,max_lines=6),
            }
        } 
    } 

# Conta a quantidade de colunas de cada dicionario
def conta_lista(x):
    return (len(x["col"]))
