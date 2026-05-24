import flet as ft

logo = ft.Image(src="assets/FinanzasFit.png", width = 200, height = 200, border_radius = 100)

def InicioView(page):
    
    def cerrar_sesion(e):
        page.go("/")
        
    def ir_perfil(e):
        page.go("/perfil")
    
    def ir_presupuesto():
        page.go("/presupuesto")
        
    def ir_gastos():
        page.go("/gastos")
        
    inicio=  ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Divider(color=ft.Colors.BLACK, thickness=2, height=20),
                    logo,
                    ft.Text(f"Bienvenido, {page.user_data['nombre']}!", size=24, weight="bold", color="#12852E", text_align=ft.TextAlign.CENTER),
                    ft.Divider(color=ft.Colors.BLACK, thickness=2, height=20),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                ),
                width=400,
                height=350,
            )
        )
    
    intro= ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Divider(color=ft.Colors.BLACK, thickness=2, height=20),
                    ft.Text("Tu compañero para una vida financiera mas comoda y segura", size=20, color="#12852E", text_align=ft.TextAlign.CENTER),
                    ft.Text("Comienza a gestionar tu dinero de manera inteligente y alcanza tus metas financieras", size=20, color="#12852E", text_align=ft.TextAlign.CENTER),
                    ft.Divider(color=ft.Colors.BLACK, thickness=2, height=20),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10.
                ),
                width=400,
                height=350,
                padding=10,
            )
        )
        
    return ft.View(
        route="/inicio",
        vertical_alignment=ft.MainAxisAlignment.CENTER, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor = "#B8FF9C",
        appbar=ft.AppBar(
            title=ft.Text(f"Bienvenido a FinanzasFit, {page.user_data['nombre']}!", size=20),
            bgcolor="#000000",
            color="#1AC91A",
            actions=[
                    ft.IconButton(ft.Icons.ACCOUNT_CIRCLE, on_click=ir_perfil, tooltip="Perfil"),
                    ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=cerrar_sesion,tooltip="Cerrar sesión")
                ],
        ),
        controls=[
            ft.Row(
                [
                    inicio,
                    intro
                ],
            alignment=ft.MainAxisAlignment.CENTER, 
            )
        ]
    )