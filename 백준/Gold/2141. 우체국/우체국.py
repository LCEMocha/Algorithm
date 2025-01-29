import sys
import math
input = sys.stdin.readline

n = int(input().strip())

town_and_population = []
for _ in range(n):
    town_and_population.append(list(map(int, input().split())))

town_and_population.sort(key=lambda x: x[0])
population_sum = sum([town_and_population[i][1] for i in range(n)])
population_mid = math.ceil(population_sum/2)

answer = 1
for i in range(n):
    if population_mid <= 0:
        answer = i-1
        break
    else:
        population_mid -= town_and_population[i][1]
        if population_mid <= 0:
            answer = i
            break

print(town_and_population[answer][0])