# genetic_algorithm.py
import random

class GeneticAlgorithm:
    def __init__(self, city_coordinates, population_size=50, num_generations=100):
        self.city_coordinates = city_coordinates
        self.population_size = population_size
        self.num_generations = num_generations

    def tsp_genetic_algorithm(self):
        population = self.initialize_population()
        for _ in range(self.num_generations):
            population = self.evolve_population(population)
        best_solution = min(population, key=lambda x: self.calculate_fitness(x))
        return best_solution

    def initialize_population(self):
        population = []
        for _ in range(self.population_size):
            solution = list(range(len(self.city_coordinates)))
            random.shuffle(solution)
            population.append(solution)
        return population

    def evolve_population(self, population):
        new_population = []
        for _ in range(self.population_size):
            parent1, parent2 = random.sample(population, 2)
            child = self.crossover(parent1, parent2)
            new_population.append(child)
        return new_population

    def crossover(self, parent1, parent2):
        crossover_point = random.randint(0, len(parent1) - 1)
        child = parent1[:crossover_point]
        for gene in parent2:
            if gene not in child:
                child.append(gene)
        return child

    def calculate_fitness(self, solution):
        total_distance = 0
        for i in range(len(solution) - 1):
            city1 = self.city_coordinates[solution[i]]
            city2 = self.city_coordinates[solution[i + 1]]
            distance = ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5
            total_distance += distance
        return total_distance
