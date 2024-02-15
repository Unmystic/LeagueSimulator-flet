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
        # self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.bgcolor =  ft.colors.SURFACE_VARIANT
        self.page.spacing = 5

        self.teams = {}
        self.table = []
        self.calendar = []
        self.tour = 0
        Schedule()
        self.fieldnames = ['Name', 'Rating', 'Games', 'Scored', 'Conceded',
                    '+/-', 'W', 'D', 'L', 'P']
      


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
                        on_click=self.matchdata_update
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
        

        self.league_table = ft.Ref[ft.DataTable]()

        self.match_data = ft.Ref[ft.ListView]()
        # self.match_data = ft.ListView(ref=self.match_data, expand=1, spacing=10, padding=20, auto_scroll=True)
        self.lstv =ft.ListView(ref=self.match_data, expand=1, spacing=10, padding=20, auto_scroll=True)

        self.lv = ft.Container(
                content=self.lstv,
                border=ft.border.all(2, ft.colors.GREEN_600),
                border_radius= ft.border_radius.all(30),
                width=700,
                
            )
        
    

        count = 1

        
        self.button_cont = ft.Container(content=ft.Column([self.SimulateTourButton, self.SimulateAllButton], 
                                                        spacing=175, horizontal_alignment= ft.CrossAxisAlignment.END)) 

        for i in range(0, 60):
            self.lv.content.controls.append(ft.Text(f"Line {count}"))
            count += 1

        self.first_tab = ft.Row(controls=[
                # self.league_table,
                # ft.Column([ft.Text("Linear progress indicator", style="headlineSmall"),
                #            ft.Container(content=ft.Column( [self.pb, self.button_cont]))])
                ft.Text("Just a test"),  
                
                ft.Container(content= self.button_cont,
                        )
                    
                ], spacing =50)



    def matchdata_update(self,e):
        # print(self.match_data.current.controls)
        self.match_data.current.controls.append(ft.Text("Yeppo"))
        # e.control.update()
        #self.t.update()
        # print(self.t.tabs[1].content.content.controls)
        # self.lstv.update()
        self.page.update()
        
        
    def tabs_changed(self,e):
        # print(dir(e))
        # print(e.control)
        self.match_data.current.controls.append(ft.Text(" Added"))
        e.control.update()
        # self.lv.content.controls.update()


    def build(self):
        print("I am here!")
        
        self.t = ft.Tabs(
            selected_index=0,
            animation_duration=300,
            tabs=[
                ft.Tab(
                    text="League Table ",
                    content=ft.Container(
                        content=self.first_tab, alignment=ft.alignment.top_left
                    ),
                ),

                ft.Tab(
                    text="Match results",
                    icon=ft.icons.SHORT_TEXT,
                    content=ft.Container(content=self.lstv)
                ),
            ],
        # width=900,
        height=750,
        on_change=self.tabs_changed
            
        )

        
      
        return  self.t



def main2(page: ft.Page):
    nl = SimulateLeague(page)
    page.add(nl)

if __name__ == "__main__":
    ft.app(target=main2)