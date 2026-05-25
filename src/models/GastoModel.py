from models.databaseModel import Database

class GastoModel:
    def __init__(self):
        self.db = Database()

    def agregar_gasto(self, cantidad, descripcion, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO gastos (cantidad, descripcion, id_usuario) VALUES (%s, %s, %s)",
            (cantidad, descripcion, id_usuario)
        )
        conn.commit()
        cursor.close()
        conn.close()