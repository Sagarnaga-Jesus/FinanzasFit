import flet as ft

def PerfilView(page: ft.Page, auth_controller):
    
    def regresar(e):
        page.go("/inicio")
    
    return ft.View(
        route="/perfil",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Perfil"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Text("Bienvenido a tu perfil", size=24, weight="bold"),
            ft.ElevatedButton("Regresar al inicio", on_click=regresar, width=200, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.HOME, color=ft.Colors.WHITE, size=25)))
        ],
        spacing=20,
    )