# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:59:56 2021

@author: sebas
"""
import numpy as np
import matplotlib.pyplot as plt

archivo = open(r"C:\Users\sebas\Google Drive\Fisica\Mecanica_Estadistica\Proyecto\gatsby.txt",encoding="utf8",mode='r')
texto = archivo.read()



# Los caracteres que no contamos como palabras
quitar = "¡!¿?()[],;_-:.123456789*\n!\"'"
for caracter in quitar:
    texto = texto.replace(caracter,
                          "")  # Remplazarlo por "nada"; es decir, removerlo

# Lo convertimos a minúsculas pues una palabra mayúscula y minúscula cuenta como una sola
texto = texto.lower()
# Las palabras están separadas por un espacio así que convertimos la cadena a arreglo
palabras = texto.split(" ")

# Ahora vamos a contar las palabras creando un diccionario. En este caso la clave del diccionario
# será la palabra, y el valor será el conteo
diccionario_frecuencias = {}
for palabra in palabras:
    if palabra in diccionario_frecuencias:
        diccionario_frecuencias[palabra] += 1
    else:
        diccionario_frecuencias[palabra] = 1
"""       
for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    print(f"La palabra '{palabra}' tiene una frecuencia de {frecuencia}")
""" 
densidad=np.zeros(26)
total=0
for palabra in diccionario_frecuencias:
    frecuencia = diccionario_frecuencias[palabra]
    for i in range(0,25):
        if len(palabra)==i:
            densidad[i]+=1
    total+=1
plt.plot(np.arange(1,27),densidad)
plt.show() 
 
    
    
    