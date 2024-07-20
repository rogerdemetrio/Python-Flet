import flet as ft 
import classes

#TODO: Criar lista para comportar labels e inputs
#TODO: Criar classe de modulos de cadastro
def main(page: ft.Page):
    page.Title = "Central de cadastros"

    c = classes

    listaprod = {
        "labels":{
            "label0":ft.Container(ft.Text("Nome do produto:",size=12)),
            "label1":ft.Container(ft.Text("Valor do produto:",size=12)),
            "label2":ft.Container(ft.Text("Descrição do produto:",size=12)),
            "label3":ft.Container(ft.Text("Marca do produto:",size=12))
            },
        "inputs":{
            "input0" : c.InputField(label="Digite o nome do produto"),
            "input1" : c.InputField(label="Digite o valor do produto"),
            "input2" : c.InputField(label="Digite a descrição do produto"),
            "input3" : c.InputField(label="Digite a marca do produto"),
            }
        }
    listapessoas={}
    listapesquisas={}  
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

    def pro(x):
        mid = listaprod["labels"][f"label{x}"], listaprod["inputs"][f"input{x}"]
        return mid

    def cadastroProduto():
        i = 4
        titulo = ft.Text("Cadastro de produtos",size=24)
        btn = ft.Container(content = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500), alignment=ft.alignment.center_right)
        mid_sec = ft.ResponsiveRow(controls=[
                        ft.Column(col={"md": 6}, controls = pro(0)),
                        ft.Column(col={"md": 6}, controls = pro(1)),
                        ft.Column(col={"md": 6}, controls = pro(2)),
                        ft.Column(col={"md": 6}, controls = pro(3)),
                    ])
            
        mid = ft.Column([titulo,mid_sec,btn])
        corpo = c.CorpoContainer(content = ft.Column(controls=[header, mid, footer]))
        page.add(corpo)

    def cadastroPessoa():
        i = 2
        titulo = ft.Container(ft.Text("Cadastro de pessoa",size=24))
        label1 = ft.Container(ft.Text("Nome da pessoa:",size=12))
        input1 = c.InputField(label="Digite o nome da pessoa")
        label2 = ft.Container(ft.Text("Sobrenome da pessoa:",size=12))
        input2 = c.InputField(label="Digite o sobrenome da pessoa")
        btn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500)
        mid_sec = ft.Column([titulo, ft.ResponsiveRow(controls=[
                        ft.Column(col={"md": 6}, controls=[label1,input1]),
                        ft.Column(col={"md": 6}, controls=[label2,input2]),
                    ]),
                    ft.Container(content = btn, alignment=ft.alignment.center_right),
                    ])
        corpo = c.CorpoContainer(content = ft.Column(controls=[header, mid_sec, footer]))
        page.add(corpo)

    def cadastroPesquisa():
        i = 5
        titulo = ft.Container(ft.Text("Cadastro de Pesquisa",size=24))
        label1 = ft.Container(ft.Text("Nome do produto concorrente:",size=12))
        input1 = c.InputField(label="Digite o nome do produto concorrente")
        label2 = ft.Container(ft.Text("Valor do produto concorrente:",size=12))
        input2 = c.InputField(label="Digite o valor do produto concorrente")
        label3 = ft.Container(ft.Text("Marca do produto concorrente:",size=12))
        input3 = c.InputField(label="Digite a marca do produto concorrente")
        label4 = ft.Container(ft.Text("A quanto tempo compra o produto concorrente:",size=12))
        input4 = c.InputField(label="Digite o tempo em meses")
        label5 = ft.Container(ft.Text("Observação:",size=12))
        input5 = c.InputField(label="Digite a observação",multiline=True,min_lines=3,max_lines=6)
        btn = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add, bgcolor=ft.colors.GREEN_500)
        mid_sec = ft.Column([titulo, ft.ResponsiveRow(controls=[
                        ft.Column(col={"md": 6}, controls=[label1,input1]),
                        ft.Column(col={"md": 6}, controls=[label2,input2]),
                        ft.Column(col={"md": 6}, controls=[label3,input3]),
                        ft.Column(col={"md": 6}, controls=[label4,input4]), 
                    ]),
                    ft.Container(content = ft.Column(controls=[label5,input5])),
                    ft.Container(content = btn, alignment=ft.alignment.center_right),
                    ])
        corpo = c.CorpoContainer(content = ft.Column(controls=[header, mid_sec, footer]))
        page.add(corpo)
        

    cadastroProduto()

    page.update()
ft.app(target=main)
