import flet as ft
import csv
import statistics

def main(page: ft.Page):

    #page.window_title_bar_hidden = True
    page.title = "Create a new league"
    page.window_height = 680
    page.window_width = 960
    page.window_center()
    page.window_min_height, page.window_min_width = 680, 600
    page.fonts = {
        
        "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
    }

    # page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.PRIMARY_CONTAINER
    page.spacing = 0

    teams = {}
    table = []
    fieldnames = ['Name', 'Rating', 'Games', 'Scored', 'Conceded',
                 '+/-', 'W', 'D', 'L', 'P']

    def create_table():
        with open("Scripts/data/teams.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["name", "attackRating", "defenceRating", "teamCohesion"])
            for row in reader:
                teams[row["name"]] = {"attackRating": float(row["attackRating"]), "defenceRating": float(row["defenceRating"]),
                                           "teamCohesion": float(row["teamCohesion"])}

        for team in teams:
            teamRating = round(statistics.fmean(
                [teams[team]["attackRating"], teams[team]["defenceRating"],
                 teams[team]["teamCohesion"]]), 2)
            table.append(
                {'Name': team, 'Rating': teamRating, 'Games': 0, 'Scored': 0, 'Conceded': 0,
                 '+/-': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})

    create_table()

    SimulateTourButton = ft.ElevatedButton(
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
    
    SimulateAllButton = ft.ElevatedButton(
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
    
    league_table = ft.DataTable(
                               
                gradient=ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=[ft.colors.PINK_200, ft.colors.WHITE],
                    ),
                border=ft.border.all(2, "black"),
                border_radius=10,
                vertical_lines=ft.border.BorderSide(3, "blue"),
                horizontal_lines=ft.border.BorderSide(1, "green"),
                horizontal_margin=2,
                column_spacing=5,
                data_row_max_height=35,
                heading_row_height=30,
                data_text_style=ft.TextStyle(weight=ft.FontWeight.W_400, size=16),
                columns=[
                    ft.DataColumn(ft.Text(f"{col}")) for col in fieldnames 

                ],
                rows=[
                    ft.DataRow(cells=[ ft.DataCell(ft.Text(f"{row[f'{k}']}",text_align="start")) for k in list(row.keys())]) for row in table

                ]
                )  

    LeagueTableBox = ft.TextField(
                label="Competitors",
                multiline=True,
                disabled=True,
                min_lines=10,
                value="line1        line2\nline3        line4\nline5",
            )
    

    ResultsBox = ft.TextField(
                    label="Competitors",
                    multiline=True,
                    disabled=True,
                    min_lines=10,
                    value="line1        line2\nline3        line4\nline5",
                )
    
    page.add(
        ft.Container(),
        ft.Row([
            ft.Container(expand=3, content=league_table),
            ft.Container(expand=1, content=ft.Column([SimulateTourButton, SimulateAllButton],
                                                     spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END)),                   
            ]),           
        ft.Divider(),
        ft.Row([
            ft.Container(expand=3, content=ResultsBox),
            ft.Container(expand=1, content=ft.Column([ft.Text(weight=ft.FontWeight.BOLD,size=14, value="Choose team playstyle"),
                                                       ft.Text(weight=ft.FontWeight.BOLD,size=14, value="Choose team playstyle")],
                                                     spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END)),                   
            ]),                
        )


ft.app(target=main)