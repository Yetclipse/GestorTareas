from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)

@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all() 
    # Consultamos y almacenamos todas las tareas que hay en la base de datos, para luego mostrarlas en el index.html
    return render_template('index.html',lista_de_tareas=todas_las_tareas)

@app.route('/crear-tareas', methods=['POST'])
def crear():
    #La tarea es un objeto de la clase Tarea, 
    #el contenido de la tarea se obtiene del formulario que se envía desde el index.html,
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecho=False)
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True) #el debug es para que se actualice cada vez que se haga un cambio en el código

