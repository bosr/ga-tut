"""
Population
"""
import random
from .individual import Individual


class Population(object):
    """
    Manages all individuals in a population
    """
    def __init__(self, size=0, fitness_calc=None):
        self.individuals = [Individual() for _ in range(size)]  # list of individuals
        self.fitness_calc = fitness_calc

    def __getitem__(self, idx):
        """
        return an individual at index idx
        """
        return self.individuals[idx]


    def __setitem__(self, idx, value):
        """
        set a new individual at index idx
        """
        self.individuals[idx] = value


    def fittest(self):
        """
        Element with the best fitness
        """
        if not len(self.individuals):
            raise RuntimeError("Empty population")

        from operator import itemgetter
        elements_fitnesses = [(ind, self.fitness_calc.fitness(ind)) for ind in self.individuals]
        element, fitness = max(elements_fitnesses, key=itemgetter(1))
        return element, fitness


    def size(self):
        """
        Population size
        """
        return len(self.individuals)


    def select(self, size):
        """
        select n individuals at random
        """
        new_population = Population(size=size, fitness_calc=self.fitness_calc)
        for idx in range(size):
            rint = random.randint(0, size)
            new_population.individuals[idx] = self.individuals[rint]
        return new_population
