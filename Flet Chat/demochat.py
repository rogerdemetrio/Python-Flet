import flet as ft
 
def main(pagina):
    # Atributos da pagina
    pagina.title = "ChatChatChatLine"
    pagina.bgcolor = ft.colors.GREY_700
    pagina.padding = 25
    pagina.spacing = 0
    #pagina.horizontal_alignment = "center"

    # Variaveis globais
    texto = ft.Text("ChatChatChatLine")

    chat = ft.Column(auto_scroll=True,scroll=ft.ScrollMode.HIDDEN)

    nome_usuario = ft.TextField(label="Nome do usuario")

    #Tunel que envia a mensagem para os outros usarios
    def enviar_mensagem_tunel(mensagem):
        tipo = mensagem["tipo"]
        if tipo == "mensagem":
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            # adicionar a mensagem no chat
            if mensagem["texto"] != "":
                chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))
        else:
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", size=12, italic=True, color=ft.colors.YELLOW_ACCENT_700))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,"tipo": "mensagem"})
        # limpar o campo de mensagem
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    def entrar_popup(evento):
        if nome_usuario.value != "":
            pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})
            # fechar o popup
            popup.open = False
            # remover o botao iniciar chat e texto enviado
            pagina.remove(botao_iniciar)
            pagina.remove(texto)
            # adicionar o chat
            # e criar o campo de mensagem do usuario e o botao de enviar mensagem do usuario
            pagina.add(ft.Container(chat, expand=True),
                       ft.Row([ft.Container(ft.Row([campo_mensagem, botao_enviar_mensagem]), expand=True)]))
        
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao ChatChatChatLine"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],
        )

    def entrar_chat(evento):
        pagina.overlay.append(popup)
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(target=main, view=ft.WEB_BROWSER, port=8080)

# deploy
