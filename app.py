import sqlite3

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

# 1. CREACIÓN DE TABLAS
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    paginas INTEGER NOT NULL
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS lectores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_registro TEXT NOT NULL
)
"""
)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS prestamos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_prestamo TEXT NOT NULL,
    libro_id INTEGER NOT NULL,
    lector_id INTEGER NOT NULL,
    FOREIGN KEY (libro_id) REFERENCES libros (id),
    FOREIGN KEY (lector_id) REFERENCES lectores (id)
)
"""
)

# 2. INSERCIÓN DE DATOS
cursor.execute("SELECT COUNT(*) FROM libros")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO libros (titulo, paginas) VALUES (?, ?)",
        [
            ("Cien Años de Soledad", 417),
            ("El Principito", 96),
            ("Don Quijote de la Mancha", 863),
        ],
    )

cursor.execute("SELECT COUNT(*) FROM lectores")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO lectores (nombre, apellidos, fecha_registro) VALUES (?, ?, ?)",
        [
            ("Carlos", "Mendoza", "2024-01-15"),
            ("María", "Fernández", "2024-03-22"),
        ],
    )

cursor.execute("SELECT COUNT(*) FROM prestamos")
if cursor.fetchone()[0] == 0:
    cursor.executemany(
        "INSERT INTO prestamos (fecha_prestamo, libro_id, lector_id) VALUES (?, ?, ?)",
        [
            ("2025-05-10", 1, 1),
            ("2025-05-12", 2, 2),
        ],
    )

conn.commit()
conn.close()