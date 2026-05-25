import flet as ft

def PerfilView(page: ft.Page, auth_controller):
    user = page.user_data
        
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
                spacing=10
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
            actions=[
                ft.IconButton(ft.Icons.HOME, on_click=lambda _:page.go("/inicio"), tooltip="Inicio"),
                ft.IconButton(ft.Icons.ACCOUNT_CIRCLE, on_click=lambda _:page.go("/perfil"), tooltip="Perfil"),
                ft.IconButton(ft.Icons.MONEY, on_click=lambda _:page.go("/presupuesto"), tooltip="Consultar dinero"),
                ft.IconButton(ft.Icons.PAYMENTS, on_click=lambda _:page.go("/gastos"), tooltip="Consultar gastos"),
                ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _:page.go("/"), tooltip="Cerrar sesión"),
            ],
        ),
        controls=[
            ft.Text("Bienvenido a tu perfil", size=24, weight="bold"),
            perfil
        ],
        spacing=20,
    )