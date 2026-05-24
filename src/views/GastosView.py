import flet as ft
from datetime import datetime
import shutil
import os

def GastosView(page: ft.Page):
    user = page.user_data
    
    def guardar(e):
        pass
    
    def regresar(e):
        page.go("/inicio")
    
    
    return ft.View(
        route="/gastos",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = "#B8FF9C",
        appbar=ft.AppBar(
            title=ft.Text("gastos realizados"),
            bgcolor="#000000",
            color="#1AC91A",
        ),
        controls=[
            ft.Text("En esta seccion podras consultar tus gastos realizados", size=24, weight="bold"),
            ft.ElevatedButton("Regresar al inicio", on_click=regresar, width=200, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.HOME, color=ft.Colors.WHITE, size=25)))
        ],
        spacing=20,
    )