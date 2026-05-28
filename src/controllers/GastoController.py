from models.GastoModel import GastoModel

class GastoController:
    def __init__(self):
        self.model = GastoModel()
    
    def obtener_gastos(self, id_usuario):
        gasto=self.model.obtener_gasto(id_usuario)
        return gasto
        
    def guardar_gasto(self, titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario):
        gasto = self.model.agregar_gasto(titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario)
        gasto = self.model.restar_gasto(gasto_aprox, id_usuario)
        return gasto
#        gasto = self.model.modificar_gasto( cantidad, descripcion)
    def eliminar_gasto(self,id_gasto, cantidad, id_usuario):
        eliminar=self.model.eliminar_gasto(id_gasto, cantidad, id_usuario)
        
        return eliminar

    def restar_gasto(self, id_gasto, gasto_aprox, id_usuario):
        restar_gasto = self.model.restar_gasto(id_gasto, gasto_aprox, id_usuario)
        
    def modificar_gasto(self, id_gasto, cantidad, titulo, descripcion):
        pass