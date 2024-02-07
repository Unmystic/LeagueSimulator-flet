import flet as ft


def main(page: ft.Page):

    #page.window_title_bar_hidden = True
    page.title = "Create a new league"
    page.window_height = 640
    page.window_width = 680
    page.window_center()
    page.window_min_height, page.window_min_width = 640, 680
    page.fonts = {
        
        "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
    }

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#D3FFDE"
    page.spacing = 15

    
    def slider_changed(e):
        result.value = f"{int(e.control.value)}"
        page.update()

    result = ft.Text(weight=ft.FontWeight.BOLD,size=24,)
    page.add(
        ft.Container(),
        ft.Row([
            ft.Container(expand=4, content=ft.Text("Select number of teams:", weight=ft.FontWeight.BOLD,size=18, )),
            ft.Container(expand=6, content=ft.Slider(min=4, max=20, divisions=8, label="{value} teams", on_change=slider_changed)),
            ft.Container(expand=1, content=result),            
            ]),
        
        ft.Divider())


ft.app(target=main)