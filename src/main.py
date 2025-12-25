import time
from backtracking import solve_n_queens
from csp import solve_n_queens_csp
from hill_climbing import solve_n_queens_hill_climbing
from genetic_algorithm import solve_n_queens_genetic



def run_experiment(method, solver, n):
    start = time.time()
    solutions = solver(n)
    end = time.time()
    return method, n, len(solutions), end - start


if __name__ == "__main__":
    methods = [
        ("Backtracking", solve_n_queens),
        ("CSP", solve_n_queens_csp),
        ("Hill Climbing", lambda n: [solve_n_queens_hill_climbing(n)]),
        ("Genetic Algorithm", lambda n: [solve_n_queens_genetic(n)] if n <= 10 else[])
    ]

    for method, solver in methods:
        print(f"\nMethod: {method}")
        for n in [4, 8, 10]:
            name, size, count, time_taken = run_experiment(method, solver, n)
            print(f"N={size}, Solutions={count}, Time={time_taken:.4f}s")


    
