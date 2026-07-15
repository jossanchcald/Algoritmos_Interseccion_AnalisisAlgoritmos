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
    
    if len(B) > len(A):
        A, B = B, A

    mapa = {
        numero: indice for indice, numero in enumerate(A)
    }
    interseccion = []

    for num in B:
        if num in mapa:
            interseccion.append(num)
            del mapa[num]

    return interseccion

# 3. Algoritmo de Árbol (Nahim)
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

def altura(nodo):
    return nodo.altura if nodo else 0

def balance(nodo):
    return altura(nodo.izq) - altura(nodo.der) if nodo else 0

def actualizar_altura(nodo):
    nodo.altura = 1 + max(altura(nodo.izq), altura(nodo.der))

def rotar_derecha(y):
    x = y.izq
    y.izq = x.der
    x.der = y
    actualizar_altura(y)
    actualizar_altura(x)
    return x

def rotar_izquierda(x):
    y = x.der
    x.der = y.izq
    y.izq = x
    actualizar_altura(x)
    actualizar_altura(y)
    return y

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    if valor < raiz.valor:
        raiz.izq = insertar(raiz.izq, valor)
    elif valor > raiz.valor:
        raiz.der = insertar(raiz.der, valor)
    else:
        return raiz

    actualizar_altura(raiz)
    b = balance(raiz)

    if b > 1 and valor < raiz.izq.valor:
        return rotar_derecha(raiz)
    if b < -1 and valor > raiz.der.valor:
        return rotar_izquierda(raiz)
    if b > 1 and valor > raiz.izq.valor:
        raiz.izq = rotar_izquierda(raiz.izq)
        return rotar_derecha(raiz)
    if b < -1 and valor < raiz.der.valor:
        raiz.der = rotar_derecha(raiz.der)
        return rotar_izquierda(raiz)

    return raiz

def buscar(raiz, valor):
    while raiz:
        if valor == raiz.valor:
            return True
        elif valor < raiz.valor:
            raiz = raiz.izq
        else:
            raiz = raiz.der
    return False

def interseccion_arbol(A, B): # Complejidad esperada: O(n*log(n) + m*log(n))

    # Construimos el árbol a partir del arreglo con mayor cantidad de elementos
    if len(A) >= len(B):
        mayor, menor = A, B
    else:
        mayor, menor = B, A

    raiz = None
    for x in mayor:
        raiz = insertar(raiz, x)

    comunes = []
    for x in menor:
        if buscar(raiz, x):
            comunes.append(x)

    return comunes

# Verificar que los algoritmos funcionen bien
"""
A_test = [4, 8, 5, 15, 3, 6, 2]
B_test = [10, 3, 1, 8, 9]

print(f"Resultado Fuerza Bruta: {interseccion_fuerza_bruta(A_test, B_test)}")

Fuerza Bruta si devuelve como en el ejemplo [8, 3]

print(f"Resultado Árbol: {interseccion_arbol(A_test, B_test)}")

Árbol si devuelve como en el ejemplo [3, 8]
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
tiempos_mapa = []
tiempos_arbol = []

for n, m in casos:
    # Generar arreglos aleatorios de tamaño n y m
    A = random.sample(range(1, 100000), n)
    B = random.sample(range(1, 100000), m)
        
    # Tiempos Fuerza Bruta
    inicio = time.perf_counter()
    interseccion_fuerza_bruta(A, B)
    tiempos_fbruta.append(time.perf_counter() - inicio)
        
    # Tiempos Mapa
    inicio = time.perf_counter()
    interseccion_mapas(A, B)
    tiempos_mapa.append(time.perf_counter() - inicio)
        
    # Tiempos Arboles
    inicio = time.perf_counter()
    interseccion_arbol(A, B)
    tiempos_arbol.append(time.perf_counter() - inicio)
        
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
    label='Fuerza Bruta (O(n * m))'
)

# Gráfica de Mapa
plt.plot(
    range(len(casos)),
    tiempos_mapa,
    marker='o',
    linestyle='-',
    color='blue',
    label='Mapa (O(n + m))'
)

# Gráfica de Árbol
plt.plot(
    range(len(casos)),
    tiempos_arbol,
    marker='o',
    linestyle='-',
    color='green',
    label='Árbol AVL (O(n*log(n) + m*log(n)))'
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