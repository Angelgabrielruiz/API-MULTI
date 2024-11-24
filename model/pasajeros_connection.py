from fastapi import HTTPException
import psycopg

class PasajerosConnection:
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect("dbname=postgres user=multidiciplinario password=multi404 host=3.225.29.67 port=5432")
        except psycopg.OperationalError as err:
            print(f"Error al conectar a la base de datos: {err}")

    def read_all(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "pasajeros" """)
                data = cur.fetchall()
            return data
        except Exception as e:
            print(f"Error al leer todos los pasajeros: {e}")
            return []

    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "pasajeros" WHERE id = %s""", (id,))
                data = cur.fetchone()
            return data
        except Exception as e:
            print(f"Error al leer un pasajero: {e}")
            return None
        
    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO "pasajeros" (name, origen, destino, colectivo_id, chofer_id) 
                    VALUES (%(name)s, %(origen)s, %(destino)s, %(colectivo_id)s, %(chofer_id)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al insertar un pasajero: {e}")
            self.conn.rollback()

    def delete(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""DELETE FROM "pasajeros" WHERE id = %s""", (id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar un pasajero: {e}")
            self.conn.rollback()

    def update(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE "pasajeros" 
                    SET name = %(name)s, origen = %(origen)s, destino = %(destino)s, 
                         colectivo_id = %(colectivo_id)s, chofer_id = %(chofer_id)s 
                    WHERE id = %(id)s
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar un pasajero: {e}")
            self.conn.rollback()
            
    def read_last(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "pasajeros" ORDER BY id DESC LIMIT 1""")
                data = cur.fetchone()
            return data
        except Exception as e:
            print(f"Error al leer el último pasajero: {e}")
            return None

    
    def close(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada exitosamente.")
