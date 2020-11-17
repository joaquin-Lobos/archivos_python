#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"

import csv
import re

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0
    file = open("texto.txt", "r")

    for i in file:
        cantidad_letras += len(i)

    print("la cantidad de caracteres en el archivo es de:", cantidad_letras)


    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    file = open("archivo_de_texto", "w")

    while True:
        texto = str(input("ingrese un texto:\n"))
        if texto == "":
            break
        file.write(texto + "\n")
        cantidad_letras += len(texto)
        

    print(cantidad_letras)


    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''


def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2
    moneda = "ARS"
    departamentos = []
    total_precios = 0.0
    precio_maximo = None
    precio_minimo = None
    with open('propiedades.csv') as propiedades:
        data = list(csv.DictReader(propiedades))
        for i in data:
            if (i.get("ambientes") == str(cantidad_ambientes)) and (i.get("moneda") == moneda):
                departamentos.append(i)
    
    for i in departamentos:
        precio = float(i.get("precio"))
        total_precios += float(i.get("precio"))
        if precio_maximo == None:
            precio_maximo = precio
        elif precio_maximo <= precio:
            precio_maximo = precio
        
        if precio_minimo == None:
            precio_minimo = precio
        elif precio_minimo >= precio:
            precio_minimo = precio

   

    print("hay", len(departamentos), "departamentos con", cantidad_ambientes, "ambientes y con el precio en", moneda)
    print("el promedio de los precios de estos departamentos es:", int(total_precios / float(len(departamentos))), moneda)
    print("precio maximo:", precio_maximo,"precio minimo", precio_minimo)
    propiedades.close()

            
    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
