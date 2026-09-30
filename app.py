import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

print("Conexión realizada con éxito.")

conn.close()