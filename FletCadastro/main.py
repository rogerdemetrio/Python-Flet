import flet as ft 
#import classes as c
import listas as l
from models import Produto,Pessoa,Pesquisa

from sqlalchemy.sql import text,column
from sqlalchemy import create_engine
from sqlalchemy.orm import *

CONN = "sqlite:///bancoCadastro.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

#TODO -> Remover repetições 
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
            i = [inputText.value for inputText in body.controls]
            tabela = {}
            for x in range(4):            
                tabela.update({str(l.listaprod["col"][x]):str(i[x])})
            tb = Produto(**tabela)
            session.add(tb)
            session.commit()

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
