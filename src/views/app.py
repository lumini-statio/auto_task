import flet as ft
import traceback
from src.views.bg_view import bg_remover_page
from src.views.converter_view import converter_page
from src.views.repeated_view import repeated_page
from src.core.utils.logger import log


def main(page: ft.Page):

    page.title = 'Random password generator'
    page.window.width = 1000
    page.window.height = 700
    page.padding = 0
    page.theme_mode = ft.Theme(
        color_scheme_seed=ft.Colors.BLUE, 
        visual_density=ft.VisualDensity.COMFORTABLE,
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            secondary=ft.Colors.ORANGE,
            surface=ft.Colors.GREY_800,
            background=ft.Colors.BLUE
        )
    )

    try:
        def change_view(e):
            selected = e.control.selected_index

            if selected == 0:
                content_area.content = bg_remover_page(page)
            elif selected == 1:
                content_area.content = converter_page(page)
            elif selected == 2:
                content_area.content = repeated_page(page)
            
            page.update()

        content_area = ft.Container(
            content=bg_remover_page(page),
            expand=True
        )

        app = ft.Container(
            content=ft.Column([
                ft.NavigationBar(
                    selected_index=0,
                    destinations=[
                        ft.NavigationBarDestination(
                            icon=ft.Icons.IMAGE, 
                            selected_icon=ft.Icons.IMAGE_OUTLINED,
                            label='background remover'
                        ),
                        ft.NavigationBarDestination(
                            icon=ft.Icons.FILE_OPEN, 
                            selected_icon=ft.Icons.FILE_OPEN_OUTLINED,
                            label='file converter'
                        ),
                        ft.NavigationBarDestination(
                            icon=ft.Icons.DELETE, 
                            selected_icon=ft.Icons.DELETE_OUTLINE,
                            label='repeated file remover'
                        )],
                        on_change=change_view
                    ),
                    content_area]
                ),
            expand=True
        )

        page.add(app)
    
    except Exception:
        log(f'{__file__} - {traceback.format_exc()}')