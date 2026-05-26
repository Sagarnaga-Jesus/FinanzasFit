import flet as ft
from datetime import datetime
import shutil
import os

def GastosView(page, GastoController):
    user = page.user_data
    
    lista_gastos = ft.GridView(expand=True, max_extent=350, child_aspect_ratio=1.2, spacing=20, run_spacing=20)
    
    def guardar(e):
        cantidad = gasto_aprox.value
        descripcion = f"{titulo.value} - {descripcion.value} - {tipo.value} - {gasto_aprox.value}"
        usuario = user['id_usuario']        
        GastoController.guardar_gasto(titulo.value, descripcion.value, tipo.value, gasto_aprox.value, id_usuario.value)
        


        
    
    titulo = ft.TextField(label="Titulo", bgcolor="white")
    descripcion = ft.TextField(label="Descripcion", bgcolor="white")
    tipo = ft.Dropdown(
        label="Tipo de gasto",
        width=400,
        bgcolor="white",
        options=[
            ft.dropdown.Option("Negocio"),
            ft.dropdown.Option("Hogar"),
            ft.dropdown.Option("Educativo"),
            ft.dropdown.Option("Familiar"),
            ft.dropdown.Option("Diario"),
            ft.dropdown.Option("Otro"),
        ]
    )
    gasto_aprox = ft.TextField(label="Dinero a utilizar", bgcolor="white")
    agregar = ft.IconButton(ft.Icons.ADD_BOX, on_click=guardar, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), color="BLACK"), icon_size=40, tooltip="Agregar unidad")
    
    formulario = ft.Row([
                    ft.Column([
                        ft.Row([
                            ft.Text("Añadir nuevo gasto", size=18, weight="bold", color="black"),
                            titulo, agregar
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                        ft.Row([
                            descripcion, tipo, gasto_aprox
                            ]),
                            
                    ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER,),
                    
                ], alignment=ft.MainAxisAlignment.CENTER,)
        
    gasto = ft.Card(
        width=520,
        height=250,
        content = ft.Container(
            padding=15,
            content = ft.Column([
                ft.Text("titulo del gasto", size=20, weight="bold"),
                ft.Text("Descripcion de gasto", size=20),
                    ft.Row([
                        ft.ElevatedButton(content="Confirmar gasto", bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE),
                        ft.ElevatedButton(content="Modificar gasto", bgcolor=ft.Colors.BLUE_900, color=ft.Colors.WHITE),
                        ft.ElevatedButton(content="Eliminar gasto", bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE),
                    ],alignment=ft.MainAxisAlignment.CENTER, spacing=10)
            ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    )
    
    return ft.View(
        route="/gastos",
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
            formulario,
            ft.Divider(height=4, thickness=4, color=ft.Colors.BLACK),
            gasto
        ],
        spacing=20,
    )