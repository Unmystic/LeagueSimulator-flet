import flet as ft

def main(page: ft.Page):
    def dropdown_changed(e):
        print(dd.value)
        t.value = f"Dropdown changed to {dd.key}"
        page.update()

    t = ft.Text()
    dd = ft.Dropdown(
        on_change=dropdown_changed,
        options=[
            ft.dropdown.Option(text="Red", key=1),
            ft.dropdown.Option(text="Green", key=2),
            ft.dropdown.Option(text="Blue", key=3),
        ],
        width=200,
    )
    page.add(dd, t)

ft.app(target=main)