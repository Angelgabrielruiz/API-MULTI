import psycopg
from typing import Optional

class ColectivoConnection:
    conn = None

    def __init__(self):
        try:
            # Establece la conexión a la base de datos
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
                cur.execute("""INSERT INTO "colectivo" (asientos, ubicacion, num_serie) 
                               VALUES (%(asientos)s, %(ubicacion)s, %(num_serie)s)""", data)
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
                               SET asientos = %(asientos)s, ubicacion = %(ubicacion)s, num_serie = %(num_serie)s 
                               WHERE id = %(id)s""", data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar un colectivo: {e}")
            self.conn.rollback()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada exitosamente.")
