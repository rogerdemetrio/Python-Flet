import flet as ft 

# Classe padrão dos TextField da main
class InputField(ft.TextField):
    def __init__(self,label="",multiline=False,min_lines=1,max_lines=1):
        super().__init__()
        self.label=label
        self.bgcolor=ft.colors.GREY_800
        #self.focused_border_color=ft.colors.AMBER_500
        self.border_color=ft.colors.WHITE
        self.multiline = multiline
        self.min_lines = min_lines
        self.max_lines = max_lines
        #self.border=ft.InputBorder.NONE
        #self.filled=True
        self.hint_text="Digite aqui"

class LinhaDiv(ft.Divider):
    def __init__(self):
        super().__init__()
        self.color = ft.colors.WHITE54