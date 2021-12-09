from cryptography import fernet
from cryptography.fernet import Fernet 
from pathlib import Path #archivos y carpetas

def leerArchivo(archivos):
    stream = open(archivos, "rt", encoding="utf-8")
    print(stream.read())
def leerArchivo(hola):
    stream = open(hola, "rt",encoding="utf-8")
    print(stream.read() )
def leerArchivo(pruebas):
     stream = open(pruebas, "rt",encoding="utf-8")
     print(stream.read())
def escribirArchivo(linea, archivos):
    with open(archivos, 'a') as file:
        file.write("\n"+linea)
def escribirArchivo(linea, hola):
    with open(hola, 'a') as file:
        file.write("\n"+linea)
def escribirArchivo(linea, pruebas):
    with open(pruebas, 'a') as file:
        file.write("\n"+linea)
def generar_clave():
    archivos = r'llave.llave'
    objetoArchivo= Path(archivos)
    if not objetoArchivo.is_file():
        clave = Fernet.generate_key() #genero la clave

        with open("llave.llave","wb") as key_file:
            key_file.write(clave)

def cargar_clave():
    return open("llave.llave","rb").read()

def encriptar(archivos,clave):
    f = Fernet(clave)
    with open(archivos, "rb") as file:
        file_data = file.read()
    
    datos_encriptados= f.encrypt(file_data)

    with open(archivos, "wb") as file:
        file.write(datos_encriptados)
def encriptar(hola,clave):
    f = Fernet(clave)
    with open(hola, "rb") as file:
        file_data = file.read()
    
    datos_encriptados= f.encrypt(file_data)

    with open(hola, "wb") as file:
        file.write(datos_encriptados)
def encriptar(pruebas,clave):
    f = Fernet(clave)
    with open(pruebas, "rb") as file:
        file_data = file.read()
    
    datos_encriptados= f.encrypt(file_data)

    with open(pruebas, "wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivos,clave):
    f= Fernet(clave)
    with open(archivos, "rb") as file:
        datos_encriptados = file.read()
    
    datos = f.decrypt(datos_encriptados)

    with open(archivos,"wb") as file:
        file.write(datos)
def desencriptar(hola,clave):
    f= Fernet(clave)
    with open(hola, "rb") as file:
        datos_encriptados = file.read()
    
    datos = f.decrypt(datos_encriptados)

    with open(hola,"wb") as file:
        file.write(datos)
def desencriptar(pruebas,clave):
    f= Fernet(clave)
    with open(pruebas, "rb") as file:
        datos_encriptados = file.read()
    
    datos = f.decrypt(datos_encriptados)

    with open(pruebas,"wb") as file:
        file.write(datos)