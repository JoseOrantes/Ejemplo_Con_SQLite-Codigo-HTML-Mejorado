#importaciones necesarias
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.users import getUserbyCui, registerUser
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

auth_bp = Blueprint("auth", __name__)

#Metodo get is por default
@auth_bp.route("/", methods=["GET", "POST"])  #Nuevo decorador
def login():
    if request.method == "POST":
        cui = request.form["cui"]
        password = request.form["password"]
        user = getUserbyCui(cui)
        
        if user and user["password"] == password:
            session["cui"] = user["cui"]
            return redirect(url_for("catalog.products"))
        else:
            flash('Wrong credentials')
        
    return render_template('login.html')

#Metodo get is por default
@auth_bp.route("/logout")  #Nuevo decorador
def logout():
    session.clear() #borra todo
    flash("Sesión cerrada correctamente", "Success")
    return redirect(url_for("auth.login"))

#Metodo get es por default
@auth_bp.route("/registro", methods=["GET", "POST"])  #Nuevo decorador
def registro():
    if request.method == "POST":
        cui = request.form["cui"]
        name = request.form["name"]
        dateBorn = request.form["dateBorn"]
        email = request.form["email"]
        password = request.form["password"]
        picture = request.files["picture"]
        
        #Valida si ya existe en el perfil
        filename = None
        if picture:
            filename = secure_filename(picture.filename)
            picture.save(os.path.join(UPLOAD_FOLDER, filename))
        
        if registerUser(cui, name, email, password, dateBorn, filename):  # Pass only the filename here
            flash("Registro exitoso. Puedes iniciar sesión", "success")
            return redirect(url_for("auth.login"))
        else:
            flash("El usuario ya existe", "danger")
    # Return the registration form for GET request
    return render_template("registro.html")
    

#metodo GET                    
@auth_bp.route("/home")
def home():
    cui = session.get("cui")
    if not cui:
        flash("Debes iniciar sesion", "danger")
        return redirect(url_for("auth.login"))
    
    # Obtenemos el usuario que se va a loggear
    user = getUserbyCui(cui)

    if not user:
        flash("Usuario no encontrado", "danger")
        session.pop("cui", None)
        return redirect(url_for('auth.login'))

    return render_template("home.html", user=user, session=session)