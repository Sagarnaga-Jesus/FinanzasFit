import flet as ft

logo = ft.Image(src="assets/FinanzasFit.png", width = 150, height = 150)

def InicioView(page):
    
    def cerrar_sesion():
        page.go("/")
        
    return ft.View(
        route="/inicio",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Inicio"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white",
            actions=[
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=cerrar_sesion,tooltip="Cerrar sesión")
                ],
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.HOME, size=50, color=ft.Colors.GREEN),
                    logo,
                    ft.Text(f"Bienvenido, {page.user_data['nombre']}!", size=24, weight="bold"),
                    ft.Text("Bienvenido a Finanzas Fit", size=24, weight="bold"),
                    ft.Text("Tu compañero para una vida financiera mas comoda y segura", size=16)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        ]
    )