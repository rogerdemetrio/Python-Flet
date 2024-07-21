import flet as ft
import classes as c

def pro(x):
    mid = ft.Column(col={"md":6}, controls=[ listaprod["labels"][f"label{x}"], listaprod["inputs"][f"input{x}"] ])
    return mid
def pes(x):
    mid = ft.Column(col={"md":6}, controls=[ listapessoas["labels"][f"label{x}"], listapessoas["inputs"][f"input{x}"] ])
    return mid
def peq(x):
    mid = ft.Column(col={"md":6}, controls=[ listapesquisas["labels"][f"label{x}"], listapesquisas["inputs"][f"input{x}"] ])
    return mid

listaprod = {
    "labels":{
        "label0":ft.Container(ft.Text("Nome do produto:",size=12)),
        "label1":ft.Container(ft.Text("Valor do produto:",size=12)),
        "label2":ft.Container(ft.Text("Descrição do produto:",size=12)),
        "label3":ft.Container(ft.Text("Marca do produto:",size=12))
        },
    "inputs":{
        "input0" : c.InputField(label="Digite o nome do produto"),
        "input1" : c.InputField(label="Digite o valor do produto"),
        "input2" : c.InputField(label="Digite a descrição do produto"),
        "input3" : c.InputField(label="Digite a marca do produto"),
        }}

listapessoas={        
    "labels":{
        "label0":ft.Container(ft.Text("Nome da pessoa:",size=12)),
        "label1":ft.Container(ft.Text("Sobrenome da pessoa:",size=12))
        },
    "inputs":{
        "input0" : c.InputField(label="Digite o nome da pessoa"),
        "input1" : c.InputField(label="Digite o sobrenome da pessoa")
        }}

listapesquisas={
    "labels":{
        "label0":ft.Container(ft.Text("Nome do produto concorrente:",size=12)),
        "label1":ft.Container(ft.Text("Valor do produto concorrente:",size=12)),
        "label2":ft.Container(ft.Text("Marca do produto concorrente:",size=12)),
        "label3":ft.Container(ft.Text("A quanto tempo compra o produto concorrente:",size=12)),
        "label4":ft.Container(ft.Text("Observação:",size=12))
        },
    "inputs":{
        "input0" : c.InputField(label="Digite o nome do produto concorrente"),
        "input1" : c.InputField(label="Digite o valor do produto concorrente"),
        "input2" : c.InputField(label="Digite a marca do produto concorrente"),
        "input3" : c.InputField(label="Digite o tempo em meses"),
        "input4" : c.InputField(label="Digite a observação",multiline=True,min_lines=3,max_lines=6),
        }}  
