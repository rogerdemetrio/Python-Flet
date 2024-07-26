import flet as ft 
import listas as l
import models as md

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
    def btn_add(ev):
        i = [inputText.value for inputText in body.controls]
        tabela = {}
        for x in range(l.conta_lista(l.lista[pagina])):
            tabela.update({str(l.lista[pagina]["col"][x]):str(i[x])})
        if pagina == 0:
            tb = md.Produto(**tabela)
        if pagina == 1:
            tb = md.Pessoa(**tabela)
        if pagina == 2:
            tb = md.Pesquisa(**tabela)
        md.session.add(tb)
        md.session.commit()

    page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add)
    page.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT

    def pag_index(ev):
        global body,pagina
        pagina = ev
        page.controls.clear() 
        body = ft.Column(controls=[l.lista[ev]["inputs"][x] for x in range(l.conta_lista(l.lista[ev]))])
        page.add(ft.Column(controls=[header]),ft.Column(controls=[l.lista[ev]["tit"]]),
                 ft.Column(controls=[body]),ft.Column(controls=[ft.Divider(color=ft.colors.WHITE38)]))
 
    pag_index(0)
    page.update()

ft.app(target=main)
