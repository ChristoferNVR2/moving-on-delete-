from pulp import *
import matplotlib.pyplot as plt
import itertools
import math

cities = {
    0: (10, 21),
    1: (20, 51),
    2: (31, 71),
    3: (40, 100),
    4: (80, 40),
    5: (15, 30)
}

N = len(cities)

x_coords = [cities[i][0] for i in range(N)]
y_coords = [cities[i][1] for i in range(N)]
plt.scatter(x_coords, y_coords)

for i in range(N):
    plt.annotate(str(i), (cities[i][0], cities[i][1]))
plt.show()


def d(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


prob = LpProblem("TSP", LpMinimize)

x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat="Binary")

prob += lpSum([d(cities[i], cities[j]) * x[(i, j)] for i in cities for j in cities if i != j])

prob += lpSum([x[(i, j)] for j in cities if i != j]) == 1
prob += lpSum([x[(j, i)] for j in cities if i != j]) == 1

# Eliminación de sub-recorridos
for k in cities:
    for S in range(2, len(cities)):
        for subset in itertools.combinations([i for i in cities if i != k], S):
            prob += pulp.lpSum([x[(i, j)] for i in subset for j in subset if i != j]) <= len(subset) - 1

# Soluciona el problema
prob.solve()

# Muestra el valor de la función objetivo
print("Distancia recorrida:", pulp.value(prob.objective))
print("\n")

# Extrae la solución
solution = []
Ciudad_Inicial = 0
Sgte_Ciudad = Ciudad_Inicial
while True:
    for j in range(N):
        if j != Sgte_Ciudad and x[(Sgte_Ciudad, j)].value() == 1:
            solution.append((Sgte_Ciudad, j))
            Sgte_Ciudad = j
            break
    if Sgte_Ciudad == Ciudad_Inicial:
        break

# Muestra el recorrido solución
print("Recorrido:")
for i in range(len(solution)):
    print(str(solution[i][0]) + " -> " + str(solution[i][1]))

# Grafica la solución
for i in range(len(solution)):
    plt.plot([cities[solution[i][0]][0], cities[solution[i][1]][0]],
             [cities[solution[i][0]][1], cities[solution[i][1]][1]], 'k-')
for i in range(N):
    plt.plot(cities[i][0], cities[i][1], 'ro')

    plt.annotate(str(i), (cities[i][0], cities[i][1]))
plt.axis('equal')
plt.grid(True)
plt.show()
