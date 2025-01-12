from pulp import *

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
    #---------------------------- EJEMPLO 2: COMUNA ÚNICA ----------------------------
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
    #---------------------------- EJEMPLO 3: BARRIOS MAIPU ----------------------------
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
    #---------------------------- EJEMPLO 4: BARRIOS MAIPU CON MÁS UBICACIONES ----------------------------
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
    #---------------------------- EJEMPLO 5: CASO DE MELIPILLA  ----------------------------
    {
    "nombre": "Área urbana con 3 zonas (Radio de 3.5 km)",
    "zonas": 3,                      # Número de zonas geográficas (I)
    "ubicaciones": 5,                # Número de posibles ubicaciones de colegios (J)
    "colegios_construir": 2,         # Número de colegios a construir (p)
    "poblacion_estudiantil": {       # Población estudiantil por zona (P_i)
        0: 8500,  # Zona 1
        1: 9525,  # Zona 2
        2: 6700   # Zona 3
    },
    "distancias": {                  # Matriz de distancias (d_ij)
        (0,0): 2.1, (0,1): 3.2, (0,2): 1.8, (0,3): 3.0, (0,4): 2.5,  # Distancias desde Zona 1
        (1,0): 3.4, (1,1): 2.5, (1,2): 3.1, (1,3): 2.8, (1,4): 1.7,  # Distancias desde Zona 2
        (2,0): 2.7, (2,1): 3.0, (2,2): 2.2, (2,3): 1.5, (2,4): 3.3   # Distancias desde Zona 3
    }
    },
    #---------------------------- EJEMPLO 6: CASO DE LA ESTRELLA ----------------------------
    {
    "nombre": "Comuna Simplificada (7 zonas posibles, 9 ubicaciones)",
    "zonas": 7,
    "ubicaciones": 9,
    "colegios_construir": 2,
    "poblacion_estudiantil": {       
        "0": 45, "1": 50, "2": 40, "3": 55, "4": 30, "5": 35, "6": 50
    },
    "distancias": {                  
        "(0,0)": 4.2, "(0,1)": 3.8, "(0,2)": 4.0, "(0,3)": 3.5, "(0,4)": 4.1,
        "(0,5)": 3.9, "(0,6)": 4.0, "(0,7)": 3.7, "(0,8)": 3.8,
        "(1,0)": 4.0, "(1,1)": 3.9, "(1,2)": 3.8, "(1,3)": 4.1, "(1,4)": 3.6,
        "(1,5)": 4.2, "(1,6)": 3.7, "(1,7)": 4.0, "(1,8)": 3.9,
        "(2,0)": 4.1, "(2,1)": 4.2, "(2,2)": 3.9, "(2,3)": 4.0, "(2,4)": 3.7,
        "(2,5)": 4.1, "(2,6)": 3.8, "(2,7)": 3.9, "(2,8)": 3.6,
        "(3,0)": 3.9, "(3,1)": 4.0, "(3,2)": 4.1, "(3,3)": 3.8, "(3,4)": 3.7,
        "(3,5)": 4.0, "(3,6)": 3.9, "(3,7)": 4.1, "(3,8)": 3.6,
        "(4,0)": 4.1, "(4,1)": 3.8, "(4,2)": 3.9, "(4,3)": 3.7, "(4,4)": 4.0,
        "(4,5)": 3.8, "(4,6)": 4.1, "(4,7)": 3.6, "(4,8)": 3.9,
        "(5,0)": 4.2, "(5,1)": 4.0, "(5,2)": 3.7, "(5,3)": 4.1, "(5,4)": 3.8,
        "(5,5)": 3.9, "(5,6)": 4.0, "(5,7)": 3.6, "(5,8)": 3.8,
        "(6,0)": 3.8, "(6,1)": 4.2, "(6,2)": 4.0, "(6,3)": 3.7, "(6,4)": 3.9,
        "(6,5)": 4.1, "(6,6)": 3.8, "(6,7)": 4.0, "(6,8)": 3.7,
        "(7,0)": 4.0, "(7,1)": 3.9, "(7,2)": 3.8, "(7,3)": 4.1, "(7,4)": 4.0,
        "(7,5)": 3.9, "(7,6)": 3.8, "(7,7)": 3.6, "(7,8)": 4.1,
        "(8,0)": 3.9, "(8,1)": 4.0, "(8,2)": 3.7, "(8,3)": 3.8, "(8,4)": 3.9,
        "(8,5)": 4.1, "(8,6)": 3.6, "(8,7)": 3.7, "(8,8)": 4.0
    }
    },
    #---------------------------- EJEMPLO 7: CASO DE SANTIAGO ----------------------------


    


]

def optimizar_localizacion_colegios(nombre, zonas, ubicaciones, colegios_construir, 
                                  poblacion_estudiantil, distancias):
    # Crear el problema de minimización
    prob = LpProblem(f"Localizacion_Colegios_{nombre}", LpMinimize)

    # Conjuntos
    I = range(zonas)
    J = range(ubicaciones)

    # Variables de decisión
    y = LpVariable.dicts("colegio", J, 0, 1, LpBinary)
    x = LpVariable.dicts("asignacion", ((i,j) for i in I for j in J), 0, 1, LpBinary)

    # Función objetivo
    prob += lpSum(poblacion_estudiantil[i] * distancias[i,j] * x[i,j] 
                 for i in I for j in J)

    # Restricciones
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
        seleccion = int(input("\nSeleccione un ejemplo (1-{len(ejemplos)}): ")) - 1

        if 0 <= seleccion < len(ejemplos):
            optimizar_localizacion_colegios(**ejemplos[seleccion])
        else:
            print("Selección inválida.")
            
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()