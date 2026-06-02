import flet as ft
from datetime import datetime

def GastosView(page, gasto_controller,controller):
    user = page.user_data
    usuario = user['id_usuario']       
    
    
    dinero = ft.TextField(label="Ingreso de dinero", width=200)
    dinero_quitar = ft.TextField(label="Quitar dinero", width=200)
    total_text = ft.Text(f"Total disponible: {controller.consultar_total(usuario)}", size=14, weight="bold")
    
    def actualizar_total(usuario):
        total_text.value = f"Total disponible: {controller.consultar_total(usuario)}"
        page.update()

    def guardar_presu(e):
        if dinero.value:
            try:
                cantidad = float(dinero.value)
                controller.guardar_presupuesto(cantidad, user["id_usuario"])
                actualizar_total(user["id_usuario"])
                dinero.value = ""
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text("Por favor ingresa un número válido"))
                page.snack_bar.open = True
                page.update()
    
    def guardar2(e):
        if dinero_quitar.value:
            try:
                cantidad = float(dinero_quitar.value)
                controller.restar_presupuesto(cantidad, user["id_usuario"])
                actualizar_total(user["id_usuario"])
                dinero_quitar.value = ""
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text("Por favor ingresa un número válido"))
                page.snack_bar.open = True
                page.update()

    agregar_presupuesto = ft.IconButton(
        ft.Icons.ADD,
        tooltip="Agregar",
        bgcolor=ft.Colors.GREEN,
        on_click=guardar_presu
    )
    
    agregar_2 = ft.IconButton(
        ft.Icons.ADD,
        tooltip="Agregar",
        bgcolor=ft.Colors.GREEN,
        on_click=guardar2
    )

    card_dinero = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("Dinero", size=20, weight="bold"),
                    total_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10
            ),
            width=260,
            height=100,
            padding=15,
        )
    )
    
    #Aqui inicia gastos
    
    lista_gastos = ft.GridView(expand=True, max_extent=400, child_aspect_ratio=1.2, spacing=40, run_spacing=30)
    

    
    def confirmar_gasto(g):
        gasto = gasto_controller.confirmar_gasto(g["id_gasto"],usuario)
        if gasto:
            actualizar_total(user["id_usuario"])
            cargar_gastos()
            page.show_dialog(ft.SnackBar(ft.Text(gasto)))
    
    def  eliminar_gasto(g):
        gasto=gasto_controller.eliminar_gasto(g["id_gasto"], usuario, g["gasto_aprox"])
        if gasto:
            actualizar_total(user["id_usuario"])
            cargar_gastos()
            page.show_dialog(ft.SnackBar(ft.Text(gasto)))
            
    
    def cargar_gastos():
        lista_gastos.controls.clear()
        gastos=gasto_controller.obtener_gastos(usuario)
        
    
        for g in gastos:
            lista_gastos.controls.append(
                ft.Card(
                    width=400,
                    height=300,
                    shadow_color=ft.Colors.BLACK_87,
                    elevation=20,
                    shape=ft.RoundedRectangleBorder(radius=12),
                    
                    content = ft.Container(
                        padding=15,
                        content = ft.Column([
                            ft.Text(g["titulo"], size=20, weight="bold"),
                            ft.Text(f"Descripcion: {g['descripcion']}", size=20),
                            ft.Text(f"Dinero a gastar: {g['gasto_aprox']}", size=20),
                                ft.Column([
                                    ft.Row(ft.ElevatedButton(content="Confirmar gasto", on_click= lambda e, gasto=g: confirmar_gasto(gasto), bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE,),alignment=ft.MainAxisAlignment.CENTER,)
                                    ,
                                    ft.Row(ft.ElevatedButton(content="Modificar gasto", bgcolor=ft.Colors.BLUE_900, on_click=lambda e, gasto=g: modificar_gasto(gasto), color=ft.Colors.WHITE,),alignment=ft.MainAxisAlignment.CENTER,)
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
            actualizar_total(user["id_usuario"])
            cargar_gastos()
            titulo.value = ""
            descripcion.value = ""
            gasto_aprox.value = ""
            page.update()
        

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
    


    def modificar_gasto(g):
        titulo_edit = ft.TextField(value=g["titulo"])
        descripcion_edit = ft.TextField(value=g["descripcion"])
        gasto_edit = ft.TextField(value=str(g["gasto_aprox"]))
        tipo_edit = ft.Dropdown(
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
        def cerrar(e):
            modi.open = False
            page.update()

        modi = ft.AlertDialog(
                title=ft.Text("Modificar gasto"),
                content=ft.Column([
                    titulo_edit,
                    descripcion_edit,
                    gasto_edit,
                    tipo_edit
                ], spacing=10),
                actions=[
                    ft.ElevatedButton("Guardar", on_click=lambda e: guardar_modificacion(g)),
                    ft.ElevatedButton("Cancelar", on_click=cerrar)
                ],
            )
        page.overlay.append(modi) 
        modi.open = True
        page.update()
        
    
        def guardar_modificacion(g):
            if not titulo_edit.value.strip() or not descripcion_edit.value.strip() or not tipo_edit.value:
                page.show_dialog(ft.SnackBar(ft.Text("Todos los campos son obligatorios")))
                return
            
            if not gasto_aprox.value.strip():
                dinero=0
            else:
                dinero = float(gasto_aprox.value)
            
            gasto_controller.modificar_gasto(g["id_gasto"], dinero, titulo.value, descripcion.value)
            page.show_dialog(ft.SnackBar(ft.Text("Gasto modificado")))
            actualizar_total(user["id_usuario"])
            cargar_gastos()
            modi.open = False
            page.update()
    
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
                ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _:page.go("/"), tooltip="Cerrar sesión"),
            ],
        ),
        controls=[
            ft.Row([
                ft.Column([
                    ft.Row([dinero, agregar_presupuesto,])
                    ]),
                ft.Column([
                    ft.Row([dinero_quitar, agregar_2,]),
                    ]),
                ft.Column([card_dinero]),
                ],alignment=ft.MainAxisAlignment.SPACE_BETWEEN,spacing=20),
            ft.Divider(height=4, thickness=4, color=ft.Colors.BLACK),
            formulario,
            ft.Divider(height=4, thickness=4, color=ft.Colors.BLACK),
            lista_gastos
        ],
        spacing=20,
    )