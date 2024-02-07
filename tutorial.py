import flet as ft


table = """

After selecting **New League by** clicking button or choosing in menu you can :

1. Select number of teams your want in you league . 
For scheduling purposes the number has to be even. 
Currently max number of teams are 20.

2. You have an option to add your *own* custom team. 
*First*, you type your team name, then you can select your team playstyle.
*Team style* changes your attacking/defensive focus (essentially determines your preference to higher attack or defence rating).

3. *Finally*,  you must populate the league with additional teams to match your selected number of teams.
The names of the teams are generated based on the two dictionaries (firstname and lastname).
After population click **"Start Simulation"**.

4. You can simulate round by round or you can simulate whole tournament at once.
If you tired clicking **"Simulate tour"** button, you can simulate rest of the tournament.

5. To reach ***Hall of Fame*** table, your team must:

- Be undefeated.
- Have better result than 10th place in HoF.

"""


class Tutorial_dlg(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page  
        self.dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("How to simulate league tournament with this app?"),
        content=ft.Markdown(
            table,
            selectable=True,
            extension_set="gitHubWeb",
            code_theme="atom-one-dark",
            code_style=ft.TextStyle(font_family="Roboto Mono"),
            on_tap_link=lambda e: page.launch_url(e.data),
        ),
        actions=[
            ft.TextButton("Ok", on_click=self.close_dlg),
            
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.page.dialog = self.dlg
        self.dlg.open = True
        self.page.update()   

    def close_dlg(self, e):
         print("Wapapa")
         self.dlg.open = False
         self.page.update()

    def build(self, e):
        print("I am here!")
        # print("I am there!")
        return  self.dlg

# def run_dlg(page: ft.Page):
#     dial = About(page)
#     return dial

def main(page: ft.Page):

    page.title = "AlertDialog examples"
    #my_dlg =About_dlg(page)

    #print(my_dlg)
    page.add(
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: Tutorial_dlg(page)),
    )
    
if __name__ == "__main__":
    ft.app(target=main)






