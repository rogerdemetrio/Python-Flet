import flet as ft 

titulo = ft.Text("Central de cadastros",size=24)
labelProduto = ft.Text("Cadastro de produtos",size=12)

def main(p: ft.Page):
    p.Title = "Cadastro de produtos"
    p.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.BLACK45,
            inactive_color=ft.colors.GREY,
            active_color=ft.colors.GREEN_ACCENT_700,
            on_change=lambda e: print("Selected tab:", e.control.selected_index),
            destinations=[
                ft.NavigationBarDestination(icon=ft.icons.FASTFOOD_OUTLINED, label="Produtos"),
                ft.NavigationBarDestination(icon=ft.icons.PEOPLE, label="Pessoas"),
                ft.NavigationBarDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Explore",
                ),
            ]
        )    
    


    p.update()
ft.app(target=main)

#TODO: Criar um arquivo principal que consiga encaixar outros modulos de cadastro e visualização de dados
#TODO: Criar modulos de cadastro{
    # Modulo de produto
    # Modulo de pessoa
    # Modulo de pesquisa de mercado
    #}
#TODO: Conectar todos os modulos ao main{
    # Modulo de produto
    # Modulo de pessoa
    # Modulo de pesquisa de mercado
    #}