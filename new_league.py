import flet as ft




class NewLeague(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.page.title = "New League"
        self.page.window_height = 680
        self.page.window_width = 480
        self.page.window_center()
        self.page.window_min_height, self.page.window_min_width = 680, 480
        self.page.fonts = {
            
            "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
        }

        # self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor =  ft.colors.SURFACE_VARIANT
        self.page.spacing = 5

        self.CreateTeamButton = ft.ElevatedButton(
                    content=ft.Text(value="Create team", size=14, font_family="Segoe Print Bold"),
                    style=ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                        ft.MaterialState.FOCUSED: ft.colors.BLACK,
                        ft.MaterialState.DEFAULT: ft.colors.BLACK,
                    },
                    bgcolor={ft.MaterialState.DISABLED: ft.colors.GREY, ft.MaterialState.DEFAULT: ft.colors.GREEN_500},
                    padding={ft.MaterialState.DEFAULT: 15},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0,ft.MaterialState.DISABLED:0, "": 1},
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
    
        self.PopulateLeagueButton = ft.ElevatedButton(
                        content=ft.Text(value="Populate league", size=14, font_family="Segoe Print Bold"),
                        style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                            ft.MaterialState.FOCUSED: ft.colors.BLACK,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        },
                        bgcolor={ft.MaterialState.DISABLED: ft.colors.GREY, ft.MaterialState.DEFAULT: ft.colors.GREEN_500},
                        padding={ft.MaterialState.DEFAULT: 15},
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation={"pressed": 0,ft.MaterialState.DISABLED:0, "": 1},
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
                        on_click=self.populate_league,
                    )
        
        self.StartSimulationButton = ft.ElevatedButton(
                        
                        content=ft.Text(value="Start simulation", size=14, font_family="Segoe Print Bold"),
                        style=ft.ButtonStyle(
                        color={
                            ft.MaterialState.HOVERED: ft.colors.BLACK,
                            ft.MaterialState.FOCUSED: ft.colors.BLACK,
                            ft.MaterialState.DEFAULT: ft.colors.BLACK,
                        },
                        bgcolor={ft.MaterialState.DISABLED: ft.colors.GREY, ft.MaterialState.DEFAULT: ft.colors.GREEN_500},
                        padding={ft.MaterialState.DEFAULT: 15},
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation={"pressed": 0,ft.MaterialState.DISABLED:0, "": 1},
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
                        disabled=True,
                        on_click=lambda e: page.go("/simulation"),
                    )

        self.TeamListBox = ft.TextField(
                        label="Competitors",
                        multiline=True,
                        disabled=True,
                        min_lines=10,
                        value="line1        line2\nline3        line4\nline5",
                    )
        


        self.result = ft.Text(weight=ft.FontWeight.BOLD,size=20, value="4")

        self.playstyle = ft.Dropdown(
                        width=150,
                        text_size=14,
                        dense=True,
                        content_padding=5,
                        options=[
                            ft.dropdown.Option("Balanced"),
                            ft.dropdown.Option("Very Defensive"),
                            ft.dropdown.Option("Defensive"),
                            ft.dropdown.Option("Attacking"),
                            ft.dropdown.Option("Very Attacking"),
                            ],
                        )


        self.league_creation = ft.Column([
            ft.Container(),
            ft.Row([
                ft.Container(expand=4, content=ft.Text("Select number of teams:", weight=ft.FontWeight.BOLD,size=14 )),
                ft.Container(expand=6, content=ft.Slider(min=4, max=20, divisions=8, label="{value} teams", on_change=self.slider_changed)),
                ft.Container(expand=1, content=self.result),            
                ]),            
            ft.Divider(),
            ft.Column([
                ft.Checkbox(label="Create your own team", value=False),
                ft.TextField(label="Team Name",border=ft.InputBorder.NONE, disabled=True, hint_text="Please enter your team name"),
                ft.Text(weight=ft.FontWeight.BOLD,size=14, value="Choose team playstyle"),
                self.playstyle

                ],
                tight=True,

                ),
            ft.Row([self.CreateTeamButton], alignment=ft.MainAxisAlignment.END),
            ft.Divider(),
            ft.Row([
                ft.Container(expand=5, content=self.TeamListBox, bgcolor = ft.colors.SURFACE_VARIANT),
                ft.Container(expand=2, content=ft.Column([self.PopulateLeagueButton, self.StartSimulationButton],
                                                        spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END)),                   
                ]),         
            
            ])




    def slider_changed(self,e):
        self.result.value = f"{int(e.control.value)}"

        self.result.update()
        self.page.update()

    def populate_league(self,e):
        self.StartSimulationButton.disabled = False
        self.StartSimulationButton.update()
        print("Pop")
        self.PopulateLeagueButton.disabled = True
        self.PopulateLeagueButton.update()
        # self.page.update()
    

    def build(self):
        print("I am here!")
        
        return  self.league_creation
    




def main2(page: ft.Page):

    nl = NewLeague(page)

    page.add(nl)

def main(page: ft.Page):

    #page.window_title_bar_hidden = True
    page.title = "Create a new league"
    page.window_height = 680
    page.window_width = 480
    page.window_center()
    page.window_min_height, page.window_min_width = 680, 480
    page.fonts = {
        
        "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
    }

    # page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.SURFACE_VARIANT
    page.spacing = 5

    CreateTeamButton = ft.ElevatedButton(
                    content=ft.Text(value="Create team", size=14, font_family="Segoe Print Bold"),
                    style=ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                        ft.MaterialState.FOCUSED: ft.colors.BLACK,
                        ft.MaterialState.DEFAULT: ft.colors.BLACK,
                    },
                    bgcolor={ft.MaterialState.DISABLED: ft.colors.GREY, ft.MaterialState.DEFAULT: ft.colors.GREEN_500},
                    padding={ft.MaterialState.DEFAULT: 15},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0,ft.MaterialState.DISABLED:0, "": 1},
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
    
    PopulateLeagueButton = ft.ElevatedButton(
                    content=ft.Text(value="Populate league", size=14, font_family="Segoe Print Bold"),
                    style=ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                        ft.MaterialState.FOCUSED: ft.colors.BLACK,
                        ft.MaterialState.DEFAULT: ft.colors.BLACK,
                    },
                    bgcolor={ft.MaterialState.DISABLED: ft.colors.GREY, ft.MaterialState.DEFAULT: ft.colors.GREEN_500},
                    padding={ft.MaterialState.DEFAULT: 15},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0,ft.MaterialState.DISABLED:0, "": 1},
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
                    on_click=lambda e: print("Teams added"),
                )
    
    StartSimulationButton = ft.ElevatedButton(
                    
                    content=ft.Text(value="Start simulation", size=14, font_family="Segoe Print Bold"),
                    style=ft.ButtonStyle(
                    color={
                        ft.MaterialState.HOVERED: ft.colors.BLACK,
                        ft.MaterialState.FOCUSED: ft.colors.BLACK,
                        ft.MaterialState.DEFAULT: ft.colors.BLACK,
                    },
                    bgcolor={ft.MaterialState.DISABLED: ft.colors.GREY, ft.MaterialState.DEFAULT: ft.colors.GREEN_500},
                    padding={ft.MaterialState.DEFAULT: 15},
                    overlay_color=ft.colors.TRANSPARENT,
                    elevation={"pressed": 0,ft.MaterialState.DISABLED:0, "": 1},
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
                    disabled=True,
                    on_click=lambda e: print("Signal to simulation"),
                )

    TeamListBox = ft.TextField(
                    label="Competitors",
                    multiline=True,
                    disabled=True,
                    min_lines=10,
                    value="line1        line2\nline3        line4\nline5",
                )
    
    def slider_changed(e):
        result.value = f"{int(e.control.value)}"
        page.update()

    result = ft.Text(weight=ft.FontWeight.BOLD,size=20,)
    page.add(
        ft.Container(),
        ft.Row([
            ft.Container(expand=4, content=ft.Text("Select number of teams:", weight=ft.FontWeight.BOLD,size=14, )),
            ft.Container(expand=6, content=ft.Slider(min=4, max=20, divisions=8, label="{value} teams", on_change=slider_changed)),
            ft.Container(expand=1, content=result),            
            ]),            
        ft.Divider(),
        ft.Column([
            ft.Checkbox(label="Create your own team", value=False),
            ft.TextField(label="Team Name",border=ft.InputBorder.NONE, disabled=True, hint_text="Please enter your team name"),
            ft.Text(weight=ft.FontWeight.BOLD,size=14, value="Choose team playstyle"),
            ft.Dropdown(
                width=150,
                text_size=14,
                dense=True,
                content_padding=5,
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
        ft.Row([
            ft.Container(expand=5, content=TeamListBox),
            ft.Container(expand=2, content=ft.Column([PopulateLeagueButton, StartSimulationButton],
                                                     spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END)),                   
            ]),         
        
        )

if __name__ == "__main__":
    ft.app(target=main2)