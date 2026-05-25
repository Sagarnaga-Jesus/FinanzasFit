import flet as ft
import shutil
import os

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
    
    modificar_btn = ft.ElevatedButton("Modificar Perfil", on_click=lambda _: page.go("/modificar"))
    
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
            modificar_btn,
            ft.ElevatedButton("Regresar al inicio", on_click=regresar, width=200, bgcolor="cyan", color = "black", icon=(ft.Icon(ft.Icons.HOME, color=ft.Colors.WHITE, size=25)))
        ],
        spacing=20,
    )

def ModificarView(page, AuthController):
    user = page.user_data
    async def seleccionar_archivo(e):

        archivos = await file_picker.pick_files(
            allow_multiple=False
        )

        if archivos:
            archivo = archivos[0]
            
            
            page.foto_nueva_path = archivo.path
            page.foto_nueva_name = archivo.name

    file_picker = ft.FilePicker()

    boton = ft.ElevatedButton(
        "Seleccionar archivo",
        on_click=seleccionar_archivo
    )
    
    def guardar_cambios(e):
        if not nombre_nuevo.value:
            page.show_dialog(ft.SnackBar(ft.Text("Complete los campos")))
            return False
            
        else:
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
            
            success= AuthController.modificar(
                user['id_usuario'],
                nombre_nuevo.value,
                nombre_foto
            )
            if success:
                page.show_dialog(ft.SnackBar(ft.Text("Perfil actualizado correctamente")))
                user['nombre'] = nombre_nuevo.value
                user['foto'] = page.foto_nueva_name

                page.user_data = user
                page.go("/perfil")
                page.update()
            else:
                page.show_dialog(ft.SnackBar(ft.Text("Error al actualizar perfil")))
    
    nombre_nuevo = ft.TextField(label="Nuevo Nombre", icon=ft.Icons.BADGE)
    guardar_btn = ft.ElevatedButton("Guardar Cambios", on_click=guardar_cambios)
    salir = ft.ElevatedButton("Salir", on_click=lambda _: page.go("/perfil"))
    
    return ft.View(
        route="/modificar",
        controls=[
            ft.Column(
                [
                    ft.Icon(ft.Icons.ACCOUNT_BOX, size=50, color=ft.Colors.BLUE),
                    ft.Text("Registro de usuario", size=30, weight="bold"),
                    ft.Row([nombre_nuevo,],ft.CrossAxisAlignment.CENTER,),
                    ft.Row([boton],ft.CrossAxisAlignment.CENTER,),
                    ft.Row([guardar_btn,salir],ft.CrossAxisAlignment.CENTER,),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                tight=True 
            )
        ])