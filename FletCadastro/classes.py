import flet as ft 


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

class CorpoContainer(ft.Container):
    def __init__(self,content=[]):
        super().__init__()
        self.content = content
        self.padding = 5
        self.margin = 5
        self.expand = 2
