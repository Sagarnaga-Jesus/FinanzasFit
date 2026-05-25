from models.GastoModel import GastoModel

class GastoController:
    def __init__(self):
        self.model = GastoModel()
        
    def guardar_gasto(self, cantidad, descripcion, id_usuario):
        self.model.agregar_gasto(cantidad, descripcion, id_usuario)