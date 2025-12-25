import random

def count_conflicts(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                conflicts += 1
            if abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def create_individual(n):
    """Create a random individual (board configuration)."""
    return [random.randint(0, n - 1) for _ in range(n)]

def crossover(parent1, parent2):
    """Perform single-point crossover between two parents."""
    n = len(parent1)
    point = random.randint(1, n - 2)
    return parent1[:point] + parent2[point:]

def mutate(board, mutation_rate=0.1):
    """Mutate the board by randomly changing the row of some queens."""
    n = len(board)
    for col in range(n):
        if random.random() < mutation_rate:
            board[col] = random.randint(0, n - 1)
    return board

def solve_n_queens_genetic(n, population_size=50,
                              generations=300,
                              mutation_rate=0.2):
    """Solve N-Queens using a Genetic Algorithm.
    Returns one solution or none"""

    population = [create_individual(n) for _ in range(population_size)]

    for gen in range(generations):
        if gen % 50 == 0:
            print(f" GA runnung for ={n}, generation={gen}")
             
        
        population.sort(key=lambda b: count_conflicts(b))

        # best solution found
        if count_conflicts(population[0]) == 0:
            return population[0]
        
        new_population = population[:10]  # Elitism: carry forward the best 10 individuals

        while len(new_population) < population_size:
             parent1 = random.choice(population[:50])
             parent2 = random.choice(population[:50])

        child = crossover(parent1, parent2)
        child = mutate(child, mutation_rate)
        new_population.append(child)

        population = new_population

    return None