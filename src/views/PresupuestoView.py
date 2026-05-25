import flet as ft

def PresupuestoView(page, controller):
    user = page.user_data
    
    dinero = ft.TextField(label="Ingreso de dinero", width=200)
    total_text = ft.Text(f"Total guardado: {controller.consultar_total(user['id_usuario'])}")

    def guardar(e):
        if dinero.value:
            try:
                cantidad = float(dinero.value)
                controller.guardar_presupuesto(cantidad, user["id_usuario"])
                total_text.value = f"Total guardado: {controller.consultar_total(user['id_usuario'])}"
                page.update()
            except ValueError:
                page.snack_bar = ft.SnackBar(ft.Text("Por favor ingresa un número válido"))
                page.snack_bar.open = True
                page.update()

    agregar = ft.IconButton(
        ft.Icons.ADD,
        tooltip="Agregar",
        bgcolor=ft.Colors.GREEN,
        on_click=guardar
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
            width=400,
            height=200,
            padding=10,
        )
    )

    return ft.View(
        route="/presupuesto",
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="#B8FF9C",
        appbar=ft.AppBar(
            title=ft.Text("Mi presupuesto"),
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
            ft.Row([dinero, agregar], spacing=20),
            ft.Divider(),
            card_dinero
        ]
    )