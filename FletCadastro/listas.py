import flet as ft
import classes as c



listaprod = {
    "colunas":{
        "coluna0":ft.DataColumn(ft.Text("nm_prod")),
        "coluna1":ft.DataColumn(ft.Text("vl_prod")),
        "coluna2":ft.DataColumn(ft.Text("desc_prod")),
        "coluna3":ft.DataColumn(ft.Text("marca"))
        },
    "col":{
        0:"nm_prod",
        1:"vl_prod",
        2:"desc_prod",
        3:"marca"
        },
    "inputs":{
        "input0" : c.InputField(label="nome do produto"),
        "input1" : c.InputField(label="valor do produto"),
        "input2" : c.InputField(label="descrição do produto"),
        "input3" : c.InputField(label="marca do produto"),
        }}

listapessoas={        
    "colunas":{
        "coluna0":ft.DataColumn(ft.Text("nm_pessoa")),
        "coluna1":ft.DataColumn(ft.Text("sob_pessoa")),
        },   
        "col":{
        "nm_pessoa":"",
        "sob_pessoa":"",
        },
    "inputs":{
        "input0" : c.InputField(label="nome da pessoa"),
        "input1" : c.InputField(label="sobrenome da pessoa")
        }}

listapesquisas={
    "colunas":{
        "coluna0":ft.DataColumn(ft.Text("nome_conc")),
        "coluna1":ft.DataColumn(ft.Text("vl_conc")),
        "coluna2":ft.DataColumn(ft.Text("marca_conc")),
        "coluna3":ft.DataColumn(ft.Text("dias_conc")),
        "coluna4":ft.DataColumn(ft.Text("obs")),
        },
    "col":{
        "nome_conc":"",
        "vl_conc":"",
        "marca_conc":"",
        "dias_conc":"",
        "obs":"",
        },
    "inputs":{
        "input0" : c.InputField(label="nome do produto concorrente"),
        "input1" : c.InputField(label="valor do produto concorrente"),
        "input2" : c.InputField(label="marca do produto concorrente"),
        "input3" : c.InputField(label="Tempo que compra o produto no concorrente"),
        "input4" : c.InputField(label="observação",multiline=True,min_lines=3,max_lines=6),
        }}  

def conta_lista(x):
    return (len(x["colunas"]))
