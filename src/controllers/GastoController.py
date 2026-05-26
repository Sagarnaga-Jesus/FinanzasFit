from models.GastoModel import GastoModel

class GastoController:
    def __init__(self):
        self.model = GastoModel()
        
    def guardar_gasto(self, cantidad, descripcion, tipo, gasto_aprox, id_usuario):
        self.model.agregar_gasto(cantidad, descripcion, id_usuario)
    
    def restar_gasto(self, cantidad, id_usuario):
        pass
    
    def consultar_gasto(self, cantidad, id_usuario):
        pass