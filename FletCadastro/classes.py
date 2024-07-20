import flet as ft 

class InputField(ft.TextField):
    def __init__(self,label):
        super().__init__()
        self.label=label
        self.bgcolor=ft.colors.GREY_800
        self.focused_border_color=ft.colors.AMBER_500
        self.border_color=ft.colors.AMBER_600