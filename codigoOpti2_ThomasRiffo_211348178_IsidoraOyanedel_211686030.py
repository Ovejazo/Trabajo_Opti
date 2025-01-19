from pulp import *

#--------------- DEFINIMOS LOS EJEMPLOS QUE VAMOS A USAR ---------------

ejemplos = [
    #---------------------------- EJEMPLO 1: COMUNA PEQUEÑA ----------------------------
    {
        "nombre": "Ejemplo Comuna Pequeña",
        "zonas": 4,                    # Número de zonas geográficas (I)
        "ubicaciones": 5,              # Número de posibles ubicaciones de colegios (J)
        "colegios_construir": 3,       # Número de colegios a construir (p)
        "poblacion_estudiantil": {     # Población estudiantil por zona (P_i)
            0: 150,  # Zona 1
            1: 200,  # Zona 2
            2: 180,  # Zona 3
            3: 250,  # Zona 4
        },
        "distancias": {               # Matriz de distancias (d_ij)
            (0,0): 1.5, (0,1): 0.1, (0,2): 4.2, (0,3): 2.8, (0,4): 3.5,
            (1,0): 2.8, (1,1): 1.8, (1,2): 3.1, (1,3): 4.0, (1,4): 2.5,
            (2,0): 3.2, (2,1): 2.7, (2,2): 1.6, (2,3): 3.3, (2,4): 4.1,
            (3,0): 2.4, (3,1): 3.5, (3,2): 2.9, (3,3): 1.7, (3,4): 2.2
        }
    },
    #---------------------------- EJEMPLO 2: VERIFICACIONES DE QUE FUNCIONA EL METODO ----------------------------
    {
        "nombre": "Ejemplo Comuna Pequeña",
        "zonas": 4,                    # Número de zonas geográficas (I)
        "ubicaciones": 5,              # Número de posibles ubicaciones de colegios (J)
        "colegios_construir": 2,       # Número de colegios a construir (p)
        "poblacion_estudiantil": {     # Población estudiantil por zona (P_i)
            0: 150,  # Zona 1
            1: 200,  # Zona 2
            2: 180,  # Zona 3
            3: 250,  # Zona 4
        },
        "distancias": {               # Matriz de distancias (d_ij)
            (0,0): 1.5, (0,1): 0.1, (0,2): 4.2, (0,3): 2.8, (0,4): 3.5,
            (1,0): 2.8, (1,1): 1.8, (1,2): 3.1, (1,3): 4.0, (1,4): 2.5,
            (2,0): 3.2, (2,1): 2.7, (2,2): 1.6, (2,3): 3.3, (2,4): 0.1,
            (3,0): 2.4, (3,1): 3.2, (3,2): 2.9, (3,3): 1.7, (3,4): 2.2
        }
    },
    #---------------------------- EJEMPLO 3: COMUNA ÚNICA ----------------------------
    {
        "nombre": "Comuna de longitudinal",
        "zonas": 1,                      # Número de zonas geográficas (I)
        "ubicaciones": 4,                # Número de posibles ubicaciones de colegios (J)
        "colegios_construir": 1,         # Número de colegios a construir (p)
        "poblacion_estudiantil": {       # Población estudiantil por zona (P_i)
            0: 2341,  # Zona 1
        },
        "distancias": {                  # Matriz de distancias (d_ij)
            (0,0): 3.4, (0,1): 3.7, (0,2): 3.2, (0,3): 3.9
        }
    },
    #---------------------------- EJEMPLO 4: BARRIOS MAIPU ----------------------------
    {
    "nombre": "Diferentes barrios de Maipú (Longituinal, Maipú centro, Lo Errazuriz, Ciudad Satélite)",
    "zonas": 4,                      # Número de zonas geográficas (I)
    "ubicaciones": 1,                # Número de posibles ubicaciones de colegios (J)
    "colegios_construir": 1,         # Número de colegios a construir (p)
    "poblacion_estudiantil": {       # Población estudiantil por zona (P_i)
        0: 7028,  # Zona 1
        1: 10646,  # Zona 2
        2: 3532,  # Zona 3
        3: 5559,  # Zona 4
    },
    "distancias": {                  # Matriz de distancias (d_ij)
        (0,0): 3.8,  # Zona 1
        (1,0): 1.5,  # Zona 2
        (2,0): 6.3,  # Zona 3
        (3,0): 2.7   # Zona 4
    }
    },
    #---------------------------- EJEMPLO 5: BARRIOS MAIPU CON MÁS UBICACIONES ----------------------------
    {
    "nombre": "Diferentes barrios de Maipú (Longitudinal, Maipú Centro, Lo Errazuri, Ciudad Satélite)",
    "zonas": 4,                      # Número de zonas geográficas (I)
    "ubicaciones": 3,                # Número de posibles ubicaciones de colegios (J)
    "colegios_construir": 2,         # Número de colegios a construir (p)
    "poblacion_estudiantil": {       # Población estudiantil por zona (P_i)
        0: 7028,  # Lo Errazuri
        1: 10646,  # Longitudinal
        2: 3532,  # Maipú Centro
        3: 5559   # Ciudad Satélite
    },
    "distancias": {                  # Matriz de distancias (d_ij)
        (0,0): 3.8, (0,1): 2.5, (0,2): 4.2,  # Distancias desde Lo Errazuri
        (1,0): 1.5, (1,1): 2.0, (1,2): 3.3,  # Distancias desde Longitudinal
        (2,0): 6.3, (2,1): 4.1, (2,2): 2.8,  # Distancias desde Maipú Centro
        (3,0): 2.7, (3,1): 3.5, (3,2): 4.0   # Distancias desde Ciudad Satélite
    }
    },
    #---------------------------- EJEMPLO 6: CASO DE MELIPILLA  ----------------------------
    {
    "nombre": "Comuna de Melipilla - Área Urbana Principal",
    "zonas": 5,                      # Principales zonas urbanas
    "ubicaciones": 7,                # Ubicaciones potenciales para colegios
    "colegios_construir": 3,         # Colegios a construir basado en demanda
    "poblacion_estudiantil": {       # Distribución real aproximada de estudiantes
        0: 6800,  # Centro de Melipilla (mayor densidad)
        1: 5900,  # Sector Norte - Padre Demetrio
        2: 5400,  # Sector Sur - Poblaciones
        3: 4500,  # Sector Poniente
        4: 4400   # Sector Oriente
    },
    "distancias": {                  # Distancias reales en km basadas en rutas principales
        (0,0): 0.5, (0,1): 1.8, (0,2): 2.3, (0,3): 2.7, (0,4): 1.9, (0,5): 2.4, (0,6): 2.1,  # Desde Centro
        (1,0): 1.8, (1,1): 0.4, (1,2): 2.5, (1,3): 3.1, (1,4): 2.2, (1,5): 2.8, (1,6): 2.4,  # Desde Norte
        (2,0): 2.3, (2,1): 2.5, (2,2): 0.4, (2,3): 2.6, (2,4): 2.7, (2,5): 1.9, (2,6): 2.3,  # Desde Sur
        (3,0): 2.7, (3,1): 3.1, (3,2): 2.6, (3,3): 0.5, (3,4): 3.2, (3,5): 2.8, (3,6): 2.0,  # Desde Poniente
        (4,0): 1.9, (4,1): 2.2, (4,2): 2.7, (4,3): 3.2, (4,4): 0.4, (4,5): 2.5, (4,6): 2.9   # Desde Oriente
    }
    },
    #---------------------------- EJEMPLO 7: CASO DE LA ESTRELLA ----------------------------
    {
    "nombre": "Comuna de La Estrella - Región de O'Higgins",
    "zonas": 6,                      # Principales sectores poblados
    "ubicaciones": 12,               # Ubicaciones factibles para colegios
    "colegios_construir": 3,         # Número óptimo para la población
    "poblacion_estudiantil": {       # Distribución de los 608 estudiantes
        0: 152,  # La Estrella Centro
        1: 125,  # San Miguel de La Estrella
        2: 98,   # Las Chacras
        3: 86,   # La Aguada
        4: 75,   # San Joaquín de La Estrella
        5: 72    # Los Patrones
    },
    "distancias": {                  # Distancias en km basadas en rutas reales
        (0,0): 0.5, (0,1): 2.3, (0,2): 4.1, (0,3): 3.8, (0,4): 2.9, (0,5): 3.2, (0,6): 4.5, (0,7): 3.7, (0,8): 2.8, (0,9): 4.2, (0,10): 3.4, (0,11): 2.6,
        (1,0): 2.3, (1,1): 0.6, (1,2): 3.2, (1,3): 4.1, (1,4): 3.8, (1,5): 2.7, (1,6): 3.9, (1,7): 4.3, (1,8): 3.5, (1,9): 2.9, (1,10): 4.0, (1,11): 3.3,
        (2,0): 4.1, (2,1): 3.2, (2,2): 0.4, (2,3): 2.8, (2,4): 3.6, (2,5): 4.2, (2,6): 3.1, (2,7): 2.9, (2,8): 4.4, (2,9): 3.7, (2,10): 2.5, (2,11): 4.0,
        (3,0): 3.8, (3,1): 4.1, (3,2): 2.8, (3,3): 0.5, (3,4): 2.4, (3,5): 3.9, (3,6): 4.3, (3,7): 3.2, (3,8): 2.7, (3,9): 4.1, (3,10): 3.6, (3,11): 2.8,
        (4,0): 2.9, (4,1): 3.8, (4,2): 3.6, (4,3): 2.4, (4,4): 0.6, (4,5): 2.8, (4,6): 3.7, (4,7): 4.2, (4,8): 3.4, (4,9): 2.6, (4,10): 4.1, (4,11): 3.5,
        (5,0): 3.2, (5,1): 2.7, (5,2): 4.2, (5,3): 3.9, (5,4): 2.8, (5,5): 0.4, (5,6): 2.6, (5,7): 3.8, (5,8): 4.3, (5,9): 3.5, (5,10): 2.9, (5,11): 4.1
    }
    },
    #---------------------------- EJEMPLO 8: CASO DE PROVIDENCIA ----------------------------
    {
    "nombre": "Comuna de Providencia - Distribución por Barrios Principales",
    "zonas": 7,                       # Zonas de 2 km²
    "ubicaciones": 5,                 # Ubicaciones estratégicas para colegios
    "colegios_construir": 3,          # Número óptimo de colegios
    "poblacion_estudiantil": {        # Distribución basada en densidad poblacional real
        0: 2100,  # Pedro de Valdivia Norte (menor densidad por área residencial)
        1: 2850,  # Providencia Centro (alta densidad comercial y residencial)
        2: 2650,  # Manuel Montt (zona mixta comercial-residencial)
        3: 2450,  # Salvador (zona residencial densa)
        4: 2300,  # Barrio Italia (zona mixta cultural-residencial)
        5: 2500,  # Los Leones (zona comercial y residencial)
        6: 2200   # Pocuro (zona principalmente residencial)
    },
    "distancias": {                   # Distancias reales en km basadas en calles principales
        (0,0): 0.4, (0,1): 1.8, (0,2): 2.3, (0,3): 1.5, (0,4): 2.1,  # Desde Pedro de Valdivia Norte
        (1,0): 1.8, (1,1): 0.3, (1,2): 1.2, (1,3): 1.9, (1,4): 1.6,  # Desde Providencia Centro
        (2,0): 2.3, (2,1): 1.2, (2,2): 0.4, (2,3): 1.1, (2,4): 1.8,  # Desde Manuel Montt
        (3,0): 1.5, (3,1): 1.9, (3,2): 1.1, (3,3): 0.3, (3,4): 1.4,  # Desde Salvador
        (4,0): 2.1, (4,1): 1.6, (4,2): 1.8, (4,3): 1.4, (4,4): 0.3,  # Desde Barrio Italia
        (5,0): 1.7, (5,1): 1.3, (5,2): 1.6, (5,3): 2.0, (5,4): 1.5,  # Desde Los Leones
        (6,0): 1.9, (6,1): 1.4, (6,2): 1.7, (6,3): 1.8, (6,4): 1.3   # Desde Pocuro
    }
    },
    #---------------------------- EJEMPLO 9: CASO DE MARIO PINTO ----------------------------
    {
    "nombre": "Comuna de María Pinto - Distribución Rural-Urbana",
    "zonas": 5,                      # Principales sectores poblados
    "ubicaciones": 6,                # Ubicaciones potenciales para colegios
    "colegios_construir": 2,         # Número óptimo considerando distribución poblacional
    "poblacion_estudiantil": {       # Distribución aproximada de estudiantes por sector
        0: 750,   # María Pinto Centro (mayor concentración)
        1: 525,   # Santa Emilia
        2: 475,   # Santa Luisa
        3: 400,   # El Rosario
        4: 350    # Santa Inés
    },
    "distancias": {                  # Distancias reales en km por caminos rurales
        (0,0): 0.5, (0,1): 3.2, (0,2): 4.8, (0,3): 3.9, (0,4): 4.5, (0,5): 3.7,  # Desde María Pinto Centro
        (1,0): 3.2, (1,1): 0.4, (1,2): 5.1, (1,3): 4.2, (1,4): 3.8, (1,5): 4.6,  # Desde Santa Emilia
        (2,0): 4.8, (2,1): 5.1, (2,2): 0.4, (2,3): 3.5, (2,4): 4.7, (2,5): 4.2,  # Desde Santa Luisa
        (3,0): 3.9, (3,1): 4.2, (3,2): 3.5, (3,3): 0.5, (3,4): 3.6, (3,5): 3.8,  # Desde El Rosario
        (4,0): 4.5, (4,1): 3.8, (4,2): 4.7, (4,3): 3.6, (4,4): 0.4, (4,5): 3.3   # Desde Santa Inés
    }
    },
    #---------------------------- EJEMPLO 10: CASO DE TRASLADO ENTRE COMUNAS Puente Alto - La Florida ----------------------------
    {
    "nombre": "Interconexión Puente Alto - La Florida",
    "zonas": 8,                      # 4 zonas por comuna
    "ubicaciones": 10,               # Ubicaciones estratégicas para colegios
    "colegios_construir": 4,         # Colegios a distribuir entre ambas comunas
    "poblacion_estudiantil": {       # Distribución por zonas principales
        # Puente Alto
        0: 12500,  # Zona Bajos de Mena
        1: 15800,  # Zona Centro Puente Alto
        2: 13200,  # Zona Las Vizcachas
        3: 14500,  # Zona Gabriela
        # La Florida
        4: 11200,  # Zona San José de la Estrella
        5: 13800,  # Zona Walker Martínez
        6: 12400,  # Zona Vicuña Mackenna
        7: 10600   # Zona Santa Raquel
    },
    "distancias": {                  # Distancias reales en km considerando rutas principales
        # Desde Bajos de Mena (PA)
        (0,0): 0.5, (0,1): 2.8, (0,2): 4.5, (0,3): 3.2, (0,4): 5.7, (0,5): 6.3, (0,6): 4.8, (0,7): 5.9, (0,8): 5.2, (0,9): 4.7,
        # Desde Centro Puente Alto
        (1,0): 2.8, (1,1): 0.4, (1,2): 3.1, (1,3): 2.5, (1,4): 4.2, (1,5): 4.8, (1,6): 3.5, (1,7): 4.6, (1,8): 3.9, (1,9): 3.4,
        # Desde Las Vizcachas
        (2,0): 4.5, (2,1): 3.1, (2,2): 0.5, (2,3): 3.8, (2,4): 5.3, (2,5): 5.9, (2,6): 4.6, (2,7): 5.7, (2,8): 5.0, (2,9): 4.5,
        # Desde Gabriela
        (3,0): 3.2, (3,1): 2.5, (3,2): 3.8, (3,3): 0.4, (3,4): 3.9, (3,5): 4.5, (3,6): 3.2, (3,7): 4.3, (3,8): 3.6, (3,9): 3.1,
        # Desde San José de la Estrella (LF)
        (4,0): 5.7, (4,1): 4.2, (4,2): 5.3, (4,3): 3.9, (4,4): 0.5, (4,5): 2.8, (4,6): 2.3, (4,7): 3.4, (4,8): 2.7, (4,9): 2.2,
        # Desde Walker Martínez
        (5,0): 6.3, (5,1): 4.8, (5,2): 5.9, (5,3): 4.5, (5,4): 2.8, (5,5): 0.4, (5,6): 2.9, (5,7): 2.6, (5,8): 1.9, (5,9): 2.4,
        # Desde Vicuña Mackenna
        (6,0): 4.8, (6,1): 3.5, (6,2): 4.6, (6,3): 3.2, (6,4): 2.3, (6,5): 2.9, (6,6): 0.4, (6,7): 2.1, (6,8): 1.4, (6,9): 1.9,
        # Desde Santa Raquel
        (7,0): 5.9, (7,1): 4.6, (7,2): 5.7, (7,3): 4.3, (7,4): 3.4, (7,5): 2.6, (7,6): 2.1, (7,7): 0.5, (7,8): 1.7, (7,9): 2.2
    }
    }
]

def optimizar_localizacion_colegios(nombre, zonas, ubicaciones, colegios_construir, 
                                  poblacion_estudiantil, distancias):
    # Definimos el problema con el que vamos a trabajar
    prob = LpProblem(f"Localizacion_Colegios_{nombre}", LpMinimize)

    # --------------- PARAMETROS Y VARIABLES DEL PROBLEMA ---------------
    I = range(zonas)
    J = range(ubicaciones)

    # Variables de decisión
    y = LpVariable.dicts("colegio", J, 0, 1, LpBinary)
    x = LpVariable.dicts("asignacion", ((i,j) for i in I for j in J), 0, 1, LpBinary)

    # Función objetivo
    prob += lpSum(poblacion_estudiantil[i] * distancias[i,j] * x[i,j] 
                 for i in I for j in J)

    # --------------- RESTRICCIONES DEL PROBLEMA ---------------
    # 1. Cada zona debe ser asignada a exactamente un colegio
    for i in I:
        prob += lpSum(x[i,j] for j in J) == 1

    # 2. Solo se puede asignar a colegios que estén construidos
    for i in I:
        for j in J:
            prob += x[i,j] <= y[j]

    # 3. Número total de colegios a construir
    prob += lpSum(y[j] for j in J) == colegios_construir

    # Resolver el problema
    prob.solve(PULP_CBC_CMD())

    # Mostrar resultados
    print("\n" + "="*50)
    print(f"Resultados para {nombre}")
    print("="*50)
    print(f"Estado: {LpStatus[prob.status]}")
    print(f"Costo total (suma de distancias ponderadas) = {value(prob.objective):.2f}")

    print("\nColegios construidos:")
    for j in J:
        if value(y[j]) > 0.99:
            print(f"- Ubicación {j+1}")

    print("\nAsignaciones:")
    for i in I:
        for j in J:
            if value(x[i,j]) > 0.99:
                print(f"- Zona {i+1} asignada al colegio en ubicación {j+1}")
                print(f"  Población: {poblacion_estudiantil[i]} estudiantes")
                print(f"  Distancia: {distancias[i,j]:.1f} km")

def main():
    print("Ejemplos de Optimización de Localización de Colegios:")
    print("-" * 60)
    
    for idx, ejemplo in enumerate(ejemplos):
        print(f"{idx + 1}. {ejemplo['nombre']}")
        print(f"   Zonas: {ejemplo['zonas']}, "
              f"Ubicaciones posibles: {ejemplo['ubicaciones']}, "
              f"Colegios a construir: {ejemplo['colegios_construir']}")
        print("-" * 60)

    try:
        seleccion = int(input("\nSeleccione un ejemplo: ")) - 1

        if 0 <= seleccion < len(ejemplos):
            optimizar_localizacion_colegios(**ejemplos[seleccion])
        else:
            print("Selección inválida.")
            
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()