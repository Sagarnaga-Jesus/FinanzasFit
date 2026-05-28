from models.GastoModel import GastoModel

class GastoController:
    def __init__(self):
        self.model = GastoModel()
        
    def guardar_gasto(self, titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario):
        gasto = self.model.agregar_gasto(titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario)
        gasto = self.model.restar_gasto(gasto_aprox, id_usuario)
#        gasto = self.model.modificar_gasto( cantidad, descripcion)

    def restar_gasto(self, id_gasto, gasto_aprox, id_usuario):
        restar_gasto = self.model.restar_gasto(id_gasto, gasto_aprox, id_usuario)
        
    def modificar_gasto(self, id_gasto, cantidad, titulo, descripcion):
        pass