import flet as ft
from datetime import datetime
import requests


def LoginView(page: ft.Page, auth_controller):
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    
    
    
    def login_click(e):
        if not correo.value or not contra.value:
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos")))
            return
        
    
        user, msg = auth_controller.login(correo.value, contra.value)
    
        if user:
            page.user_data = user
            page.go("/inicio")
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
            
    def olvidado():
        page.show_dialog(ft.SnackBar(ft.Text("Se a enviado su contraseña al correo")))
    
    
    iniciar= ft.ElevatedButton("Iniciar sesión", on_click=login_click, width=350, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.MAIL, color=ft.Colors.WHITE, size=25)))
    registrarse = ft.ElevatedButton("Crear una nueva cuenta", on_click=lambda _: page.go("/registro"), width=350, bgcolor="green", color = "black", icon=(ft.Icon(ft.Icons.ACCOUNT_BOX, color=ft.Colors.WHITE, size=25)))
    olvidada =( ft.TextButton("¿Olvidaste la contraseña?", on_click=olvidado))
    
    return ft.View(
        route="/",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        appbar=ft.AppBar(
            title=ft.Text("Login"),
            bgcolor=ft.Colors.BLUE_GREY_900,
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.GREEN),
                    ft.Text("Acceso al sistema de Finanzas Fit", size=24, weight="bold"),
                    correo,
                    contra,
                    iniciar,
                    registrarse,
                    olvidada
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ]
    )
    