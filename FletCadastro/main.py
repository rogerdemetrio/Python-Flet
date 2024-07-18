import flet as ft 
import modulos

titulo = ft.Text("Central de cadastros",size=24)

#TODO: Criar modulos de cadastro:

produto_tab = True
pessoa_tab = True
pesquisa_tab = True
def main(p: ft.Page):
    p.Title = titulo

    p.navigation_bar = ft.CupertinoNavigationBar(
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
    def pag_index(n):
        print(n)
        if n == 0:
            modulos.cadastroProduto()
        if n == 1:
            modulos.cadastroPessoa()
        if n == 2:
            modulos.cadastroPesquisa()
        else:
            modulos.cadastroProduto()
        
    p.update()
ft.app(target=main)

#TODO: Criar uma tela principal que consiga encaixar outros modulos de cadastro e visualização de dados

#TODO: Conectar todos os modulos ao main:
    # Modulo de produto
    # Modulo de pessoa
    # Modulo de pesquisa de mercado
