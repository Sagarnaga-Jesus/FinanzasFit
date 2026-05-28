import flet as ft
from datetime import datetime
import shutil
import os

def GastosView(page, gasto_controller):
    user = page.user_data
    usuario = user['id_usuario']       
    
    lista_gastos = ft.GridView(expand=True, max_extent=400, child_aspect_ratio=1.2, spacing=20, run_spacing=20)
    
    def  eliminar_gasto(g):
        gasto=gasto_controller.eliminar_gasto(g["id_gasto"], usuario, g["gasto_aprox"])
        if gasto:
            cargar_gastos()
            page.show_dialog(ft.SnackBar(ft.Text(gasto)))
    
    def cargar_gastos():
        lista_gastos.controls.clear()
        gastos=gasto_controller.obtener_gastos(usuario)
    
        for g in gastos:
            lista_gastos.controls.append(
                ft.Card(
                    width=520,
                    height=350,
                    content = ft.Container(
                        padding=15,
                        content = ft.Column([
                            ft.Text(g["titulo"], size=20, weight="bold"),
                            ft.Text(f"Descripcion: {g["descripcion"]}", size=20),
                            ft.Text(f"Dinero a gastar: {g["gasto_aprox"]}", size=20),
                                ft.Column([
                                    ft.Row(ft.ElevatedButton(content="Confirmar gasto", bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE,),alignment=ft.MainAxisAlignment.CENTER,)
                                    ,
                                    ft.Row(ft.ElevatedButton(content="Modificar gasto", bgcolor=ft.Colors.BLUE_900, color=ft.Colors.WHITE,),alignment=ft.MainAxisAlignment.CENTER,)
                                    ,
                                    ft.Row(ft.ElevatedButton(content="Eliminar gasto", on_click= lambda e, gasto=g: eliminar_gasto(gasto) , bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE,),alignment=ft.MainAxisAlignment.CENTER,)
                                    ,
                                ],alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=14)
                        ],horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        )
                    )
                )
            )
        page.update()
        
    cargar_gastos()
    
    def guardar(e):
        if not titulo.value.strip() or not descripcion.value.strip() or not tipo.value:
            page.show_dialog(ft.SnackBar(ft.Text("Todos los campos son obligatorios")))
            return
        
        if not gasto_aprox.value.strip():
            dinero=0
        else:
            dinero = float(gasto_aprox.value)
        
        gasto, msg = gasto_controller.guardar_gasto(titulo.value, descripcion.value, tipo.value, dinero, usuario)
        if gasto:
            page.show_dialog(ft.SnackBar(ft.Text(msg)))
            cargar_gastos()
            titulo.value = ""
            descripcion.value = ""
            gasto_aprox.value = ""
        

    titulo = ft.TextField(label="Titulo", bgcolor="white")
    descripcion = ft.TextField(label="Descripcion", bgcolor="white")
    tipo = ft.Dropdown(
        label="Tipo de gasto",
        width=400,
        filled=True,
        bgcolor=ft.Colors.WHITE,
        fill_color=ft.Colors.WHITE,
        options=[
            ft.dropdown.Option("Negocio"),
            ft.dropdown.Option("Hogar"),
            ft.dropdown.Option("Educativo"),
            ft.dropdown.Option("Familiar"),
            ft.dropdown.Option("Diario"),
            ft.dropdown.Option("Ahorro"),
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
            lista_gastos
        ],
        spacing=20,
    )