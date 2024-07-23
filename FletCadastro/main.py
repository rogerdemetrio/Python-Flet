import flet as ft 
import classes as c
import listas as l

def main(page: ft.Page):
    
    header = ft.Column([ft.Container(content=ft.Text("DemetrioVendas",size=32),alignment=ft.alignment.center), ft.Divider()])
    
    # Padrões da pagina alterados para trazer em forma de aplicativo para smartphone "simulado"
    page.window.center()
    page.bgcolor = ft.colors.GREY_900
    page.padding = 20
    page.window.height = 920
    page.window.width = 480
    page.window.maximizable = False
    page.window.resizable = False
    page.window.shadow = True
    page.title = "Central de cadastros"

    def pag_index(e): 
        if e == 0:
            page.controls.clear()
            cadastroProduto()
        if e == 1:
            page.controls.clear()
            cadastroPessoa()
        if e == 2:
            page.controls.clear()
            cadastroPesquisa()
    
    def btn_add(e):
        if pagina == 0:
            new_row = ft.DataRow(cells=[ ft.DataCell(ft.Text(inputText.value)) for inputText in body.controls ])
            my_table.rows.append(new_row)
            my_table.update()

        if pagina == 1:
            new_row = ft.DataRow(cells=[ ft.DataCell(ft.Text(inputText.value)) for inputText in body.controls ])
            my_table.rows.append(new_row)
            my_table.update()
                
        if pagina == 2:
            new_row = ft.DataRow(cells=[ ft.DataCell(ft.Text(inputText.value)) for inputText in body.controls ])
            my_table.rows.append(new_row)
            my_table.update()

    page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.BLACK45,
            inactive_color=ft.colors.WHITE70,
            active_color=ft.colors.AMBER_700,
            icon_size=36,
            on_change=lambda e: pag_index(e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.FASTFOOD_OUTLINED,selected_icon=ft.icons.FASTFOOD, label="Produtos"),
                ft.NavigationBarDestination(icon=ft.icons.PEOPLE_OUTLINED,selected_icon=ft.icons.PEOPLE, label="Pessoas"),
                ft.NavigationBarDestination(icon=ft.icons.BOOK_OUTLINED,selected_icon=ft.icons.BOOK, label="Pesquisa"),
            ],
        )
    
    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500)

    def cadastroProduto():
        global pagina,body,my_table
        pagina = 0
        titulo = ft.Text("Cadastro de produtos",size=20)
        body = ft.Column(col={"md":6},controls=[l.listaprod["inputs"][f"input{x}"] for x in range(4)])
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
        my_table = ft.DataTable(columns=[l.listaprod["colunas"][f"coluna{x}"] for x in range(4)],rows=[],)
        page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )

    def cadastroPessoa():
        global pagina,body,my_table
        pagina = 1
        titulo = ft.Container(ft.Text("Cadastro de pessoa",size=20))
        body = ft.Column(col={"md":6},controls=[l.listapessoas["inputs"][f"input{x}"] for x in range(2)])
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
        my_table = ft.DataTable(columns=[l.listapessoas["colunas"][f"coluna{x}"] for x in range(2)],rows=[],)
        page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )
    def cadastroPesquisa():
        global pagina,body,my_table
        pagina = 2
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=20))
        body = ft.Column(col={"md":6},controls=[l.listapesquisas["inputs"][f"input{x}"] for x in range(5)])
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
        my_table = ft.DataTable(columns=[l.listapesquisas["colunas"][f"coluna{x}"] for x in range(5)],rows=[],)
        page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )

    cadastroProduto()
    page.update()

ft.app(target=main)
