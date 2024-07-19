import flet as ft 

class Modulos:
#TODO:[prioridade] Modulo de produto   
    def cadastroProduto():           
        titulo = ft.Container(ft.Text("Cadastro de produtos",size=24))
        lab_pro = ft.Container(ft.Text("Nome do produto:",size=12))
        corpo = ft.Column([titulo,lab_pro])
        ft.Page.add(corpo)
    
#TODO: Modulo de pessoa
    def cadastroPessoa():
        titulo = ft.Text("Cadastro de pessoas",size=12)
        return titulo
    
#TODO: Modulo de pesquisa de mercado
    def cadastroPesquisa():
        titulo = ft.Text("Cadastro de pesquisa de mercado",size=12)
        return titulo
