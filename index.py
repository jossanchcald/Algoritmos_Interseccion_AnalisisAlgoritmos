"""
PARTE 2:
Seleccione 3 respuestas basadas en su análisis, 
impleméntelas y grafique sus tiempos de ejecución 
(incluir los 3 algoritmos en un mismo gráfico).
"""

import time
import random
import matplotlib.pyplot as plt

# 1. Fuerza Bruta (Selim)
def interseccion_fuerza_bruta(A, B): # Complejidad esperada: O(n) * O(m)

    comunes = []
    for a in A:
        for b in B:
            if a == b:
                comunes.append(a)
    return comunes

# 2. Algoritmo de Mapa (Josue)
def interseccion_mapas(A, B): # Complejidad esperada: O(n) + O(m)*O(1)
    pass

# 3. Algoritmo de Árbol (Nahim)
def interseccion_arbol(A, B): # Complejidad esperada: O(n*log(n) + m*log(n))
    pass

# Verificar que los algoritmos funcionen bien
"""
A_test = [4, 8, 5, 15, 3, 6, 2]
B_test = [10, 3, 1, 8, 9]

print(f"Resultado Fuerza Bruta: {interseccion_fuerza_bruta(A_test, B_test)}") 

Fuerza Bruta si devuelve como en el ejemplo [8, 3]
"""

# Tamaños de los arreglos (n y m) a evaluar
casos = [
    (100, 80),
    (300, 250),
    (600, 600),
    (900, 750),
    (1300, 1100),
    (1800, 1800),
    (2500, 2100),
    (3400, 3000),
    (4700, 4700),
    (6200, 5500)
]
    
tiempos_fbruta = []
# tiempos_mapa = [] # Descomenta Josue cuando tengas tu parte
# tiempos_arbol = [] # Descomentar Nahim cuando tengas tu parte

for n, m in casos:
    # Generar arreglos aleatorios de tamaño n y m
    A = random.sample(range(1, 100000), n)
    B = random.sample(range(1, 100000), m)
        
    # Tiempos Fuerza Bruta
    inicio = time.perf_counter()
    interseccion_fuerza_bruta(A, B)
    tiempos_fbruta.append(time.perf_counter() - inicio)
        
    # Tiempos Mapa
    # inicio = time.perf_counter()
    # interseccion_mapas(A, B)
    # tiempos_mapas.append(time.perf_counter() - inicio)
        
    # Tiempos Arboles
    # inicio = time.perf_counter()
    # interseccion_arbol(A, B)
    # tiempos_arbol.append(time.perf_counter() - inicio)
        
    print(f"Tamaño {n, m} procesado")


plt.figure(figsize=(10, 6))

#Crear los pares en la grafica
ejeX = [f"({n},{m})" for n, m in casos]

# Gráfica de Fuerza Bruta
plt.plot(
    range(len(casos)),
    tiempos_fbruta,
    marker='o',
    linestyle='-',
    color='red',
    label='Fuerza Bruta (O(n*m))'
)

# Pares (n, m) en el eje x
plt.xticks(range(len(casos)), ejeX)
    
# Configuraciones visuales de la gráfica
plt.title('Comparación de Tiempos de Ejecución', fontsize=14)
plt.xlabel('Casos evaluados (n, m)', fontsize=12)
plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
    
# Mostrar la gráfica
plt.show()