import psycopg

class TarjetaConnection:
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
                cur.execute("""SELECT * FROM "tarjeta" """)
                data = cur.fetchall()
            return data
        except Exception as e:
            print(f"Error al leer todas las tarjetas: {e}")
            return []

    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "tarjeta" WHERE id = %s""", (id,))
                data = cur.fetchone()
            return data
        except Exception as e:
            print(f"Error al leer una tarjeta: {e}")
            return None

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO "tarjeta" (nombre, num_tarjeta, fecha_expiracion, cvc) 
                    VALUES (%(nombre)s, %(num_tarjeta)s, %(fecha_expiracion)s, %(cvc)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al insertar una tarjeta: {e}")
            self.conn.rollback()

    def delete(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""DELETE FROM "tarjeta" WHERE id = %s""", (id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar una tarjeta: {e}")
            self.conn.rollback()

    def update(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE "tarjeta" 
                    SET nombre = %(nombre)s, num_tarjeta = %(num_tarjeta)s, fecha_expiracion = %(fecha_expiracion)s, cvc = %(cvc)s 
                    WHERE id = %(id)s
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar una tarjeta: {e}")
            self.conn.rollback()

    def close(self):
        """Cierra la conexión de manera segura"""
        if self.conn:
            self.conn.close()
            print("Conexión cerrada exitosamente.")
