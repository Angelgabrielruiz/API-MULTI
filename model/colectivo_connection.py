import psycopg
from typing import Optional

class ColectivoConnection:
    conn = None

    def __init__(self):
        try:
            
            self.conn = psycopg.connect("dbname=postgres user=multidiciplinario password=multi404 host=3.225.29.67 port=5432")
        except psycopg.OperationalError as err:
            print(f"Error al conectar a la base de datos: {err}")

    def read_all(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "colectivo" """)
                data = cur.fetchall()
            return data
        except Exception as e:
            print(f"Error al leer todos los colectivos: {e}")
            return []

    def read_one(self, id: int):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "colectivo" WHERE id = %s""", (id,))
                data = cur.fetchone()
            return data
        except Exception as e:
            print(f"Error al leer un colectivo: {e}")
            return None

    def write(self, data: dict):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""INSERT INTO "colectivo" (asientos, ubicacion, num_serie, fecha, horario) 
                               VALUES (%(asientos)s, %(ubicacion)s, %(num_serie)s, %(fecha)s, %(horario)s)""", data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al insertar un colectivo: {e}")
            self.conn.rollback()

    def delete(self, id: int):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""DELETE FROM "colectivo" WHERE id = %s""", (id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar un colectivo: {e}")
            self.conn.rollback()

    def update(self, data: dict):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""UPDATE "colectivo" 
                               SET asientos = %(asientos)s, ubicacion = %(ubicacion)s, num_serie = %(num_serie)s, fecha = %(fecha)s, horario = %(horario)s
                               WHERE id = %(id)s""", data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar un colectivo: {e}")
            self.conn.rollback()
            
            
    def update_asientos(self, id: int, asientos: int):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""UPDATE "colectivo" 
                               SET asientos = %s 
                               WHERE id = %s""", (asientos, id))
                self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar los asientos del colectivo: {e}")
            self.conn.rollback()
            
    
    def get_pasajeros_by_colectivo(self, colectivo_id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                SELECT id, name, origen, destino
                FROM "pasajeros"
                WHERE colectivo_id = %s
                """, (colectivo_id,))
                data = cur.fetchall()
            return data
        except Exception as e:
            print(f"Error al obtener pasajeros por colectivo: {e}")
            return []



    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada exitosamente.")
