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
        "tb":md.Produto,
        "col":{
            0:["nm_prod","Nm. Prod."],
            1:["vl_prod","Vl. Prod."],
            2:["desc_prod","Desc. Prod."],
            3:["marca","Marca"]
            },
        "inputs":{
            0 : c.InputField(label="Nome do produto"),
            1 : c.InputField(label="Valor do produto",hint_text=num_hint,
                             input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*(\.\d{0,4})?$", replacement_string="")),
            2 : c.InputField(label="Descrição do produto"),
            3 : c.InputField(label="marca do produto"),
            },
        "vis":True,
        "table":"tbproduto"
        },

    1 : {  
        "tit":ft.Text("Cadastro de Pessoas",size=20,color=ft.colors.WHITE),
        "dest":ft.NavigationBarDestination(icon=ft.icons.PEOPLE_OUTLINED,selected_icon=ft.icons.PEOPLE, label="Pessoas"),
        "tb":md.Pessoa,
        "col":{
            0:["nm_pessoa","Nome"],
            1:["sob_pessoa","Sobrenome"],
            },
        "inputs":{
            0 : c.InputField(label="nome da pessoa"),
            1 : c.InputField(label="sobrenome da pessoa")
            },
        "vis":True,
        "table":"tbpessoa"
        },

    2 : {
        "tit":ft.Text("Cadastro de Pesquisa",size=20,color=ft.colors.WHITE),
        "dest":ft.NavigationBarDestination(icon=ft.icons.BOOK_OUTLINED,selected_icon=ft.icons.BOOK, label="Pesquisa"),
        "tb":md.Pesquisa,
        "col":{
            0:["nome_conc","Prod. Concorrente"],
            1:["vl_conc","Vl. Prod."],
            2:["marca_conc","Marca"],
            3:["dias_conc","Tempo"],
            4:["obs","Observação"],
            },
        "inputs":{
            0 : c.InputField(label="nome do produto concorrente"),
            1 : c.InputField(label="valor do produto concorrente",hint_text=num_hint,
                             input_filter=ft.InputFilter(allow=True, regex_string=r"^\d*(\.\d{0,4})?$", replacement_string="")),
            2 : c.InputField(label="marca do produto concorrente"),
            3 : c.InputField(label="Tempo que compra o produto no concorrente"),
            4 : c.InputField(label="observação",multiline=True,min_lines=3,max_lines=3),
            },
        "vis":True,
        "table":"tbpesquisa"
        },
    3 : {
        "tit":ft.Text("Teste de Texto usando dicionario",size=20,color=ft.colors.WHITE),
        "dest":ft.NavigationBarDestination(icon=ft.icons.STICKY_NOTE_2_OUTLINED,selected_icon=ft.icons.STICKY_NOTE_2, label="Texto"),
        "tb":"",
        "table":"",
        "col":{
             0:"",
            },
        "inputs":{
            0 : ft.Text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \nExcepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                        ,color=ft.colors.BLACK87)
            },
        "vis":False,
        },
    } 

# Conta a quantidade de colunas de cada dicionario
def conta_lista(x):
    return (len(x["col"]))
