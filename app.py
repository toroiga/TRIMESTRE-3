from flask import flask, render_template
import sqlite3
app=flask(__name__)
#conexion a la base de datos
def get_db_connection():
    conn=sqlite3.connect('database.db')
    conn.row_factory=sqlite3.Row
    return conn
#ruta principal que muestra los datos de la tabla fake
@app.route ('/')
def index():
    conn=get_db_connection()
    rows=conn.execute('select*from fake').fetchall()
    conn.close()
    return render_template('index.html',rows=rows)
if __name__=='_main_':
    app.run(debug=True)


    
    
