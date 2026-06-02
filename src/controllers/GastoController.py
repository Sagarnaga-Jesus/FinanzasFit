from models.GastoModel import GastoModel

class GastoController:
    def __init__(self):
        self.model = GastoModel()
    
    def obtener_gastos(self, id_usuario):
        gasto=self.model.obtener_gasto(id_usuario)
        return gasto
        
    def guardar_gasto(self, titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario):
        gasto = self.model.agregar_gasto(titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario)
        if gasto:
            resta = self.model.restar_gasto(gasto_aprox, id_usuario)
            
            return True, "Gasto agregado a lista"

    def eliminar_gasto(self,id_gasto, id_usuario, cantidad,):
        eliminar=self.model.eliminar_gasto(id_gasto, cantidad, id_usuario)
        
        return eliminar
    
    def confirmar_gasto(self, id_gasto, id_usuario):
        confirmar = self.model.confirmar_gasto(id_gasto, id_usuario)
        return confirmar

    def restar_gasto(self, id_gasto, gasto_aprox, id_usuario):
        restar_gasto = self.model.restar_gasto(id_gasto, gasto_aprox, id_usuario)

# No se si te sirva asi o me equivoque jaja        
    def modificar_gasto(self, id_gasto, cantidad, titulo, descripcion):
        modifi = self.model.modificar_gasto(id_gasto, cantidad, titulo, descripcion)
        return modifi