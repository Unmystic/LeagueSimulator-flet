import flet as ft
import statistics
import random
import csv



class NewLeague(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.page.title = "New League"
        self.page.window_height = 645
        self.page.window_width = 480
        self.page.window_center()
        self.page.window_min_height, self.page.window_min_width = 640, 480
        self.page.fonts = {
            
            "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
        }

        # self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor =  ft.colors.SURFACE_VARIANT
        self.page.spacing = 5
        self.page.padding = 0
        self.page.update()

        # Counter  and list for teams - particapants
        self.count = 0
        self.teams = []


        # Here we go again with our WET dreams . TODO : create class for Buttons
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
                    disabled=True,
                    on_click=self.create_team,
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

        # Using list view instead textfield for  universality reasons, also it is easier to add items
        self.TeamListBox = ft.Container(
                content=ft.ListView(expand=1, spacing=1, padding=5, auto_scroll=True,item_extent=10, ),
                border=ft.border.all(2, ft.colors.GREEN_600),
                border_radius= ft.border_radius.all(10),
                width=400,
                height=250
                
            )
        

        # Display the selected number of particapnts via dropdown selection
        self.result = ft.Text(weight=ft.FontWeight.BOLD,size=20, value="4")

        self.playstyle = ft.Dropdown(
                        width=150,
                        text_size=14,
                        dense=True,
                        content_padding=5,
                        options=[
                            ft.dropdown.Option(text="Balanced",key=2),
                            ft.dropdown.Option(text="Very Defensive", key=0),
                            ft.dropdown.Option(text="Defensive", key=1),
                            ft.dropdown.Option(text="Attacking", key=3),
                            ft.dropdown.Option(text="Very Attacking", key=4),
                            ],
                        on_change=self.dropdown_changed
                        )

        # Textfield for new team initialy disabled 
        self.new_team_field = ft.TextField(label="Team Name",border=ft.InputBorder.NONE, disabled=True, hint_text="Please enter your team name")

        # Block for team creation wrapped in containers for grid manipulation reasons
        self.league_creation = ft.Container(content=ft.Column([
            ft.Container(bgcolor="#D3FFDE" ),
            ft.Row([
                ft.Container(expand=4, content=ft.Text("Select number of teams:", weight=ft.FontWeight.BOLD,size=14 ),bgcolor="#D3FFDE" ),
                ft.Container(expand=6, content=ft.Slider(min=4, max=20, divisions=8, label="{value} teams", on_change=self.slider_changed),bgcolor="#D3FFDE" ),
                ft.Container(expand=1, content=self.result,bgcolor="#D3FFDE" ),            
                ]),            
            ft.Divider(),
            ft.Column([
                ft.Checkbox(label="Create your own team", value=False, on_change=self.checkbox_changed),
                self.new_team_field,
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
                                                        spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END),bgcolor="#D3FFDE" ),                   
                ]),         
            
            ]),
            bgcolor="#D3FFDE",
            padding=0,
            margin=0
            )
          



    # Function for slider. Rewritind our laber with team numbers. Update necessary!
    def slider_changed(self,e):
        self.result.value = f"{int(e.control.value)}"

        self.result.update()
        self.page.update()


    # Checkbox logic, including solution to "add team after populatind the league" problem
    def checkbox_changed(self, e):

        if self.PopulateLeagueButton.disabled:
            self.CreateTeamButton.disabled = True
            self.CreateTeamButton.update()
            self.page.snack_bar = ft.SnackBar(ft.Text(f"League was already created!"))
            self.page.snack_bar.open = True
            self.page.update()


        elif self.CreateTeamButton.disabled:
            self.CreateTeamButton.disabled = False
            self.CreateTeamButton.update()
            self.new_team_field.disabled = False
            self.new_team_field.update()
        
        else:
            self.CreateTeamButton.disabled = True
            self.CreateTeamButton.update()
            self.new_team_field.disabled = True
            self.new_team_field.update()
        
    
    def dropdown_changed(self, e):

        self.playstyle.error_text = None       
        self.playstyle.update()

    #Button press logig for  Adding team to our listview
    def create_team(self,e):
        if self.new_team_field.value != "":
            print(self.playstyle.value)
            if self.playstyle.value == None:
                self.playstyle.error_text= "Please choose playstyle"
                self.playstyle.update()
                return

            self.count += 1
            choice = int(self.playstyle.value)
            ar, dr, tc = self.generate_rating(choice=choice)
            self.teams.append({"name": self.new_team_field.value, "attackRating": ar, "defenceRating": dr, "teamCohesion": tc})
            self.TeamListBox.content.controls.append(ft.Text(f"{self.count}. {self.new_team_field.value}"))
            self.TeamListBox.update()
            self.new_team_field.value == ""


    # Next three function taken from original code and slightly adapted. They are defining teams parameters and writing them in file
    def generate_rating(self, choice=2):
        ratings = [random.uniform(50, 59.99), random.uniform(60.00, 69.99), random.uniform(70.00, 79.99),
                   random.uniform(80.00, 89.99), random.uniform(90.00, 94.99)]
        balanced_weights = {"defence": [5, 10, 30, 40, 15], "attack": [5, 10, 30, 40, 15], "team_cohesion": [5, 10, 30, 40, 15]}
        def_weights = {"defence": [5, 10, 25, 40, 20], "attack": [5, 10, 35, 40, 10], "team_cohesion": [5, 10, 30, 35, 20]}
        very_def_weights = {"defence": [5, 10, 25, 35, 25], "attack": [5, 10, 40, 40, 5], "team_cohesion": [5, 10, 35, 40, 10]}
        att_weights = {"defence": [5, 10, 35, 40, 10], "attack": [5, 10, 25, 40, 20], "team_cohesion": [5, 10, 30, 35, 20]}
        very_att_weights = {"defence": [5, 10, 40, 40, 5], "attack": [5, 10, 25, 35, 25], "team_cohesion": [5, 10, 35, 40, 10]}
        weights = [very_def_weights, def_weights, balanced_weights, att_weights, very_att_weights]
        attackRating = round(statistics.fmean(random.choices(ratings, weights[choice]['attack'], k=5)), 2)
        defenceRating = round(statistics.fmean(random.choices(ratings, weights[choice]['defence'], k=5)), 2)
        teamCohesion = round(statistics.fmean(random.choices(ratings, weights[choice]['team_cohesion'], k=5)), 2)
        return attackRating, defenceRating, teamCohesion

    def write_teamdata(self):
        with open("Scripts/data/teams.csv", "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "attackRating", "defenceRating", "teamCohesion"])
            for team in self.teams:
                writer.writerow({"name": team["name"], "attackRating": team["attackRating"], "defenceRating": team["defenceRating"], "teamCohesion": team["teamCohesion"] })
            

    def populate_league(self,e):

        firstName = []
        lastName = []
        team_names = []

        with open("Scripts/data/firstName.txt") as file:
            for line in file:
                firstName.append(line.rstrip())
        with open("Scripts/data/lastName.txt") as file:
            for line in file:
                lastName.append(line.rstrip())

        for i in range(self.count, int(self.result.value),1):
            teamName = f"{firstName[random.randint(0, len(firstName) - 1)]} {lastName[random.randint(0, len(lastName) - 1)]}"
            if teamName in team_names:
                teamName = f"{firstName[random.randint(0, len(firstName) - 1)]} {lastName[random.randint(0, len(lastName) - 1)]}"
            choice = random.choice([1, 2, 3])
            ar, dr, tc = self.generate_rating(choice)
            self.TeamListBox.content.controls.append(ft.Text(f"{i + 1}. {teamName}"))
            self.TeamListBox.update()
            # self.listWidget.addItem(f"{i + 1}. {teamName}")
            self.teams.append({"name": teamName, "attackRating": ar, "defenceRating": dr, "teamCohesion": tc})
            team_names.append(teamName)

        self.write_teamdata()

        self.StartSimulationButton.disabled = False
        self.StartSimulationButton.update()
        self.PopulateLeagueButton.disabled = True
        self.PopulateLeagueButton.update()
        self.CreateTeamButton.disabled = True
        self.CreateTeamButton.update()

    

    def build(self):
        
        
        return  self.league_creation
    




def main2(page: ft.Page):

    nl = NewLeague(page)

    page.add(nl)



if __name__ == "__main__":
    ft.app(target=main2)