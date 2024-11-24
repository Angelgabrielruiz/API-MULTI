import psycopg

class ReservasConnection:
    conn = None

    def __init__(self):
        try: 
            self.conn = psycopg.connect("dbname=postgres user=multidiciplinario password=multi404 host=3.225.29.67 port=5432")
        except psycopg.OperationalError as err:
            print(f"Error al conectar a la base de datos: {err}")

    def read_all(self):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "reservas" """)
                data = cur.fetchall()
            return data
        except Exception as e:
            print(f"Error al leer todas las reservas: {e}")
            return []

    def read_one(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""SELECT * FROM "reservas" WHERE id = %s""", (id,))
                data = cur.fetchone()
            return data
        except Exception as e:
            print(f"Error al leer una reserva: {e}")
            return None

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO "reservas" (fecha_reserva, forma_pago, monto, pasajero_id, cantidad) 
                    VALUES (%(fecha_reserva)s, %(forma_pago)s, %(monto)s, %(pasajero_id)s, %(cantidad)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al insertar una reserva: {e}")
            self.conn.rollback()

    def delete(self, id):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""DELETE FROM "reservas" WHERE id = %s""", (id,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar una reserva: {e}")
            self.conn.rollback()

    def update(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    UPDATE "reservas" 
                    SET fecha_reserva = %(fecha_reserva)s, forma_pago = %(forma_pago)s, monto = %(monto)s, pasajero_id = %(pasajero_id)s, cantidad = %(cantidad)s 
                    WHERE id = %(id)s
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar una reserva: {e}")
            self.conn.rollback()

    def close(self):
        """Cierra la conexión de manera segura"""
        if self.conn:
            self.conn.close()
            print("Conexión cerrada exitosamente.")
