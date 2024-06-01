from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# Crear el problema
problem = LpProblem("Maximizar_Beneficio", LpMaximize)

# Parámetros
capacities = [2 * 10**6, 2.5 * 10**6, 1.3 * 10**6, 3 * 10**6]
royalties = [5, 4, 4, 5]
qualities = [1.0, 0.7, 1.5, 0.5]
required_qualities = [0.9, 0.8, 1.2, 0.6, 1.0]
discount_factor = [1 / (1 + 0.1) ** j for j in range(1, 6)]

# Variables de decisión
x = LpVariable.dicts("x", [(i, j) for i in range(1, 5) for j in range(1, 6)], lowBound=0)
y = LpVariable.dicts("y", [(i, j) for i in range(1, 5) for j in range(1, 6)], cat='Binary')

# Función objetivo
revenue = lpSum([discount_factor[j-1] * (10 * lpSum([x[(i, j)] for i in range(1, 5)]) - lpSum([royalties[i-1] * y[(i, j)] for i in range(1, 5)])) for j in range(1, 6)])
problem += revenue

# Restricciones de capacidad de producción
for i in range(1, 5):
    for j in range(1, 6):
        problem += x[(i, j)] <= capacities[i-1] * y[(i, j)]

# Restricciones de número máximo de minas operativas
for j in range(1, 6):
    problem += lpSum([y[(i, j)] for i in range(1, 5)]) <= 3

# Restricciones de calidad del mineral mezclado
for j in range(1, 6):
    problem += lpSum([qualities[i-1] * x[(i, j)] for i in range(1, 5)]) == required_qualities[j-1] * lpSum([x[(i, j)] for i in range(1, 5)])

# Resolver el problema
problem.solve()

# Obtener y mostrar los resultados
for j in range(1, 6):
    print(f"Año {j}:")
    for i in range(1, 5):
        print(f"  x[{i},{j}] (toneladas extraídas de la mina {i}): {x[(i, j)].varValue}")
        print(f"  y[{i},{j}] (mina {i} operativa): {y[(i, j)].varValue}")
    print()
