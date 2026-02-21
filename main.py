from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all() 
    # Consultamos y almacenamos todas las tareas que hay en la base de datos, para luego mostrarlas en el index.html
    return render_template('index.html',lista_de_tareas=todas_las_tareas)

@app.route('/crear-tareas', methods=['POST'])
def crear():
    contenido = request.form['contenido_tarea']
    categoria = request.form.get('categoria')          # puede venir vacío
    fecha_str = request.form.get('fecha_limite')     # viene "YYYY-MM-DD" o vacío
    tarea = Tarea(contenido=contenido, hecho=False, categoria=categoria, fecha_limite=fecha_limite)
    
    # Convertir String de fecha a objeto date
    fecha_limite = None 
    if fecha_str:
        try:
            fecha_limite = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        except ValueError:
            # Si la fecha no es válida, la dejamos como None
            fecha_limite = None
    
    tarea = Tarea(
        contenido=contenido, 
        hecho=False, 
        categoria=categoria if categoria else None, 
        fecha_limite=fecha_limite
    )

    # si vienen vacíos, los dejamos como None
    categoria = categoria if categoria else None
    fechas_limite = fecha_limite if fecha_limite else None
    
    tarea = Tarea(contenido=contenido, hecho=False, categoria=categoria, fecha_limite=fecha_limite)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    db.session.query(Tarea).filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/tarea-hecha/<id>') 
def hecha(id): 
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first() # Se obtiene la tarea que se busca 
    tarea.hecho = not(tarea.hecho) # Guardamos en la variable booleana de la tarea, su contrario 
    db.session.commit()  # Ejecutar la operación pendiente de la base de datos 
    return redirect(url_for('home'))  # Esto nos redirecciona a la función home()

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True) #el debug es para que se actualice cada vez que se haga un cambio en el código

