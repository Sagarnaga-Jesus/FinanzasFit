from models.GastoModel import GastoModel

class GastoController:
    def __init__(self):
        self.model = GastoModel()
        
    def guardar_gasto(self, cantidad, descripcion, tipo, gasto_aprox, id_usuario):
        gasto = self.model.agregar_gasto(cantidad, descripcion, id_usuario)
        return gasto
#        gasto = self.model.restar_gasto(cantidad, id_usuario)
#        gasto = self.model.modificar_gasto( cantidad, descripcion)

    def restar_gasto(self, cantidad, id_usuario):
        pass
    def modificar_gasto(self, id_gasto, cantidad, titulo, descripcion):
        pass