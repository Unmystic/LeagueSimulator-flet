import flet as ft
import csv


def main(page: ft.Page):

    #page.window_title_bar_hidden = True
    page.title = "Hall of fame"
    page.window_height = 680
    page.window_width = 570
    page.window_center()
    page.window_min_height, page.window_min_width = 680, 560
    page.fonts = {
        
        "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
    }

    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#D3FFDE"
    page.spacing = 5

    top = []
    fieldnames = ['Name', 'Rating', 'Games',
                '+ / -', 'Wins', 'Draws', 'Points']

    def check_top():

        with open("Scripts/data/hof.csv", "r", newline='') as file:

            reader = csv.DictReader(file, fieldnames=fieldnames)
            next(reader)
            for row in reader:
                team = {'Name': row['Name'], 'Rating': row['Rating'], 'Games': row['Games'],
                        '+ / -': row['+ / -'], 'Wins': row['Wins'], 'Draws': row['Draws'],
                        'Points': row['Points']}

                top.append(team)
    
    check_top()
    

    hof_table = ft.DataTable(
            
            
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=[ft.colors.PINK_200, ft.colors.WHITE],
                ),
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(3, "blue"),
            horizontal_lines=ft.border.BorderSide(1, "green"),
            column_spacing=20,
            columns=[
                ft.DataColumn(ft.Text(f"{col}")) for col in fieldnames 

            ],
            rows=[
                ft.DataRow(cells=[ ft.DataCell(ft.Text(f"{row['Name']}")),
                                  ft.DataCell(ft.Text(f"{row['Rating']}")),
                                  ft.DataCell(ft.Text(f"{row['Games']}")),
                                  ft.DataCell(ft.Text(f"{row['+ / -']}")),
                                  ft.DataCell(ft.Text(f"{row['Wins']}")),
                                  ft.DataCell(ft.Text(f"{row['Draws']}")),
                                  ft.DataCell(ft.Text(f"{row['Points']}")),                              
                                    ]
                                  ) for row in top

            ]
            )


    page.add(
        ft.AppBar(title=ft.Text("Hall of Fame"), bgcolor=ft.colors.GREEN_ACCENT_200, center_title=True),
        hof_table       
        )

if __name__ == "__main__":
    ft.app(target=main)