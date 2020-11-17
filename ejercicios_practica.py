#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import csv
import re
def contar_lineas(file1, file2 = None):
    cantidad_lineas = 0

    for i in file1:
        if file2 != None:
            file2.write(i)
        cantidad_lineas += 1   
    return cantidad_lineas
    


def ej1():
    # Ejercicios con archivos txt
    file = open("texto.txt", "r")
    print("la cantidad de lineas en el texto es:", contar_lineas(file) )  
    file.close()
    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea a linea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''


def ej2():
    # Ejercicios con archivos txt

    fi = open("notas.txt", "r")
    fo = open("copia_nota.txt", "w")
   
    print(contar_lineas(fi, fo))
    
    print("se copió el contenido del archivo exitosamente")

    fo.close()
    fi.close()

    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura (write)

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    dos_ambientes = 0
    tres_ambientes = 1
    for i in data:
        if i.get("ambientes") == "2":
            dos_ambientes += 1
        elif i.get("ambientes") == "3":
            tres_ambientes +=1


    print("la cantiad de departamentos con dos ambientes es:", dos_ambientes)
    print("la cantidad de departamentos con dos ambientes es:", tres_ambientes)
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''


def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}
    while True:
        fruta_nueva = str(input('ingresar el tipo de fruta o verdura:\n'))
        if fruta_nueva == "fin":
            break
        stock = int(input('ingresar el stock:\n'))
        inventario[fruta_nueva] = stock
    
    print(inventario)
    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario "inventario" el par:
    <fruta>:<cantidad>
    El diccionario "inventario" ya viene cargado
    con el valor el stock de manzanas para que vean
    de ejemplo.
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"
    '''
    
    # En el bucle realizar:
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"

def ej5():
    # Ejercicios con archivos CSV
    inventario_csv = open("inventario.csv", "w", newline='')
    header = ["fruta verdura", "cantidad"]
    writer = csv.DictWriter(inventario_csv, fieldnames=header)
    writer.writerow({"fruta verdura": "fruta verdura", "cantidad": "cantidad"})


    while True:
        fruta_nueva = str(input("ingresar el tipo de fruta o verdura:\n"))
        if fruta_nueva == "fin":
            break
        stock = int(input("ingresar el stock:\n"))
        writer.writerow({"fruta verdura": fruta_nueva, "cantidad": stock})
        
    inventario_csv.close()




    '''
    Parecido al el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario, que utilizaremos para escribir en el archivo CSV:

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Ojo! No es igual al diccionario del anterior ejercicio, 
    porque el anterior usaba como "clave" el nombre de la fruta.
    Ahora tenemos dos pares de valores "clave: valor", pueden
    ver el inventario con el ejemplo de la manzana.

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
