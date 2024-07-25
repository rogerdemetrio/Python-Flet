import flet as ft 
import listas as l
import models as md

#TODO -> Remover repetições
#TODO -> Criar classes com a bagunça abaixo
#TODO -> Mostrar informação do banco na tela

def main(page: ft.Page):
    
    header = ft.Column([ft.Container(content=ft.Text("DemetrioVendas",size=32),alignment=ft.alignment.center), ft.Divider()])
    
    # Padrões da pagina alterados para trazer em forma de aplicativo para smartphone "simulado"
    page.title = "Central de cadastros"
    page.theme = ft.Theme(color_scheme_seed="green")
    page.window.center()
    page.bgcolor = ft.colors.GREY_700
    page.padding = 20
    page.window.height = 920
    page.window.width = 480
    page.window.maximizable = False
    page.window.resizable = False
    page.window.shadow = True

    page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.BLACK45,
            inactive_color=ft.colors.WHITE70,
            #active_color=ft.colors.GREEN_900,
            icon_size=36,
            
            on_change=lambda e: pag_index(e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.FASTFOOD_OUTLINED,selected_icon=ft.icons.FASTFOOD, label="Produtos"),
                ft.NavigationBarDestination(icon=ft.icons.PEOPLE_OUTLINED,selected_icon=ft.icons.PEOPLE, label="Pessoas"),
                ft.NavigationBarDestination(icon=ft.icons.BOOK_OUTLINED,selected_icon=ft.icons.BOOK, label="Pesquisa"),
            ],
        )
    
    
    def pag_index(ev): 
        if ev == 0:
            page.controls.clear()
            cadastroProduto()

        if ev == 1:
            page.controls.clear()
            cadastroPessoa()

        if ev == 2:
            page.controls.clear()
            cadastroPesquisa()

    
    def btn_add(ev):
        i = [inputText.value for inputText in body.controls]
        tabela = {}
        if pagina == 0:
            for x in range(l.conta_lista(l.listaprod)):
                tabela.update({str(l.listaprod["col"][x]):str(i[x])})
            tb = md.Produto(**tabela)

        if pagina == 1:
            for x in range(l.conta_lista(l.listapessoas)):
                tabela.update({str(l.listapessoas["col"][x]):str(i[x])})
            tb = md.Pessoa(**tabela)
                
        if pagina == 2:
            for x in range(l.conta_lista(l.listapesquisas)):
                tabela.update({str(l.listapesquisas["col"][x]):str(i[x])})
            tb = md.Pesquisa(**tabela)
        md.session.add(tb)
        md.session.commit()

        #new_row = ft.DataRow(cells=[ ft.DataCell(ft.Text(inputText.value)) for inputText in body.controls ])
        #my_table.rows.append(new_row)
        #my_table.update()
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT



    def cadastroProduto():
        global pagina,body,my_table
        pagina = 0
        titulo = ft.Text("Cadastro de Produtos",size=20)
        body = ft.Column(controls=[l.listaprod["inputs"][f"input{x}"] for x in range(l.conta_lista(l.listaprod))])
        my_table = ft.DataTable(columns=[l.listaprod["colunas"][f"coluna{x}"] for x in range(l.conta_lista(l.listaprod))],rows=[],)
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
        page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )
        

    def cadastroPessoa():
        global pagina,body,my_table
        pagina = 1
        titulo = ft.Container(ft.Text("Cadastro de Pessoa",size=20))
        body = ft.Column(controls=[l.listapessoas["inputs"][f"input{x}"] for x in range(l.conta_lista(l.listapessoas))])
        my_table = ft.DataTable(columns=[l.listapessoas["colunas"][f"coluna{x}"] for x in range(l.conta_lista(l.listapessoas))],rows=[],)
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
        page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )

    def cadastroPesquisa():
        global pagina,body,my_table
        pagina = 2
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=20))
        body = ft.Column(controls=[l.listapesquisas["inputs"][f"input{x}"] for x in range(l.conta_lista(l.listapesquisas))])
        my_table = ft.DataTable(columns=[l.listapesquisas["colunas"][f"coluna{x}"] for x in range(l.conta_lista(l.listapesquisas))],rows=[],)
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
        page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )

    cadastroProduto()
    page.update()

ft.app(target=main)
