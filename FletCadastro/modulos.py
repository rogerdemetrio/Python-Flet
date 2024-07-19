import flet as ft 

page = ft.Page

class Modulos:
#TODO:[prioridade] Modulo de produto   
    def cadastroProduto():
        titulo = ft.Container(ft.Text("Cadastro de produtos",size=24))
        label1 = ft.Container(ft.Text("Nome do produto:",size=12))
        input1 = ft.TextField(label="Digite o nome do produto")
        label2 = ft.Container(ft.Text("Valor do produto:",size=12))
        input2 = ft.TextField(label="Digite o valor do produto")
        #btn_send = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.LIME_300)
        corpo = ft.Column([titulo,
                           ft.Row([ft.Column([label1,input1]),ft.Column([label2,input2])])],

                           )
        page.add(corpo)

    def cadastroPessoa():          
        titulo = ft.Container(ft.Text("Cadastro de pessoa",size=24))
        label1 = ft.Container(ft.Text("Nome da pessoa:",size=12))
        input1 = ft.TextField(label="Digite o nome da pessoa")
        #btn_send = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.LIME_300)
        corpo = ft.Column([titulo,label1,ft.Row([input1])])
        page.add(corpo)

    def cadastroPesquisa():         
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=24))
        label1 = ft.Container(ft.Text("Nome do produto:",size=12))
        input1 = ft.TextField(label="Digite o nome do produto")
        #btn_send = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=fab_pressed, bgcolor=ft.colors.LIME_300)
        corpo = ft.Column([titulo,label1,ft.Row([input1])])
        page.add(corpo)
