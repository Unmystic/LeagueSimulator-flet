import flet as ft
import csv
import statistics

class SimulateLeague(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page
        self.page.title = "New League"
        self.page.window_height = 800
        self.page.window_width = 980
        self.page.window_center()
        self.page.window_min_height, self.page.window_min_width = 680, 480
        self.page.fonts = {        
            "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
        }
        # self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor =  ft.colors.SURFACE_VARIANT
        self.page.spacing = 5

        self.teams = {}
        self.table = []
        self.fieldnames = ['Name', 'Rating', 'Games', 'Scored', 'Conceded',
                    '+/-', 'W', 'D', 'L', 'P']

        print(self.table)
        self.create_table()
        print(self.table)
        self.SimulateTourButton = ft.ElevatedButton(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(value="Simulate", size=20, font_family="Segoe Print Bold"),
                                    ft.Text(value="Tour", size=20, font_family="Segoe Print Bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                                ),
                            padding=ft.padding.all(10),),
                        # content=ft.Text(value="Create team", size=14, font_family="Segoe Print Bold"),
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
        
        self.SimulateAllButton = ft.ElevatedButton(
                        content=ft.Container(
                            content=ft.Column(
                                [
                                    ft.Text(value="Simulate", size=20, font_family="Segoe Print Bold"),
                                    ft.Text(value="All", size=20, font_family="Segoe Print Bold"),
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=5,
                                ),
                            padding=ft.padding.all(10),),
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
        
        self.league_table = ft.DataTable(
                                
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.alignment.bottom_right,
                        colors=[ft.colors.PINK_200, ft.colors.WHITE],
                        ),
                    border=ft.border.all(2, "black"),
                    border_radius=10,
                    vertical_lines=ft.border.BorderSide(3, "blue"),
                    horizontal_lines=ft.border.BorderSide(1, "green"),
                    horizontal_margin=10,
                    column_spacing=20,
                    data_row_min_height=20,
                    data_row_max_height=32,
                    heading_row_height=30,
                    data_text_style=ft.TextStyle(weight=ft.FontWeight.W_600, size=16),
                    columns=[
                        ft.DataColumn(ft.Text(f"{col}", size=17)) for col in self.fieldnames 

                    ],
                    rows=[
                        ft.DataRow(cells=[ ft.DataCell(ft.Text(f"{row[f'{k}']}",text_align="JUSTIFY")) for k in list(row.keys())]) for row in self.table

                    ]
                    )  


        self.lv = ft.Container(
                content=ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True),
                border=ft.border.all(2, ft.colors.GREEN_600),
                border_radius= ft.border_radius.all(30),
                width=700,
                
            )
        
    

        count = 1

        self.pb = ft.ProgressBar(width=150, value =0.05, bar_height=40, tooltip="League progress")


        self.button_cont = ft.Container(content=ft.Column([self.SimulateTourButton, self.SimulateAllButton], 
                                                        spacing=75, horizontal_alignment= ft.CrossAxisAlignment.END)) 

        for i in range(0, 60):
            self.lv.content.controls.append(ft.Text(f"Line {count}"))
            count += 1

        self.first_tab = ft.Row(controls=[
                self.league_table,
                ft.Column([ft.Text("Linear progress indicator", style="headlineSmall"),
                           ft.Container(content=ft.Column( [self.pb, self.button_cont]))])
                # self.league_table,
                # ft.Container(content=ft.Column([ ft.Text("Linear progress indicator", style="headlineSmall"), self.pb, self.button_cont],
                #         horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=75))
                    
                ])

        
        
    def create_table(self):
        with open("Scripts/data/teams.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["name", "attackRating", "defenceRating", "teamCohesion"])
            for row in reader:
                self.teams[row["name"]] = {"attackRating": float(row["attackRating"]), "defenceRating": float(row["defenceRating"]),
                                        "teamCohesion": float(row["teamCohesion"])}

        for team in self.teams:
            teamRating = round(statistics.fmean(
                [self.teams[team]["attackRating"], self.teams[team]["defenceRating"],
                self.teams[team]["teamCohesion"]]), 2)
            self.table.append(
                {'Name': team, 'Rating': teamRating, 'Games': 0, 'Scored': 0, 'Conceded': 0,
                '+/-': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
        
        

    def build(self):
        print("I am here!")

        t = ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Tab 1",
                content=ft.Container(
                    content=ft.Text("This is Tab 1"), alignment=ft.alignment.center
                ),
            ),
            ft.Tab(
                tab_content=ft.Icon(ft.icons.SEARCH),
                content=ft.Text("This is Tab 2"),
            ),
            ft.Tab(
                text="Tab 3",
                icon=ft.icons.SETTINGS,
                content=ft.Text("This is Tab 3"),
            ),
            ],
        width=400,
        height=400,
        )
        
        self.t = ft.Tabs(
            selected_index=1,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="League Table ",
                    content=ft.Container(
                        content=self.league_table, alignment=ft.alignment.top_left
                    ),
                ),

                ft.Tab(
                    text="Match results",
                    icon=ft.icons.SHORT_TEXT,
                    content=ft.Container(content=self.lv),
                ),
            ],
        width=800,
        height=980,
            
        )

        
        # print("I am there!")
        return  self.t



def main2(page: ft.Page):
    nl = SimulateLeague(page)
    page.add(nl)



def main(page: ft.Page):

    #page.window_title_bar_hidden = True
    page.title = "Create a new league"
    page.window_height = 800
    page.window_width = 980
    page.window_center()
    page.window_min_height, page.window_min_width = 680, 600
    page.fonts = {
        
        "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
    }

    # page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.PRIMARY_CONTAINER
    page.spacing =5
    

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
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(value="Simulate", size=20, font_family="Segoe Print Bold"),
                                ft.Text(value="Tour", size=20, font_family="Segoe Print Bold"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,
                            ),
                        padding=ft.padding.all(10),),
                    # content=ft.Text(value="Create team", size=14, font_family="Segoe Print Bold"),
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
                    content=ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(value="Simulate", size=20, font_family="Segoe Print Bold"),
                                ft.Text(value="All", size=20, font_family="Segoe Print Bold"),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=5,
                            ),
                        padding=ft.padding.all(10),),
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
                horizontal_margin=10,
                column_spacing=20,
                data_row_min_height=20,
                data_row_max_height=32,
                heading_row_height=30,
                data_text_style=ft.TextStyle(weight=ft.FontWeight.W_600, size=16),
                columns=[
                    ft.DataColumn(ft.Text(f"{col}", size=17)) for col in fieldnames 

                ],
                rows=[
                    ft.DataRow(cells=[ ft.DataCell(ft.Text(f"{row[f'{k}']}",text_align="JUSTIFY")) for k in list(row.keys())]) for row in table

                ]
                )  

    # LeagueTableBox = ft.TextField(
    #             label="Competitors",
    #             multiline=True,
    #             disabled=True,
    #             min_lines=10,
    #             value="line1        line2\nline3        line4\nline5",
    #         )

    lv = ft.Container(
            content=ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True),
            border=ft.border.all(2, ft.colors.GREEN_600),
            border_radius= ft.border_radius.all(30),
            width=700,
            
        )
    
    

    count = 1

    pb = ft.ProgressBar(width=150, value =0.05, bar_height=40, tooltip="League progress")


    button_cont = ft.Container(expand=1, content=ft.Column([SimulateTourButton, SimulateAllButton], 
                                                      spacing=75, horizontal_alignment= ft.CrossAxisAlignment.END)) 

    for i in range(0, 60):
        lv.content.controls.append(ft.Text(f"Line {count}"))
        count += 1

    first_tab = ft.Row([
            league_table,
            ft.Column([ ft.Text("Linear progress indicator", style="headlineSmall"), pb, button_cont],
                      horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=75),
                 
            ])

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="League Table ",
                content=ft.Container(
                    content=first_tab, alignment=ft.alignment.top_left
                ),
            ),

            ft.Tab(
                text="Match results",
                icon=ft.icons.SHORT_TEXT,
                content=lv,
            ),
        ],
        expand=3,
    )
    


    page.add(
        ft.Container(),
        t
        # ft.Row([
        #     t,
        #     ft.Container(expand=1, content=ft.Column([SimulateTourButton, SimulateAllButton],
        #                                              spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END)),                   
        #     ]),           
        # # ft.Divider(),
        # ft.Row([
        #     ft.Container(expand=3, content=ResultsBox),
        #     ft.Container(expand=1, content=ft.Column([ft.Text(weight=ft.FontWeight.BOLD,size=14, value="Choose team playstyle"),
        #                                                ft.Text(weight=ft.FontWeight.BOLD,size=14, value="Choose team playstyle")],
        #                                              spacing=100, horizontal_alignment= ft.CrossAxisAlignment.END)),                   
        #     ]),                
        )

if __name__ == "__main__":
    ft.app(target=main2)