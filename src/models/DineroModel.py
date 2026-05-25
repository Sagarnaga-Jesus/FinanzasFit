
from models.databaseModel import Database

class DineroModel:
    def __init__(self):
        self.db = Database()

    def agregar_presupuesto(self, cantidad, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO dinero (presupuesto, id_usuario) VALUES (%s, %s)",
            (cantidad, id_usuario)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def obtener_total(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT SUM(presupuesto) FROM dinero WHERE id_usuario=%s",
            (id_usuario,)
        )
        total = cursor.fetchone()[0] or 0
        cursor.close()
        conn.close()
        return total
