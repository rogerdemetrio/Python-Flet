import flet as ft 

#TODO: Criar classe de modulos de cadastro
def main(page: ft.Page):
    page.Title = "Central de cadastros"

#TODO: Tela principal que consiga encaixar outros modulos de cadastro e visualização de dados
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
        titulo = ft.Container(ft.Text("Cadastro de produtos",size=24))
        label1 = ft.Container(ft.Text("Nome do produto:",size=12))
        input1 = ft.TextField(label="Digite o nome do produto")
        label2 = ft.Container(ft.Text("Valor do produto:",size=12))
        input2 = ft.TextField(label="Digite o valor do produto")
        label3 = ft.Container(ft.Text("Valor do produto:",size=12))
        input3 = ft.TextField(label="Digite o valor do produto")
        label4 = ft.Container(ft.Text("Valor do produto:",size=12))
        input4 = ft.TextField(label="Digite o valor do produto")
        btn = ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.LIGHT_GREEN_900)
        corpo = ft.Column(controls=[
                            titulo,
                            ft.ResponsiveRow([ft.Column(col={"md": 6}, controls=[label1,input1]),ft.Column(col={"md": 6}, controls=[label2,input2])]),
                            ft.ResponsiveRow([ft.Column(col={"md": 6}, controls=[label3,input3]),ft.Column(col={"md": 6}, controls=[label4,input4])]),
                            ft.Column(controls=[btn],alignment=ft.CrossAxisAlignment.END),
                            ])
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
        
    cadastroProduto()

    page.update()
ft.app(target=main)


