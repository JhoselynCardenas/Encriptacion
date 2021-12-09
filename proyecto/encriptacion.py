
import librerias

opcion = 0

librerias.generar_clave()
clave=librerias.cargar_clave()

archivos = "archivo.txt"
hola = "hola.txt"
pruebas = "prueba.txt"

while opcion !=5:
    print("\nSelecciona una opción")
    print("1.Leer Archivo\n2.Agregar Texto al Archivo\n3.Encriptar\n4.Desencriptar\n5.Salir")
    opcion = int(input ("Ingresa una opción: "))
    if opcion ==1:
        while opcion !=4:
            print("\n¿Qué archivo quieres ver?")
            print("1.Archivo\n2.Hola\n3.Pruebas\n4.Atrás")
            opcion = int(input ("Ingresa una opción: "))
            if opcion ==1:
             librerias.leerArchivo(archivos)
            elif opcion ==2:
                librerias.leerArchivo(hola)
            elif opcion == 3:
                librerias.leerArchivo(pruebas)
            else:
                print("\n Atrás")
    elif opcion == 2:
        while opcion != 4:
            print("\n¿Qué archivo deseas?")
            print("1.Archivo\n2.Hola\n3.Pruebas\n4.Atrás")
            opcion = int(input ("Ingresa una opción: "))
            if opcion ==1:
                linea = input("Texto a agregar:")
                librerias.escribirArchivo(linea, archivos)
            elif opcion ==2:
                linea = input("Texto a agregar:")
                librerias.escribirArchivo(linea, hola)
            elif opcion == 3:
                linea = input("Texto a agregar:")
                librerias.escribirArchivo(linea, pruebas)
            else:
                print("\n Atrás")
        
    elif opcion == 3:
        while opcion != 4:
            print("\n¿Qué quieres hacer?")
            print("1.Encriptar un archivo\n2.Encriptar todos los archivos\n3.Atrás")
            opcion = int(input ("Ingresa una opción: "))
            if opcion ==1:
                while opcion != 4:
                    print("\n¿Qué archivo deseas?")
                    print("1.Archivo\n2.Hola\n3.Pruebas\n4.Atrás")
                    opcion = int(input ("Ingresa una opción: "))
                    if opcion ==1:
                        librerias.encriptar(archivos,clave)
                        print("Archivo encriptado, el texto es: ")
                        librerias.leerArchivo(archivos)
                    elif opcion ==2:
                        librerias.encriptar(hola,clave)
                        print("Archivo encriptado, el texto es: ")
                        librerias.leerArchivo(hola)
                    elif opcion == 3:
                        librerias.encriptar(pruebas,clave)
                        print("Archivo encriptado, el texto es: ")
                        librerias.leerArchivo(pruebas)
                    else:
                        print("\n Atrás")
            elif opcion ==2:
                librerias.encriptar(archivos,clave)
                librerias.encriptar(hola,clave)
                librerias.encriptar(pruebas,clave)
                print("Archivos encriptados")
                print("\nNombre del archivo: archivo")
                librerias.leerArchivo(archivos)
                print("\nNombre del archivo: hola")
                librerias.leerArchivo(hola)
                print("\nNombre del archivo: prueba")
                librerias.leerArchivo(pruebas)
            else:
                print("\nAtrás")

    elif opcion == 4:
        print("\n¿Qué quieres hacer?")
        print("1.Desencriptar un archivo\n2.Desencriptar todos los archivos\n3.Atrás")
        opcion = int(input ("Ingresa una opción: "))
        if opcion ==1:
            while opcion != 4:
                print("\n¿Qué archivo deseas?")
                print("1.Archivo\n2.Hola\n3.Pruebas\n4.Atrás")
                opcion = int(input ("Ingresa una opción: "))
                if opcion ==1:
                    librerias.desencriptar(archivos,clave)
                    print("archivo desencriptado, el texto es: ")
                    librerias.leerArchivo(archivos)
                elif opcion ==2:
                    librerias.desencriptar(hola,clave)
                    print("archivo desencriptado, el texto es: ")
                    librerias.leerArchivo(hola)
                elif opcion == 3:
                    librerias.desencriptar(pruebas,clave)
                    print("archivo desencriptado, el texto es: ")
                    librerias.leerArchivo(pruebas)
                else:
                    print("\n Atrás")
        elif opcion ==2:
            librerias.desencriptar(archivos,clave)
            librerias.desencriptar(hola,clave)
            librerias.desencriptar(pruebas,clave)
            print("Archivos desencriptados")
            print("\nNombre del archivo: archivo, el texto es:")
            librerias.leerArchivo(archivos)
            print("\nNombre del archivo: hola, el texto es: ")
            librerias.leerArchivo(hola)
            print("\nNombre del archivo: prueba, el texto es: ")
            librerias.leerArchivo(pruebas)
        else:
            print("\nAtrás")
        
    else:
        print("\n¡Opción seleccionada Incorrecta!")