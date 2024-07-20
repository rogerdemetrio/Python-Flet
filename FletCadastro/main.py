import flet as ft 
import classes as c
import listas as l

#TODO: Criar classe de modulos de cadastro
def main(page: ft.Page):
    page.Title = "Central de cadastros"

# Main
    
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

    header = ft.Column([ft.Container(content=ft.Text("DemetrioVendas",size=36),alignment=ft.alignment.center), ft.Divider()])
    footer = ft.Column([ft.Divider(),ft.Text("Footer")])

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
    
    def btn_add(e):
        print("Clicou")
        #page.add()

    def cadastroProduto():
        i = 4
        titulo = ft.Text("Cadastro de produtos",size=24)
        btn = ft.Container(content = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500), alignment=ft.alignment.center_right)
        mid_sec = ft.ResponsiveRow(controls=[
                        ft.Column(col={"md": 6}, controls = l.pro(0)),
                        ft.Column(col={"md": 6}, controls = l.pro(1)),
                        ft.Column(col={"md": 6}, controls = l.pro(2)),
                        ft.Column(col={"md": 6}, controls = l.pro(3)),
                    ])
            
        mid = ft.Column([titulo,mid_sec,btn])
        corpo = c.CorpoContainer(content = ft.Column(controls=[header, mid, footer]))
        page.add(corpo)

    def cadastroPessoa():
        i = 2
        titulo = ft.Container(ft.Text("Cadastro de pessoa",size=24))
        btn = ft.Container(content = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500), alignment=ft.alignment.center_right)
        mid_sec = ft.ResponsiveRow(controls=[
                        ft.Column(col={"md": 6}, controls = l.pes(0)),
                        ft.Column(col={"md": 6}, controls = l.pes(1)),
                    ])
            
        mid = ft.Column([titulo,mid_sec,btn])
        corpo = c.CorpoContainer(content = ft.Column(controls=[header, mid, footer]))
        page.add(corpo)

    def cadastroPesquisa():
        i = 5
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=24))
        btn = ft.Container(content = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500), alignment=ft.alignment.center_right)
        mid_sec = ft.ResponsiveRow(controls=[
                        ft.Column(col={"md": 6}, controls = l.peq(0)),
                        ft.Column(col={"md": 6}, controls = l.peq(1)),
                        ft.Column(col={"md": 6}, controls = l.peq(2)),
                        ft.Column(col={"md": 6}, controls = l.peq(3)),
                        ft.Column(col={"md": 12}, controls = l.peq(4)),
                    ])
        mid = ft.Column([titulo,mid_sec,btn])
        corpo = c.CorpoContainer(content = ft.Column(controls=[header, mid, footer]))
        page.add(corpo)
        

    cadastroProduto()

    page.update()
ft.app(target=main)
