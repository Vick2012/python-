import mysql.connector

# Clase Heroe
class Heroe:
    def __init__(self, nombre: str, codigo: str, fuerza: int, destreza: int, inteligencia: int):
        self.nombre = nombre
        self.codigo = codigo
        self.fuerza = fuerza
        self.destreza = destreza
        self.inteligencia = inteligencia

    def _str_(self):
        return f"Heroe({self.nombre}, {self.codigo}, F:{self.fuerza}, D:{self.destreza}, I:{self.inteligencia})"

# Función para conectar a MySQL
def conectar_mysql():
    try:
        conexion = mysql.connector.connect(
            host="viaduct.proxy.rlwy.net",
            user="root",
            password="hIJsSmBtQqPhSnMVTaraiLXeLqJIwlPc",
            database="railway",
            port=16537
        )
        print("✅ Conexión a MySQL exitosa.")
        return conexion
    except mysql.connector.Error as e:
        print(f"❌ Error de conexión: {e}")
        return None

# Función para guardar un héroe en MySQL
def guardar_heroe(heroe):
    """
    Guarda un héroe en la base de datos MySQL y notifica en la terminal.
    """
    conexion = conectar_mysql()
    if conexion is None:
        print("⛔ No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conexion.cursor()
        
        # Insertar datos en la tabla
        cursor.execute("""
            INSERT INTO heroes (nombre, codigo, fuerza, destreza, inteligencia)
            VALUES (%s, %s, %s, %s, %s);
        """, (heroe.nombre, heroe.codigo, heroe.fuerza, heroe.destreza, heroe.inteligencia))

        conexion.commit()
        print(f"✅ Héroe '{heroe.nombre}' guardado con éxito en la base de datos.")

    except mysql.connector.IntegrityError:
        print("⚠ Error: El código del héroe ya existe en la base de datos.")
    except Exception as e:
        print(f"❌ Error al guardar el héroe: {e}")
    finally:
        cursor.close()
        conexion.close()

# Código principal
if __name__ == "__main__":
    print("🔄 Intentando conectar con MySQL...")

    # Crear un héroe de prueba
    heroe = Heroe("Victor Alfonso Alarcón", "2012", 100, 90, 85)

    # Guardar en MySQL
    guardar_heroe(heroe)