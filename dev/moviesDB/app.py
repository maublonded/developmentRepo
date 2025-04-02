''' Programa principal de MovieDB '''

from flask import Flask, request, url_for, render_template, redirect, flash, session

import os
import random
import movieClasses as mc

app = Flask(__name__)
app.secret_key = os.urandom(24) # Clave secreta para la sesion
sistema = mc.SistemaCine()
archivo_actores = "datos/actores.csv"
archivo_peliculas = "datos/peliculas.csv"
archivo_relaciones = "datos/relacion.csv"
archivo_usuarios = "datos/users_hashed.csv"
sistema.cargar_csv(archivo_actores, mc.Actor)
sistema.cargar_csv(archivo_peliculas, mc.Pelicula)
sistema.cargar_csv(archivo_relaciones, mc.Relacion)
sistema.cargar_csv(archivo_usuarios, mc.User)

@app.route('/')
def index():
    ''' Pagina principal de la aplicacion '''
    return render_template('index.html')

@app.route('/actores')
def actores():
    ''' Muestra la lista de actores '''
    actores = sistema.actores.values()
    return render_template('actores.html', actores=actores)

@app.route('/peliculas')
def peliculas():
    ''' Muestra la lista de peliculas '''
    peliculas = sistema.peliculas.values()
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/actor/<int:id_actor>')
def actor(id_actor):
    ''' Muestra la informacion de un actor '''
    actor = sistema.actores[id_actor]
    personajes = sistema.obtener_personajes_por_estrella(id_actor)
    print(actor)
    print(personajes)
    return render_template('actor.html', actor=actor, lista_peliculas=personajes)

@app.route('/pelicula/<int:id_pelicula>')
def pelicula(id_pelicula):
    ''' Muestra la informacion de una pelicula '''
    pelicula = mc.peliculas[id_pelicula]
    return render_template('pelicula.html', pelicula=pelicula)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        exito  = sistema.login(username, password)  
        if exito:
            session['logged_in'] = True
            session['username'] = sistema.usuario_actual.nombre_completo
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('index'))
            #return render_template('index.html')
        else:
            flash('Usuario o contraseña incorrectos', 'danger')
            return render_template('login.html')
    return render_template('login.html')

@app.route('/logout')
def logout():
    ''' Cierra la sesión del usuario '''
    session.clear()
    sistema.usuario_actual = None
    flash('Has cerrado sesión correctamente', 'info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)