import flet as ft
from datetime import datetime
import shutil
import os
logo = ft.Image(src="assets/FinanzasFit.png", width = 100, height = 100, border_radius = 100)

def RegistroView(page: ft.Page, auth_controller):
    
    def ver_contra():
        contra.password = not contra.password
        contra.update()
        
    correo=(ft.TextField(label="Correo",autofocus=True, icon=ft.Icons.PERSON ))
    contra=(ft.TextField(label="Contraseña",suffix=ft.IconButton(icon=ft.Icons.VISIBILITY, on_click=ver_contra) ,password=True, autofocus=True, icon=ft.Icons.PASSWORD))
    nombre=(ft.TextField(label="Nombre",icon=ft.Icons.BADGE))
    
    
    async def seleccionar_archivo(e):

        archivos = await file_picker.pick_files(
            allow_multiple=False
        )
        
        if archivos:
            archivo = archivos[0]
            
            page.foto_name = archivo.name
            page.foto_path = archivo.path
            print(archivo.name)
            print(archivo.path)

    file_picker = ft.FilePicker()

    boton = ft.ElevatedButton(
        "Seleccionar archivo",
        on_click=seleccionar_archivo,
        color=ft.Colors.GREEN,
        height=40,
        width=200,
    )
    
    

    def registra(e):
        if not correo.value and not contra.value and not nombre.value:
            page.show_dialog(ft.SnackBar(ft.Text("Por favor, complete todos los campos"), bgcolor=ft.Colors.RED))
            return
        
        nombre_foto = "Default.webp"
        
        if hasattr(page, "foto_path"):
            destino = os.path.join(
                    "assets",
                    page.foto_name
                )
    
            shutil.copy(
                page.foto_path,
                destino
            )
            
            nombre_foto = page.foto_name
        
        hoy = datetime.now()
        fecha = hoy.strftime("%Y-%m-%d %H:%M:%S")
        
        user, msg = auth_controller.registrar_Usuario(nombre.value, correo.value, contra.value, fecha, nombre_foto)
        
        if user:
            page.go("/")
            page.show_dialog(ft.SnackBar(ft.Text(msg), bgcolor=ft.Colors.GREEN))
        else:
            page.show_dialog(ft.SnackBar(ft.Text(msg), bgcolor=ft.Colors.RED))
    
    registrar =( ft.ElevatedButton("Registrase",color=ft.Colors.BLUE, on_click=registra, height=40, width=200))
    def regresar():
        page.go("/")
        
    reversa = ( ft.ElevatedButton("Regresar a login",color=ft.Colors.RED ,on_click=regresar, height=40, width=200))
    
    return ft.View(
        route="/registro",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = "#B8FF9C",
        appbar=ft.AppBar(
            title=ft.Text("Registro"),
            bgcolor="#000000",
            color="#1AC91A",
        ),
        controls=[
            ft.Column(
                [
#                    logo,
                    ft.Icon(ft.Icons.ACCOUNT_BOX, size=80, color=ft.Colors.BLACK),
                    ft.Text("Registro de usuario", size=30, weight="bold"),
                    nombre,
                    correo,
                    contra,
                    boton,
                    registrar,
                    reversa
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ]
    )
    