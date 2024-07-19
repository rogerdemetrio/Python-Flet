import flet as ft 

titulo = ft.Text("Central de cadastros",size=24)
#TODO: Remover os modulos do arquivo principal
#TODO: Criar classe de modulos de cadastro
def main(page: ft.Page):
    page.Title = titulo


    def pag_index(e):
        if e == 0:
            cadastroProduto()
        if e == 1:
            cadastroPessoa()

        if e == 2:
            cadastroPesquisa()

    page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.BLACK45,
            inactive_color=ft.colors.WHITE70,
            active_color=ft.colors.YELLOW_400,
            icon_size=36,
            on_change=lambda e: pag_index(e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.FASTFOOD_OUTLINED,selected_icon=ft.icons.FASTFOOD, label="Produtos"),
                ft.NavigationBarDestination(icon=ft.icons.PEOPLE_OUTLINED,selected_icon=ft.icons.PEOPLE, label="Pessoas"),
                ft.NavigationBarDestination(icon=ft.icons.BOOK_OUTLINED,selected_icon=ft.icons.BOOK, label="Pesquisa"),
            ],
        )
    
    def cadastroProduto():
        page.controls.clear()
        titulo = ft.Container(ft.Text("Cadastro de produtos",size=24))
        lab_pro = ft.Container(ft.Text("Nome do produto:",size=12))
        corpo = ft.Column([titulo,lab_pro])
        page.add(corpo)

    def cadastroPessoa():
        page.controls.clear()           
        titulo = ft.Container(ft.Text("Cadastro de pessoa",size=24))
        lab_pro = ft.Container(ft.Text("Nome da pessoa:",size=12))
        corpo = ft.Column([titulo,lab_pro])
        page.add(corpo)

    def cadastroPesquisa():
        page.controls.clear()           
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=24))
        lab_pro = ft.Container(ft.Text("Nome do produto:",size=12))
        corpo = ft.Column([titulo,lab_pro])
        page.add(corpo)
            
    cadastroProduto()

    page.update()
ft.app(target=main)

#DONE: Criar uma tela principal que consiga encaixar outros modulos de cadastro e visualização de dados

#TODO: Conectar todos os modulos ao main:
    # Modulo de produto
    # Modulo de pessoa
    # Modulo de pesquisa de mercado
