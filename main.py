import flet as ft

import about
import tutorial

from hall_of_fame import HoFClass

def main(page: ft.Page):

    #page.window_title_bar_hidden = True
    page.window_height = 640
    page.window_width = 680
    page.window_center()
    page.window_min_height, page.window_min_width = 640, 680
    page.fonts = {
        
        "Segoe Print Bold": "fonts/segoeprint_bold.ttf",
    }

    page.theme_mode = ft.ThemeMode.LIGHT
    # page.bgcolor = "#D3FFDE"
    page.spacing = 5

    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")
        page.show_snack_bar(ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!")))
        page.update()
        
    def handle_on_open(e):
        print(f"{e.control.content.value}.on_open")

    def handle_on_close(e):
        print(f"{e.control.content.value}.on_close")

    def handle_on_hover(e):
        print(f"{e.control.content.value}.on_hover")

    author = ft.Text("Developed by Dmitry Platonychev",size=20, italic=True)
    resourses = ft.Text("Resources : Material Icons, Midjourney")
    year = ft.Text("2024")

    def close_dlg(e):
        dlg.open = False
        page.update()

    dlg = ft.AlertDialog(
        modal=True,
        title=ft.Text("League Simulation GUI", text_align="CENTER"),
      
        content= ft.Column([
            author,
            resourses,
            year
            ],
            tight=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
            
        ],
        actions_alignment=ft.MainAxisAlignment.CENTER,
        on_dismiss=lambda e: print("Dialog dismissed!")
    )



    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    # page.appbar = ft.AppBar(
    #     title=ft.Text("Menus", ref=appbar_text_ref, font_family="Segoe Print Bold"),
    #     center_title=True,
    #     bgcolor=ft.colors.BLUE
    # )

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.colors.WHITE,
            mouse_cursor={ft.MaterialState.HOVERED: ft.MouseCursor.WAIT,
                          ft.MaterialState.DEFAULT: ft.MouseCursor.ZOOM_OUT},
            shape={ft.MaterialState.DEFAULT: ft.ContinuousRectangleBorder(radius=2),},
            surface_tint_color=None,
            padding=0
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                on_open=handle_on_open,
                on_close=handle_on_close,
                on_hover=handle_on_hover,
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("New League"),
                        leading=ft.Icon(ft.icons.FIBER_NEW, color=ft.colors.GREEN_200),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_200}),
                        on_click=handle_menu_item_click
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Hall of Fame"),
                        leading=ft.Icon(ft.icons.STARS_OUTLINED,color='#FF80ED'),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_200}),
                        on_click=handle_menu_item_click
                    ),
                    ft.Divider(),
                    ft.MenuItemButton(
                        content=ft.Text("Quit"),
                        leading=ft.Icon(ft.icons.CLOSE, color='red'),
                        style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_200}),
                        on_click=lambda _: page.window_close()
                    )
                ]
            ),
            ft.SubmenuButton(
                content=ft.Text("Help"),
                on_open=handle_on_open,
                on_close=handle_on_close,
                on_hover=handle_on_hover,
                controls=[
        
                            ft.MenuItemButton(
                                content=ft.Text("About"),
                                leading=ft.Icon(ft.icons.INFO),
                                close_on_click=False,
                                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_200}),
                                on_click=lambda e: about.About_dlg(page)
                            ),
                            ft.MenuItemButton(
                                content=ft.Text("Tutorial"),
                                leading=ft.Icon(ft.icons.HELP),
                                close_on_click=False,
                                style=ft.ButtonStyle(bgcolor={ft.MaterialState.HOVERED: ft.colors.GREEN_200}),
                                on_click=lambda e: tutorial.Tutorial_dlg(page)
                            )
                  
                ]
            ),
        ]
    )

    img = ft.Image(
        
        src=f"animals_soccer.png",
        fit=ft.ImageFit.CONTAIN,
        width = page.width,
        height = page.height * 0.7,
        expand=True,
    )

    btn1 = ft.ElevatedButton(
                    expand=True,
                    content=ft.Text(value="New League", size=16, font_family="Segoe Print Bold"),
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
                )
    
    btn2= ft.ElevatedButton(
                    expand=True,
                    content=ft.Text(value="Hall of Fame", size=16, font_family="Segoe Print Bold"),
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
                    on_click=lambda _: page.go("/store"),
                )
    
    btn3= ft.ElevatedButton(
                    expand=True,
                    content=ft.Text(value="Tutorial", size=16, font_family="Segoe Print Bold"),
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
                    on_click= lambda e: tutorial.Tutorial_dlg(page),
                )
    
    btn4 = ft.ElevatedButton(
                    expand=True,
                    content=ft.Text(value="About", size=16, font_family="Segoe Print Bold"),
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
                    on_click=lambda e: about.About_dlg(page),
                )


    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Row([menubar]), 
                    ft.Container(img, alignment=ft.alignment.center, expand=True),
                    ft.Row([btn1, btn2, btn3, btn4], alignment=ft.MainAxisAlignment.SPACE_EVENLY ) 
                ],
            )
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Hall of Fame"), bgcolor=ft.colors.GREEN_ACCENT_200, center_title=True),
                        HoFClass(page),
                    ],
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)




    # page.add(
    #     ft.Row([menubar]), 
    #     ft.Container(img, alignment=ft.alignment.center, expand=True),
    #     ft.Row([btn1, btn2, btn3, btn4], alignment=ft.MainAxisAlignment.SPACE_EVENLY ) 
        
        
    # )


ft.app(target=main)