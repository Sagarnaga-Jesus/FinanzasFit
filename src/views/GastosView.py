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
        
    gasto = ft.Card(
        content = [
            ft.Text("Gastos", size=20, weight="bold"),
            ft.Text("En esta seccion podras registra tus gastos realizados", size=14),
            ft.Subtitle(content="Descripcion de gasto", size=20),
            ft.Row([
                ft.Column([
                    ft.ElevatedButton(content="Añadir gasto", bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE),
                    ft.ElevatedButton(content="Cambiar gasto", bgcolor=ft.Colors.BLUE_900, color=ft.Colors.WHITE),
                    ft.ElevatedButton(content="Eliminar gasto", bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE),
                ])
            ])
        ]
    )
    
    
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
            ft.ElevatedButton("Regresar al inicio", on_click=regresar, width=200, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.HOME, color=ft.Colors.WHITE, size=25))),
            gasto
        ],
        spacing=20,
    )