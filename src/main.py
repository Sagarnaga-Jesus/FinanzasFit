import flet as ft
from views.LoginView import LoginView
from views.RegistroView import RegistroView
from views.InicioView import InicioView
from views.OlvidadoView import OlvidadoView
from views.PerfilView import PerfilView,ModificarView
from views.GastosView import GastosView
from views.PresupuestoView import PresupuestoView
from controllers.UserController import AuthController
from controllers.DineroController import DineroController

#The is Admin#08

def start(page: ft.Page):
    page.title = "Finanzas Fit"
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 450
    page.window_height = 700
    
    auth = AuthController()
    dinero = DineroController()
    
    def route_change(e):
        page.views.clear()
        
        if page.route == "/":
            page.views.append(LoginView(page,auth))
        elif page.route == "/registro":
            page.views.append(RegistroView(page,auth))
        elif page.route == "/olvidado":
            page.views.append(OlvidadoView(page, auth))
        elif page.route == "/inicio":
            page.views.append(InicioView(page))
        elif page.route == "/perfil":
            page.views.append(PerfilView(page, auth))
        elif page.route == "/modificar":
            page.views.append(ModificarView(page, auth))
        elif page.route == "/gastos":
            page.views.append(GastosView(page))
        elif page.route == "/presupuesto":
            page.views.append(PresupuestoView(page,dinero))
        page.update()

    def view_pop(e):
        if len(page.views) > 1:
            page.views.pop()
            page.update()
            top_view = page.views[-1]
            page.go(top_view.route)
    
    #Manejos de eventos
    page.on_route_change = route_change
    page.on_view_pop = view_pop
    
    if page.route == "/":
        route_change(None)
    else:
        page.go("/")
    
def main ():
    ft.app(start)
    
if __name__ == "__main__":
    main()