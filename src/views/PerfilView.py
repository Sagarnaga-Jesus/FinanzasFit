import flet as ft

def PerfilView(page: ft.Page, auth_controller):
    user = page.user_data
    
    def regresar(e):
        page.go("/inicio")
        
    perfil = ft.Card(
        content = ft.Container(
            content = ft.Column([
                ft.Image(src=f"assets/{user['foto']}", width=150, height=150, border_radius=75), 
                ft.Divider(),
                ft.Text(f"Nombre: {user['nombre']}"),
                ft.Text(f"Correo: {user['email']}"),
                ft.Text(f"Fecha de registro: {user['fecha_registro']}")
            ], 
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10.
                ),
                width=400,
                height=350,
                padding=10,
        ))
    
    return ft.View(
        route="/perfil",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = "#B8FF9C",
        appbar=ft.AppBar(
            title=ft.Text("Perfil"),
            bgcolor="#000000",
            color="#1AC91A",
        ),
        controls=[
            ft.Text("Bienvenido a tu perfil", size=24, weight="bold"),
            perfil,
            ft.ElevatedButton("Regresar al inicio", on_click=regresar, width=200, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.HOME, color=ft.Colors.WHITE, size=25)))
        ],
        spacing=20,
    )