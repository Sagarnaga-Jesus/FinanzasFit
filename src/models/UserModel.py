import bcrypt
from models.databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()
    
    def registrar(self, usuario_data):
        salt = bcrypt.gensalt()
        hashed_pw = bcrypt.hashpw(
            usuario_data.password.encode('utf-8'),
            salt
        )
        
        conn= self.db.get_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email=%s",(usuario_data.email,))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return False
        
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, password, fecha_registro, foto) VALUES (%s, %s, %s, %s, %s)",
                (
                    usuario_data.nombre,
                    usuario_data.email,
                    hashed_pw.decode('utf-8'),
                    usuario_data.fecha,
                    usuario_data.foto
                )
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def modificar_perfil(self, id_usuario, nombre, foto):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            
            cursor.execute("UPDATE usuario SET nombre = %s WHERE id_usuario = %s", (nombre, id_usuario))
            cursor.execute("UPDATE usuario SET foto = %s WHERE id_usuario = %s", (foto, id_usuario))
            
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()
    
    def validar_login(self,email,password):
        conn = None
        cursor = None
        try:
            conn= self.db.get_connection()
            cursor=conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuario WHERE email=%s",(email,))
            user = cursor.fetchone()
            conn.close()
            
            if user and bcrypt.checkpw(password.encode('utf-8'),user['password'].encode('utf-8')):
                conn = self.db.get_connection()
                cursor = conn.cursor()
            
                cursor.execute(
                    "UPDATE usuario SET ultimo_registro = NOW() WHERE id_usuario = %s",
                    (user["id_usuario"],)
                )
                
                conn.commit()
                
                return user
            return None
        except Exception as err:
            print(f"Error: {err}")
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
            
    def existe_correo(self,correo):
        conn = None
        cursor = None
        
        try:
            conn= self.db.get_connection()
            cursor=conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuario WHERE email=%s",(correo,))
            user = cursor.fetchone()
            conn.close()
            if user:
                return True
            else:
                return False
            
        except Exception as err:
            print(f"Error: {err}")
            return False
        finally:
            if cursor: cursor.close()
            if conn: conn.close()
    
    def cambiar_password(self,password,correo):
        conn = None
        cursor = None
        
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(
            password.encode('utf-8'),
            salt
        )
        
        try:
            conn= self.db.get_connection()
            cursor=conn.cursor(dictionary=True)
            cursor.execute("UPDATE usuario SET password = %s WHERE email = %s", (hashed, correo))
            
            conn.commit()
            return True
        except Exception as err:
            print(f"Error: {err}")
            return False
        finally:
            if cursor:
                cursor.close()

            if conn:
                conn.close()