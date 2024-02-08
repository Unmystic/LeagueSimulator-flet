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

    CreateTeamButton = ft.ElevatedButton(
                    content=ft.Text(value="Create team", size=16, font_family="Segoe Print Bold"),
                    style=ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                        ft.MaterialState.FOCUSED: ft.colors.BLACK,
                        ft.MaterialState.DEFAULT: ft.colors.BLACK,
                    },
                    bgcolor={ft.MaterialState.FOCUSED: ft.colors.GREEN_800, "": ft.colors.GREEN_500},
                    padding={ft.MaterialState.DEFAULT: 20},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0, "": 1},
                    animation_duration=500,
                    side={
                        ft.MaterialState.DEFAULT: ft.BorderSide(1, ft.colors.WHITE),
                        ft.MaterialState.HOVERED: ft.BorderSide(2, ft.colors.WHITE),
                    },
                    shape={
                        ft.MaterialState.HOVERED: ft.RoundedRectangleBorder(radius=10),
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=10),
                    },
                    ),
                    on_click=lambda e: print("Team created"),
                )

    
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
        ft.Divider(),
        ft.Column([
            ft.Checkbox(label="Create your own team", value=False),
            ft.TextField(label="Team Name",border=ft.InputBorder.NONE, disabled=True, hint_text="Please enter your team name"),
            ft.Text(weight=ft.FontWeight.BOLD,size=16, value="Choose team playstyle"),
            ft.Dropdown(
                width=200,
                options=[
                    ft.dropdown.Option("Balanced"),
                    ft.dropdown.Option("Very Defensive"),
                    ft.dropdown.Option("Defensive"),
                    ft.dropdown.Option("Attacking"),
                    ft.dropdown.Option("Very Attacking"),
                    ],
                )
            ],
            tight=True,

            ),
        ft.Row([CreateTeamButton], alignment=ft.MainAxisAlignment.END),
        ft.Divider(),
        
        )


ft.app(target=main)