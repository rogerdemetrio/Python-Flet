import flet as ft 
import dictionary as l
import models as md
import classes as cl

#TODO -> Mostrar informação do banco na tela

def main(page: ft.Page):
    # Padrões da pagina alterados para trazer em forma de aplicativo para smartphone "simulado"
    page.window.height = 920
    page.window.width = 480
    page.window.maximizable = False
    page.window.resizable = False
    page.window.shadow = True

    # Cores, titulo e alguns outros parametros basicos
    page.title = "Central de cadastros"
    page.theme = ft.Theme(color_scheme_seed=ft.colors.RED_900)
    page.bgcolor = ft.colors.GREY_500
    page.window.center()
    page.padding = 20
    
    # Tipo de navegação da pagina
    page.navigation_bar = ft.CupertinoNavigationBar(
            bgcolor=ft.colors.BLACK45,
            inactive_color=ft.colors.WHITE70,
            icon_size=36,
            on_change=lambda e: pag_index(e.control.selected_index),
            destinations=[
                # Busca a lista de destinos que são os botões inferiores, 
                # é criado dinamicamente conforme configurado no dictionary.py
                l.lista[x]["dest"] for x in range(len(l.lista))
            ],
        )
    
    # Função que adiciona as informações no banco de dados 
    # quando o botão flutuante é acionado
    def btn_add(ev):
        # Pega os valores dos inputs nas telas em forma de lista
        i = [inputText.value for inputText in body.controls]
        # Cria uma tabela vazia
        tabela = {}
        # Laço para formar um dicionario com os dados de coluna e input ficando assim {'coluna': 'input', 'coluna2': 'input2'}. 
        # Esse dicionario vem da junção da dos valores da "col" que ficam no dicionary.py, 
        # com os valores encontrados nos campos de input na tela principal
        for x in range(l.conta_lista(l.lista[pagina])):
            tabela.update({str(l.lista[pagina]["col"][x]):str(i[x])})
        # Depois de formado o dicionario, é criado essa variavel para "quebrar" a lista 
        # passando na frente dela o parametro de cada tabela correspondente a tela. 
        # Ficando assim: md.Produto({'coluna'= 'input', 'coluna2'= 'input2'}) 
        # e depois passando para o banco através da session e comitando
        tb = l.lista[pagina]["tb"](**tabela)
        md.session.add(tb)
        md.session.commit()

    # Função de paginação, traz os elementos viziveis 
    # (fora botão e navegação)
    def pag_index(ev):
        global body,pagina
        pagina = ev
        page.controls.clear() 
        body = ft.Column(controls=[l.lista[pagina]["inputs"][x] for x in range(l.conta_lista(l.lista[pagina]))])
        page.add(ft.Column(controls=[cl.header()]),ft.Column(controls=[l.lista[pagina]["tit"]]),
                 ft.Column(controls=[body]),ft.Column(controls=[cl.LinhaDiv()]))
        
        # Botão flutuante e posicionamento
        if not l.lista[pagina]["vis"]:
            page.floating_action_button = ""
            page.update()
        else:
            lista = ft.ListView
            page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add,)
            page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_FLOAT
            page.update()
            
            # Conecta no banco pra trazer as informações ja cadastradas
            #BUG Ajustar urgente
            tab = l.lista[pagina]["table"]
            colunas = [(l.lista[pagina]["col"][x]) for x in range(l.conta_lista(l.lista[pagina]))]
            unpacked = ", ".join([tab+"."+ e for e in colunas])

            with md.engine.connect() as conn:
                query = conn.execute(md.text(f"SELECT {unpacked} FROM {tab}"))
                for inputText in query.all():
                    xxx = ft.DataCell(ft.Text(value=(inputText[x] for x in range(4))))
                    print(ft.Text(value=(inputText)))
                    my_table = ft.DataTable(columns=[ft.DataColumn(ft.Text(str(l.lista[pagina]["col"][x]))) for x in range(l.conta_lista(l.lista[pagina]))],rows=[],)
                    my_table.rows.append(ft.DataRow(cells=[xxx]))
                page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS), expand= 2), )
            
                
                

    # Carrega a primeira tela ao abrir o aplicativo
    pag_index(0)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
