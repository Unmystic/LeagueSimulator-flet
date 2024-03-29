import flet as ft
import csv
import statistics

from Scripts.schedule import Schedule
from Scripts.match_engine import Match
import Scripts.check_HoF


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
        self.page.bgcolor =  "green"
        self.page.spacing = 5

        self.page.update()

        self.teams = {}
        self.table = []
        self.calendar = []
        self.tour = 0
        Schedule()
        self.fieldnames = ['Name', 'Rating', 'Games', 'Scored', 'Conceded',
                    '+/-', 'W', 'D', 'L', 'P']
      
        self.create_table()
        self.fill_calendar()

        # Third WET boy adventure with buttons. TODO : rewrite buttons by creating the single class
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
                        on_click=self.simulate_tour
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
                        on_click=self.simulate_games,
                    )
        

        self.league_table = ft.Ref[ft.DataTable]()

        self.match_data = ft.Ref[ft.ListView]()
        self.lstv =ft.ListView(ref=self.match_data, expand=1, spacing=10, padding=20, auto_scroll=True)

        # Defining container for our matchdata listview
        self.lv = ft.Container(
                content=self.lstv,
                border=ft.border.all(2, ft.colors.GREEN_600),
                border_radius= ft.border_radius.all(30),
                width=700,
                bgcolor = ft.colors.SURFACE_VARIANT
                
            )
        
    

        count = 1

        self.pb = ft.ProgressBar(width=150, value =0, bar_height=40, tooltip="League progress")


        self.button_cont = ft.Container(content=ft.Column([self.SimulateTourButton, self.SimulateAllButton], 
                                                        spacing=175, horizontal_alignment= ft.CrossAxisAlignment.END), ) 

        # Our main and first tab four our TabView will include league table and container with buttons and progress bar

        self.first_tab = ft.Row(controls=[

                ft.DataTable(
                    ref=self.league_table,                                
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
                    columns=[ft.DataColumn(ft.Text(f"{col}", size=17)) for col in self.fieldnames ],
                    rows=[ft.DataRow(cells=[ ft.DataCell(ft.Text(f"{row[f'{k}']}",text_align="JUSTIFY")) for k in list(row.keys())]) for row in self.table

                    ]
                    ),  
                
                 ft.Container(content=ft.Column([ ft.Text("Progress of league", style="headlineSmall", width =100),
                                                self.pb,
                                                self.button_cont],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=50),bgcolor = "#D3FFDE")

                    
                ], spacing =50)

    # Update functions for our tabs, because view does not update themselfs
    def table_update(self):
        
        self.league_table.current.rows =[ft.DataRow(cells=[ ft.DataCell(ft.Text(f"{row[f'{k}']}",text_align="JUSTIFY"))
                                                           for k in list(row.keys())]) for row in self.table]
        self.page.update()
        self.first_tab.update() 

    def matchdata_update(self,e):

        self.match_data.update()
        self.page.update()
        
    #Rest of the functions,excluding build and tab change, are modified version of original functions.    
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

    def fill_calendar(self):
        # Populate calendar with games
        with open("Scripts/data/schedule.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames=["tour", "homeTeam", "awayTeam"])
            for row in reader:
                home = {}
                home["tour"] = row["tour"]
                home["name"] = row["homeTeam"]
                home["rating"] = self.teams[row["homeTeam"]]
                # Adding teamCohesion rating with each game
                self.teams[row["homeTeam"]]["teamCohesion"] = float(self.teams[row["homeTeam"]]["teamCohesion"]) + 0.25


                away = {}
                away["tour"] = row["tour"]
                away["name"] = row["awayTeam"]
                away["rating"] = self.teams[row["awayTeam"]]
                # Adding teamCohesion rating with each game
                self.teams[row["awayTeam"]]["teamCohesion"] = float(self.teams[row["awayTeam"]]["teamCohesion"]) + 0.25

                self.calendar.append([{"home": home, "away": away}])

    
    def simulate_games(self,e):
        # Simulating whole tournament using Match (from match_engine.py)

        # Finishing progress bar
        self.pb.value = 1

        count_games = 0
        self.tour += 1
        self.publish_tourdata(e)
        self.SimulateTourButton.disabled = True
        self.SimulateTourButton.update()

        for game in self.calendar:

            count_games += 1
            match = Match(game[0]['home'], game[0]['away'], self.table)
            result, self.table = match.match_data()
            self.match_data.current.controls.append(ft.Text(f" {result}", size=16, font_family="Segoe Print Bold"))
            

            if count_games == (len(self.teams) // 2):
                if self.tour == (len(self.teams) - 1) * 2 :
                    pass
                else:
                    self.tour += 1
                    self.publish_tourdata(e)
                    count_games = 0


        self.table.sort(reverse=True, key=self.Myfunc)
        self.table_update()
        
        self.lv.update()

        self.SimulateAllButton.disabled = True
        self.SimulateAllButton.update()


        self.tour = (len(self.teams) - 1) * 2
   

        if self.table[0]['L'] == 0:
            hof_table = Scripts.check_HoF.table_hof()
            Scripts.check_HoF.compare_results(team=self.table[0], hof_table=hof_table)

    # Sort table function was update to solve the "same amount of points" situations 
    def Myfunc(self, e):
        """sort list with dictionary by not one, but two of values"""

        return (e['P'], int(e['+/-']))

    def publish_tourdata(self,e):

        self.lv.content.controls.append(ft.Text("\n"))
        self.lv.content.controls.append(ft.Text(f"Tour {self.tour} match results are :", italic=True, size=18))
        self.lv.content.controls.append(ft.Text("\n"))

        self.lv.update()
        self.page.update()
        
        

    def simulate_tour(self, e):

        self.pb.value += 1/((len(self.teams) - 1)*2)

        games_in_tour = len(self.teams) // 2

        if len(self.calendar) == games_in_tour:
            self.SimulateTourButton.disabled = True
            self.SimulateTourButton.update()

            self.SimulateAllButton.disabled = True
            self.SimulateAllButton.update()

        self.tour += 1
        self.publish_tourdata(e)

        for i in range(games_in_tour):

            match = Match(self.calendar[i][0]['home'], self.calendar[i][0]['away'], self.table)
            result, self.table = match.match_data()
            self.match_data.current.controls.append(ft.Text(f"{result}", size=16, font_family="Segoe Print Bold"))
            
            
        self.lv.update()

        for i in range(games_in_tour):
            self.calendar.pop(0)

        self.table.sort(reverse=True, key=self.Myfunc)
        
        self.table_update()
        self.page.update()
        

        if len(self.calendar) == 0 and self.table[0]['L'] == 0:
            hof_table = Scripts.check_HoF.table_hof()
            Scripts.check_HoF.compare_results(team=self.table[0], hof_table=hof_table)

    # Does not do any difference, but could
    def tabs_changed(self,e):
        print("Tab switched")

    # Tab control defined in build function with no particular reason
    def build(self):
        
        self.t = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="League Table ",
                    content=ft.Container(
                        content=self.first_tab, alignment=ft.alignment.top_left, 
                        bgcolor ="#D3FFDE",
                    ),
                ),

                ft.Tab(
                    text="Match results",
                    icon=ft.icons.SHORT_TEXT,
                    content=ft.Container(content=self.lv)
                ),
            ],
        # width=900,
        overlay_color = ft.colors.SURFACE_VARIANT,
        unselected_label_color = "grey",
        divider_color = "#D3FFDE",
        height=750,
        # on_change=self.tabs_changed         
        )
     
        return  self.t



def main2(page: ft.Page):
    nl = SimulateLeague(page)
    page.add(nl)



if __name__ == "__main__":
    ft.app(target=main2)