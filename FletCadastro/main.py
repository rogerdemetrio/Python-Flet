import flet as ft 
import classes as c
import listas as l

def main(page: ft.Page):
# Main
    #page.window.center()
    header = ft.Column([ft.Container(content=ft.Text("DemetrioVendas",size=32),alignment=ft.alignment.center), ft.Divider()])
    page.bgcolor = ft.colors.GREY_900
    page.padding = 20
    page.window.height = 920
    page.window.width = 480
    page.window.maximizable = False
    page.window.resizable = False
    page.window.shadow = True

    lv = ft.ListView(auto_scroll=True)

    page.Title = "Central de cadastros"
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
            page.add(ft.Row(controls = [ft.Column(controls = [ ft.Text("teste") ]),ft.Column(controls = [ ft.Text("teste") ]),ft.Column(controls = [ ft.Text("teste") ]) ]))
        if pagina == 1:
            page.add(ft.Row(controls = [ft.Column(controls = [  ]) ]))
        if pagina == 2:
            page.add(ft.Row(controls = [ft.Column(controls = [  ]) ]))
    

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
        global pagina,j
        pagina = 0
        j = 4
        titulo = ft.Text("Cadastro de produtos",size=20)
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]))
        for i in range(0,j):
            mid_sec = l.pro(i)
            page.add(mid_sec)
        page.add(ft.Divider(color=ft.colors.WHITE38))
        page.add(lv)

    def cadastroPessoa():
        global pagina,j
        pagina = 1
        j = 2
        titulo = ft.Container(ft.Text("Cadastro de pessoa",size=20))
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]))
        for i in range(0,j):
            mid_sec = l.pes(i)
            page.add(mid_sec)
        page.add(ft.Divider(color=ft.colors.WHITE38))

    def cadastroPesquisa():
        global pagina,j
        pagina = 2
        j = 5
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=20))
        page.add(ft.Column(controls=[header]),ft.Column(controls=[titulo]))
        for i in range(0,j):
            mid_sec = l.peq(i)
            page.add(mid_sec)
        page.add(ft.Divider(color=ft.colors.WHITE38))

    cadastroProduto()
    page.update()

ft.app(target=main)
