import flet as ft


table = """

<div align="center">

**League Simulation GUI**


*Developed* by
**Dmitry Platonychev**

Art used :

- Fugue Icons by 
Yusuke Kamiyamane (original app version)

- Material Icons
 by Google (flet-remake)

- Midjourney

~~2023~~ 2024
</div>

"""


class About_dlg(ft.UserControl):

    def __init__(self, page: ft.Page):
        super().__init__()

        self.page = page  
        self.dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("About app"),
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
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: About_dlg(page)),
    )
    

ft.app(target=main)




# def main(page: ft.Page):
#     page.title = "AlertDialog examples"

#     dlg = ft.AlertDialog(
#         title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
#     )

#     def close_dlg(e):
#         dlg_modal.open = False
#         page.update()

#     dlg_modal = ft.AlertDialog(
#         modal=True,
#         title=ft.Text("About app"),
#         content=ft.Markdown(
#             table,
#             selectable=True,
#             extension_set="gitHubWeb",
#             code_theme="atom-one-dark",
#             code_style=ft.TextStyle(font_family="Roboto Mono"),
#             on_tap_link=lambda e: page.launch_url(e.data),
#         ),
#         actions=[
#             ft.TextButton("Ok", on_click=close_dlg),
            
#         ],
#         actions_alignment=ft.MainAxisAlignment.CENTER,
#         on_dismiss=lambda e: print("Modal dialog dismissed!"),
#     )

#     def open_dlg(e):
#         page.dialog = dlg
#         dlg.open = True
#         page.update()

#     def open_dlg_modal(e):
#         page.dialog = dlg_modal
#         dlg_modal.open = True
#         page.update()

#     page.add(
#         ft.ElevatedButton("Open dialog", on_click=open_dlg),
#         ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
#     )

