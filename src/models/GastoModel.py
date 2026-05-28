from models.databaseModel import Database

class GastoModel:
    def __init__(self):
        self.db = Database()

    def agregar_gasto(self, titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO gastos (titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario) VALUES (%s, %s, %s, %s, %s)",
            (titulo, descripcion, tipo_gasto, gasto_aprox, id_usuario)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
    def restar_gasto(self, gasto_aprox, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE dinero SET presupuesto = presupuesto - %s WHERE id_usuario =%s",
            (gasto_aprox, id_usuario)
        )

        conn.commit()
        cursor.close()
        conn.close()
        
    def modificar_gasto(self, id_gasto, cantidad, titulo, descripcion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE gastos SET cantidad = %s,titulo = %s, descripcion = %s WHERE id_gasto = %s",
            (cantidad, titulo, descripcion, id_gasto)
        )
        conn.commit()
        cursor.close()
        conn.close()
    