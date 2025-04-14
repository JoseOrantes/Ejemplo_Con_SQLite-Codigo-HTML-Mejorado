import json
import os

#Ruta del archivo JSON
USERS_FILE =  os.path.join("data", "users.json")#Debe ser todo mayuscula por ser ruta

#Cargando JSON
def loadUsers():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as file:
            return json.load(file) #Devuelve la lista completa
    return []

def getUserbyCui(cui):
    users = loadUsers()
    '''
    for u in users:
        if u["cui"] == cui:
            return u
    return None
    '''
    return next((u for u in users if u["cui"] == cui), None)

def saveUsers(users):
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=4) #Convierte json en diccionario
            
def registerUser(cui, name, email, password, dateBorn, picture):
    users = loadUsers()
    if getUserbyCui(cui): #Si devuelve None no existe
        return False
    
    #Si todo va bien, continua aqui
    newUser = {
            "cui" : cui,
            "name" : name,
            "dateBorn" : dateBorn,
            "email" : email,
            "password" : password,
            "picture": picture
    }
    
    users.append(newUser)
    saveUsers(users)
    return True
        