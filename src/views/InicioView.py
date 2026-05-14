import flet as ft

def InicioView(page):
    return ft.View(
        route="/inicio",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Inicio"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.HOME, size=50, color=ft.Colors.GREEN),
                    ft.Text(f"Bienvenido, {page.user_data['nombre']}!", size=24, weight="bold"),
                    ft.Text("Bienvenido a Finanzas Fit", size=24, weight="bold"),
                    ft.Text("Tu compañero para una vida financiera saludable", size=16)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]
    )