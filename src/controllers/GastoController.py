from models.GastoModel import GastoModel
from models.schemasModel import GastoShema
from pydantic import ValidationError

class GastoController:
    def __init__(self):
        self.model = GastoModel()
    
    def obtener_gastos(self, id_usuario):
        gasto=self.model.obtener_gasto(id_usuario)
        return gasto
        
    def guardar_gasto(self, titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario):
        try:
            GastoShema(titulo=titulo, descripcion=descripcion, tipo_gasto=tipo_gasto, gasto_aprox=gasto_aprox)
            
            gasto = self.model.agregar_gasto(titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario)
            
            if gasto:
                self.model.restar_gasto(gasto_aprox, id_usuario)
                return True, "Gasto agregado a lista"
            
        except ValidationError as e:
            return False, str(e)
        
        

    def eliminar_gasto(self,id_gasto, id_usuario, cantidad,):
        eliminar=self.model.eliminar_gasto(id_gasto, cantidad, id_usuario)
        
        return eliminar
    
    def confirmar_gasto(self, id_gasto, id_usuario):
        confirmar = self.model.confirmar_gasto(id_gasto, id_usuario)
        return confirmar

    def restar_gasto(self, gasto_aprox, id_usuario):
        self.model.restar_gasto(gasto_aprox, id_usuario)

# No se si te sirva asi o me equivoque jaja        
    def modificar_gasto(self, id_gasto, cantidad, titulo, descripcion, tipo_gasto ,id_usuario):
        try:
            GastoShema(titulo=titulo, descripcion=descripcion, tipo_gasto=tipo_gasto, gasto_aprox=cantidad)
        
            modifi = self.model.modificar_gasto(id_gasto, cantidad, titulo, descripcion, id_usuario)
            if modifi:
                return True, "Gasto modificado"
        except ValidationError as e:
            return False, str(e)