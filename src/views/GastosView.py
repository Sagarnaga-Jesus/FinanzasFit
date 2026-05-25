import flet as ft
from datetime import datetime
import shutil
import os

def GastosView(page: ft.Page):
    user = page.user_data
    
    def guardar(e):
        pass
        
    gasto = ft.Card(
        content = ft.Container(
            padding=15,
            content = ft.Column([
            ft.Text("Gastos", size=20, weight="bold"),
            ft.Text("En esta seccion podras registrar tus gastos realizados", size=14),
            ft.Text("Descripcion de gasto", size=20),
            ft.TextField(label="Descripcion del gasto", width=300, multiline=True, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK),
            ft.Row([
                ft.Column([
                    ft.ElevatedButton(content="Añadir gasto", bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE),
                    ft.ElevatedButton(content="Cambiar gasto", bgcolor=ft.Colors.BLUE_900, color=ft.Colors.WHITE),
                    ft.ElevatedButton(content="Eliminar gasto", bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE),
                ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
                    )],
            elevation=5,
            margin=10,
            shape=ft.RoundedRectangleBorder(radius=12),)
        ]
    )))
    
    
    return ft.View(
        route="/gastos",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = "#B8FF9C",
        appbar=ft.AppBar(
            title=ft.Text("gastos realizados"),
            bgcolor="#000000",
            color="#1AC91A",
            actions=[
                ft.IconButton(ft.Icons.HOME, on_click=lambda _:page.go("/inicio"), tooltip="Inicio"),
                ft.IconButton(ft.Icons.ACCOUNT_CIRCLE, on_click=lambda _:page.go("/perfil"), tooltip="Perfil"),
                ft.IconButton(ft.Icons.MONEY, on_click=lambda _:page.go("/presupuesto"), tooltip="Consultar dinero"),
                ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _:page.go("/"), tooltip="Cerrar sesión"),
            ],
        ),
        controls=[
            gasto
        ],
        spacing=20,
    )