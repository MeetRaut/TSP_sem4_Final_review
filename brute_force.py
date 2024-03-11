# brute_force.py
from itertools import permutations

class BruteForce:
    def __init__(self, city_coordinates):
        self.city_coordinates = city_coordinates

    def tsp_brute_force(self):
        num_cities = len(self.city_coordinates)
        best_path = None
        min_distance = float('inf')
        for permutation in permutations(range(num_cities)):
            distance = self.calculate_distance(permutation)
            if distance < min_distance:
                min_distance = distance
                best_path = permutation
        return list(best_path)

    def calculate_distance(self, permutation):
        total_distance = 0
        for i in range(len(permutation) - 1):
            city1 = self.city_coordinates[permutation[i]]
            city2 = self.city_coordinates[permutation[i + 1]]
            distance = ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5
            total_distance += distance
        return total_distance
