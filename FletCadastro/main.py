import flet as ft 
import dictionary as l
import models as md
import classes as cl

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
        
        # Caso no dicionario o botão esteja visivel = não, cai no if e não mostra o mesmo na tela.
        if not l.lista[pagina]["vis"]:
            page.floating_action_button = ""
            page.update()
        else:
            # Botão flutuante e posicionamento  
            page.floating_action_button = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=btn_add,)
            page.floating_action_button_location = ft.FloatingActionButtonLocation.CENTER_FLOAT
            page.update()
            # Cria o corpo da tabela com as colunas
            my_table = ft.DataTable(columns=[ft.DataColumn(ft.Text(str(l.lista[pagina]["col"][x][1]),color=ft.colors.BLACK87)) for x in range(l.conta_lista(l.lista[pagina]))],rows=[],)
            # Traz o nome da tabela a ser processada
            tab = l.lista[pagina]["table"]
            # busca a lista de colunas do dicionario
            colunas = [(l.lista[pagina]["col"][x][0]) for x in range(l.conta_lista(l.lista[pagina]))]
            # tranforma a lista em uma string com "," entre as colunas
            unpacked = ", ".join([e for e in colunas])
            # cria o select com a tabela e as colunas previamente processadas
            result = md.sql.text(f"SELECT {unpacked} from {tab}")
            # Conecta no banco pra trazer as informações ja cadastradas
            query = md.session.execute(result).fetchall()
            # Cria o dataRow que vai compor a tabela com as celulas vazias
            dtRow = ft.DataRow(cells=[])
            # busca todas as tuplas derivadas do select feito anteriormente e passa para a variavel em forma de lista
            for tupla in query:
                # busca cada valor dentro da tupla do select feito anteriormente
                for valueX in tupla._tuple():
                    # Cria a variavel da celula e coloca os valores dentro de cada celula individualmente
                    dtCell = ft.DataCell(content=ft.Text(value=valueX ,color=ft.colors.BLACK))
                    dtRow.cells.append(dtCell)
                # Coloca cada linha processada dentro da tabela
                my_table.rows.append(dtRow)
                # Limpa a linha processada anteriormente
                dtRow = ft.DataRow(cells=[])
            # Adiciona um container expandido, depois a tabela criada 
            # e um outro conrtainer para gerar um espaço para o botão de adicionar os valores no banco
            page.add(ft.Container(expand=1))
            page.add(ft.Container(content= ft.Column([ft.Row([my_table], scroll= ft.ScrollMode.ALWAYS)], scroll= ft.ScrollMode.ALWAYS),height=200), )
            page.add(ft.Container(height = 50))
            
    # Carrega a primeira tela ao abrir o aplicativo
    pag_index(0)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)
