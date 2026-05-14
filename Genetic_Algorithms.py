import random

# Constants
TARGET_PHRASE = "You can't handle the truth!" # The target phrase to be matched
POPULATION_SIZE = 200 # Number of individuals in the population
MUTATION_RATE = 0.05 # Probability of mutation

# Generate initial population
def generate_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ',.!") for _ in range(len(TARGET_PHRASE)))
        population.append(individual)
    return population

# Calculate fitness score
def calculate_fitness(individual):
    score = 0
    for i in range(len(TARGET_PHRASE)):
        if individual[i] == TARGET_PHRASE[i]:
            score += 1
    return score

# Select parents based on fitness
def select_parents(population, tournament_size=10):
    def tournament():
        contestants = random.sample(population, tournament_size)
        return max(contestants, key=calculate_fitness)
    
    return [tournament(), tournament()]

# Create offspring through crossover
def crossover(parents):
    offspring = ""
    crossover_point = random.randint(0, len(TARGET_PHRASE) - 1)
    for i in range(len(TARGET_PHRASE)):
        if i <= crossover_point:
            offspring += parents[0][i]
        else:
            offspring += parents[1][i]
    return offspring

# Mutate offspring
def mutate(offspring):
    mutated_offspring = ""
    for i in range(len(offspring)):
        if random.random() < MUTATION_RATE:
            mutated_offspring += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ',.!")
        else:
            mutated_offspring += offspring[i]
    return mutated_offspring

# Main genetic algorithm
def genetic_algorithm():
    population = generate_population()
    generation = 1

    while True:
        best = max(population, key=calculate_fitness)
        print(f"Generation {generation} - Best Fit: {best}")

        if TARGET_PHRASE in population:
            break

        new_population = [best]  # carry the best forward
        for _ in range((POPULATION_SIZE - 1) // 2):
            parents = select_parents(population)
            offspring = crossover(parents)
            mutated_offspring = mutate(offspring)
            new_population.extend([offspring, mutated_offspring])

        population = new_population
        generation += 1

# Run the genetic algorithm
genetic_algorithm()