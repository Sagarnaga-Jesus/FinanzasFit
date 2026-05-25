
from models.databaseModel import Database

class DineroModel:
    def __init__(self):
        self.db = Database()

    def agregar_presupuesto(self, cantidad, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT presupuesto FROM dinero WHERE id_usuario=%s LIMIT 1",
            (id_usuario,)
        )
        resultado = cursor.fetchone()
    
        if resultado:  
            cursor.execute(
                "UPDATE dinero SET presupuesto = presupuesto + %s WHERE id_usuario =%s",
                (cantidad, id_usuario)
            )
        else:
            cursor.execute(
                "INSERT INTO dinero (presupuesto, id_usuario) VALUES (%s, %s)",
                (cantidad, id_usuario)
            )
    
        conn.commit()
        cursor.close()
        conn.close()
        
    def resta_presupuesto(self, cantidad, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE dinero SET presupuesto = presupuesto - %s WHERE id_usuario =%s",
            (cantidad, id_usuario)
        )
        conn.commit()
        cursor.close()
        conn.close()
    
    

    def obtener_total(self, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT presupuesto FROM dinero WHERE id_usuario=%s",
            (id_usuario,)
        )
        presupuesto = cursor.fetchone()
        cursor.close()
        conn.close()
        return presupuesto
