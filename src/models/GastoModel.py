from models.databaseModel import Database

class GastoModel:
    def __init__(self):
        self.db = Database()
        
    def obtener_gasto(self,id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        
        try:
            cursor.execute("SELECT * FROM gastos WHERE id_usuario = %s", (id_usuario,))
            gastos = cursor.fetchall()
            return gastos
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            conn.commit()
            cursor.close()
            conn.close()
    
    def confirmar_gasto(self, id_gasto, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            
            cursor.execute("DELETE FROM gastos WHERE id_gasto = %s", (id_gasto,))
            return "Gasto confirmado"
        except Exception as e:
            return f"Error al confirmar gasto: {e}"
        finally:
            conn.commit()
            cursor.close()
            conn.close()
    
    def eliminar_gasto(self,id_gasto, gasto_aprox, id_usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        gasto_aprox = float(gasto_aprox)
        
        try:
            cursor.execute(
            "UPDATE dinero SET presupuesto = presupuesto + %s WHERE id_usuario = %s",
            (gasto_aprox, id_usuario)
        )
            cursor.execute("DELETE FROM gastos WHERE id_gasto = %s", (id_gasto,))
            return "Gasto eliminado"
        except Exception as e:
            return f"Error al eliminar gasto: {e}"
        finally:
            conn.commit()
            cursor.close()
            conn.close()
    
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
        return True
    
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
        
    def modificar_gasto(self, id_gasto, gasto_aprox, titulo, descripcion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE gastos SET gasto_aprox = %s, titulo = %s, descripcion = %s WHERE id_gasto = %s",
            (gasto_aprox, titulo, descripcion, id_gasto)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return "Gasto modificado"
