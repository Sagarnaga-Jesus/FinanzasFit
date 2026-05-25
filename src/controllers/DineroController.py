from models.DineroModel import DineroModel

class DineroController:
    def __init__(self):
        self.model = DineroModel()

    def guardar_presupuesto(self, cantidad, id_usuario):
        self.model.agregar_presupuesto(cantidad, id_usuario)

    def consultar_total(self, id_usuario):
        return self.model.obtener_total(id_usuario)
