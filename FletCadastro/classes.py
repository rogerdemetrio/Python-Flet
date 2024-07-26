import flet as ft 

# Classe padrão dos TextField da main
class InputField(ft.TextField):
    def __init__(self,label="",hint_text="Digite aqui seu texto",multiline=False,min_lines=1,max_lines=1,input_filter=ft.InputFilter(allow=False, regex_string=r"[#$@/*=+(){}[!?;:&%]", replacement_string="")):
        super().__init__()
        self.label=label
        self.bgcolor=ft.colors.GREY_800
        #self.focused_border_color=ft.colors.AMBER_500
        self.border_color=ft.colors.WHITE
        self.multiline = multiline
        self.min_lines = min_lines
        self.max_lines = max_lines
        self.input_filter = input_filter
        #self.border=ft.InputBorder.NONE
        #self.filled=True
        self.hint_text=hint_text

class LinhaDiv(ft.Divider):
    def __init__(self):
        super().__init__()
        self.color = ft.colors.BLACK45

def header():
    return ft.Column([ft.Container(content=ft.Text(spans=[
        ft.TextSpan("InfoDeme ",ft.TextStyle(color="#333333")), 
        ft.TextSpan("Cadastros",ft.TextStyle(color="#111111"))],
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE),alignment=ft.alignment.center), 
        LinhaDiv()])