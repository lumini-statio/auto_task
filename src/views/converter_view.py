import flet as ft


def converter_page(page: ft.Page):

    def on_selected_file(e: ft.FilePickerResultEvent):

        file_path.value = (
            ", ".join(map(lambda f: f.path, e.files))
            if e.files else "Cancelled!"
        )

        file_path.update()

    picker = ft.FilePicker(on_result=lambda e: on_selected_file(e))
    file_path = ft.Text()

    page.overlay.append(picker)

    btn_picker = ft.ElevatedButton(
                    "Pick files",
                    icon=ft.Icons.UPLOAD_FILE,
                    on_click=lambda _: picker.pick_files()
                )

    main = ft.Container(
                content=ft.Column([btn_picker, file_path], expand=True),
                padding=ft.padding.all(30),
                expand=True
            )

    return main
