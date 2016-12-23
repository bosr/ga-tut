"""
main driver
"""

from basicga import population
from basicga import fitness
from basicga import algorithm


def solve():
    """
    solve for the solution
    """
    solution = "1111011111110111010110111010100000000000100001000101001011010111"
    print("{} - solution\n".format(solution))

    algo = algorithm.Algorithm()
    fitness_calc = fitness.FitnessCalc()
    fitness_calc.set_solution(bitstring_or_list=solution)
    generation_count = 0

    pop = population.Population(size=50, fitness_calc=fitness_calc)
    best_ind, best_fitness = pop.fittest()

    while best_fitness < fitness_calc.max_fitness():
        generation_count += 1
        print("{} - {} - fittest of generation: {}".format(best_ind, best_fitness, generation_count))
        pop = algo.evolve_population(pop)
        best_ind, best_fitness = pop.fittest()

    print()
    print("{} (best found)".format(best_ind))
    print("{} (solution)".format(fitness_calc.solution))

solve()
