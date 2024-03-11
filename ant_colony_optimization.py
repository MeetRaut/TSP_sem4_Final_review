# ant_colony_optimization.py
import random

class AntColonyOptimization:
    def __init__(self, city_coordinates, num_ants=50, num_iterations=100, evaporation_rate=0.5, alpha=1, beta=2):
        self.city_coordinates = city_coordinates
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta

    def tsp_ant_colony_optimization(self):
        pheromone_matrix = self.initialize_pheromone_matrix()
        best_solution = None
        for _ in range(self.num_iterations):
            solutions = self.construct_solutions(pheromone_matrix)
            self.update_pheromones(pheromone_matrix, solutions)
            best_solution = min(solutions, key=lambda x: self.calculate_distance(x))
        return best_solution

    def initialize_pheromone_matrix(self):
        num_cities = len(self.city_coordinates)
        return [[1] * num_cities for _ in range(num_cities)]

    def construct_solutions(self, pheromone_matrix):
        solutions = []
        for _ in range(self.num_ants):
            solution = self.construct_solution(pheromone_matrix)
            solutions.append(solution)
        return solutions

    def construct_solution(self, pheromone_matrix):
        num_cities = len(self.city_coordinates)
        unvisited_cities = set(range(num_cities))
        current_city = random.choice(list(unvisited_cities))
        unvisited_cities.remove(current_city)
        solution = [current_city]
        while unvisited_cities:
            probabilities = self.calculate_probabilities(current_city, unvisited_cities, pheromone_matrix)
            next_city = random.choices(list(unvisited_cities), weights=probabilities)[0]
            solution.append(next_city)
            unvisited_cities.remove(next_city)
            current_city = next_city
        return solution

    def calculate_probabilities(self, current_city, unvisited_cities, pheromone_matrix):
        probabilities = []
        for city in unvisited_cities:
            pheromone = pheromone_matrix[current_city][city]
            distance = ((self.city_coordinates[current_city][0] - self.city_coordinates[city][0]) ** 2 +
                        (self.city_coordinates[current_city][1] - self.city_coordinates[city][1]) ** 2) ** 0.5
            probability = pheromone ** self.alpha * (1 / distance) ** self.beta
            probabilities.append(probability)
        total_probability = sum(probabilities)
        return [p / total_probability for p in probabilities]

    def update_pheromones(self, pheromone_matrix, solutions):
        evaporation_amount = (1 - self.evaporation_rate)
        for i in range(len(pheromone_matrix)):
            for j in range(len(pheromone_matrix[i])):
                pheromone_matrix[i][j] *= evaporation_amount
        for solution in solutions:
            distance = self.calculate_distance(solution)
            pheromone_deposit = 1 / distance
            for i in range(len(solution) - 1):
                city1, city2 = solution[i], solution[i + 1]
                pheromone_matrix[city1][city2] += pheromone_deposit
                pheromone_matrix[city2][city1] += pheromone_deposit

    def calculate_distance(self, solution):
        total_distance = 0
        for i in range(len(solution) - 1):
            city1 = self.city_coordinates[solution[i]]
            city2 = self.city_coordinates[solution[i + 1]]
            distance = ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5
            total_distance += distance
        return total_distance
