import flet as ft
from bg_view import bg_remover_page


def main(page: ft.Page):

    page.title = 'Random password generator'
    page.window.width = 1000
    page.window.height = 700
    page.padding = 0
    page.bgcolor = ft.Colors.BACKGROUND
    page.theme_mode = ft.ThemeMode.DARK

    app = ft.Container(
        content=ft.NavigationBar(
            selected_index=0,
            destinations=[
                ft.NavigationBarDestination(
                    icon=ft.Icons.IMAGE, 
                    selected_icon=ft.Icons.IMAGE_OUTLINED,
                    label='background remover'
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FILE_DOWNLOAD, 
                    selected_icon=ft.Icons.FILE_OPEN,
                    label='file converter'
                ),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FILE_DOWNLOAD, 
                    selected_icon=ft.Icons.FILE_OPEN,
                    label='repeated file remover'
                ),
            ]
        )
    )

    page.add(app)