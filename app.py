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

conn.commit()
conn.close()