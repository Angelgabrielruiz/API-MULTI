import psycopg

class ChoferConnection:
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
                cur.execute("""SELECT * FROM "chofer" """)
                data = cur.fetchall()
            return data
        except Exception as e:
            print(f"Error al leer todos los choferes: {e}")
            return []

    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "chofer" WHERE id = %s""", (id,))
                data = cur.fetchone()
            return data
        except Exception as e:
            print(f"Error al leer un chofer: {e}")
            return None

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""INSERT INTO "chofer" (nombre) VALUES (%(nombre)s)""", data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al insertar un chofer: {e}")
            self.conn.rollback()

    def delete(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""DELETE FROM "chofer" WHERE id = %s""", (id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar un chofer: {e}")
            self.conn.rollback()

    def update(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""UPDATE "chofer" SET nombre = %(nombre)s WHERE id = %(id)s""", data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar un chofer: {e}")
            self.conn.rollback()

    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada exitosamente.")
