# Importamos la librería sqlite3 para trabajar con bases de datos SQLite
import sqlite3

# Definimos la clase Heroe, que representa a un héroe con ciertos atributos.
class Heroe:
    def __init__(self, nombre: str, codigo: str, fuerza: int, destreza: int, inteligencia: int):
       
        # Constructor de la clase Heroe que inicializa los atributos del héroe.
        self.nombre = nombre
        self.codigo = codigo
        self.fuerza = fuerza
        self.destreza = destreza
        self.inteligencia = inteligencia

    def __str__(self):
        
        #Método que devuelve una representación en forma de cadena del héroe.
        #Esto permite imprimir un objeto Heroe de forma legible.
        
        return f"Heroe({self.nombre}, {self.codigo}, F:{self.fuerza}, D:{self.destreza}, I:{self.inteligencia})"


# Función para guardar un héroe en la base de datos SQLite
def guardar_heroe(heroe):
    """
    Función que inserta un héroe en la tabla 'heroes' de la base de datos.
    :param heroe: Objeto Heroe a guardar en la base de datos.
    """
    try:
        # Conectamos a la base de datos (se creará si no existe)
        conexion = sqlite3.connect("heroes2.sqlite")
        cursor = conexion.cursor()
        
        # Insertamos los datos del héroe en la tabla 'heroes'
        #INSERT INTO heroes (nombre, codigo, fuerza, destreza, inteligencia)VALUES (?, ?, ?, ?, ?);
        cursor.execute((heroe.nombre, heroe.codigo, heroe.fuerza, heroe.destreza, heroe.inteligencia))

        # Confirmamos que los cambios se guarden en la base de datos
        conexion.commit()
        print(f"Héroe '{heroe.nombre}' guardado con éxito.")

    except sqlite3.IntegrityError:
        # Si ocurre un error de integridad (por ejemplo, si el código ya existe), mostramos un mensaje
        print("Error: El código del héroe ya existe en la base de datos.")
    except Exception as e:
        # Si ocurre cualquier otro error, lo mostramos
        print("Error al guardar el héroe:", e)
    finally:
        # Cerramos la conexión y el cursor para liberar recursos
        cursor.close()
        conexion.close()

# Función para crear la base de datos y la tabla 'heroes' si no existen
def crear_db():
   
    #Función que crea la base de datos y la tabla 'heroes' si no existen.
  
    # Conectamos a la base de datos (se creará si no existe)
    conexion = sqlite3.connect("heroes2.sqlite")
    cursor = conexion.cursor()  
    
    # Creamos la tabla 'heroes' con los campos especificados, si no existe
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS heroes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            codigo TEXT UNIQUE NOT NULL,
            fuerza INTEGER NOT NULL,
            destreza INTEGER NOT NULL,
            inteligencia INTEGER NOT NULL
        );
    """)
    
    # Guardamos los cambios en la base de datos
    conexion.commit()  
    
    # Cerramos la conexión y el cursor para liberar recursos
    cursor.close()
    conexion.close()

# Código principal
if __name__ == "__main__":
    # Imprimimos un mensaje para saber que el programa ha comenzado
    print("Hello World!")
    
    # Llamamos a la función para crear la base de datos y la tabla 'heroes' si no existen
    crear_db()
    
    # Creamos un objeto Heroe con sus atributos
    heroe1 = Heroe("Batman", "1612001", 85, 95, 100)
    
    # Llamamos a la función para guardar el héroe en la base de datos
    guardar_heroe(heroe1)
