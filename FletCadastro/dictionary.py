import flet as ft
import classes as c
import models as md

num_hint = "Até 4 casas decimais (Ex.: 9.9999)"

# Variavel que comporta o dicionario dos itens que formam a tela principal 
# e auxiliam no banco de dados
lista = {
    0 : {
        "tit":ft.Text("Cadastro de Produtos",size=20,color=ft.colors.WHITE),
        "dest":ft.NavigationBarDestination(icon=ft.icons.FASTFOOD_OUTLINED,selected_icon=ft.icons.FASTFOOD, label="Produtos"),
        "col":{
            0:"nm_prod",
            1:"vl_prod",
            2:"desc_prod",
            3:"marca"
            },
        "inputs":{
            0 : c.InputField(label="Nome do produto"),
            1 : c.InputField(label="Valor do produto",hint_text=num_hint,
                             input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*(\.\d{0,4})?$", replacement_string="")),
            2 : c.InputField(label="Descrição do produto"),
            3 : c.InputField(label="marca do produto"),
            },
        "tb":md.Produto
        },

    1 : {  
        "tit":ft.Text("Cadastro de Pessoas",size=20,color=ft.colors.WHITE),
        "dest":ft.NavigationBarDestination(icon=ft.icons.PEOPLE_OUTLINED,selected_icon=ft.icons.PEOPLE, label="Pessoas"),
        "col":{
            0:"nm_pessoa",
            1:"sob_pessoa",
            },
        "inputs":{
            0 : c.InputField(label="nome da pessoa"),
            1 : c.InputField(label="sobrenome da pessoa")
            },
        "tb":md.Pessoa
        },

    2 : {
        "tit":ft.Text("Cadastro de Pesquisa",size=20,color=ft.colors.WHITE),
        "dest":ft.NavigationBarDestination(icon=ft.icons.BOOK_OUTLINED,selected_icon=ft.icons.BOOK, label="Pesquisa"),
        "col":{
            0:"nome_conc",
            1:"vl_conc",
            2:"marca_conc",
            3:"dias_conc",
            4:"obs",
            },
        "inputs":{
            0 : c.InputField(label="nome do produto concorrente"),
            1 : c.InputField(label="valor do produto concorrente",hint_text=num_hint,
                             input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*(\.\d{0,4})?$", replacement_string="")),
            2 : c.InputField(label="marca do produto concorrente"),
            3 : c.InputField(label="Tempo que compra o produto no concorrente"),
            4 : c.InputField(label="observação",multiline=True,min_lines=3,max_lines=6),
            },
        "tb":md.Pesquisa,
        } 
    } 

# Conta a quantidade de colunas de cada dicionario
def conta_lista(x):
    return (len(x["col"]))
