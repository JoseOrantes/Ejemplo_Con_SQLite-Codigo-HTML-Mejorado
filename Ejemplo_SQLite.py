import sqlite3

try:
    conn = sqlite3.connect("mi_base.db") #.db es obligatorio
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            edad INTEGER
        )    
    """)
    conn.commit()
    
    #Agregar data
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES(?, ?)", ("Jose", 42))
    conn.commit()
    
    #Borra por ID    
    #cursor.execute("DELETE FROM usuarios WHERE id = ?", (2,))
    #conn.commit()
    
    #Actualiza 
    #cursor.execute("UPDATE usuarios SET edad = ? WHERE id = ?", (24, 6,))
    #conn.commit()
    
    #Borra todo
    #cursor.execute("DELETE FROM usuarios")
    #conn.commit()
    
    cursor.execute("SELECT * FROM usuarios")
    print(cursor.fetchall())
    
except sqlite3.Error as e:
    print("Error: ",e)
    
finally:
    conn.close()