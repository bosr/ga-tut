"""
Population
"""
from .individual import Individual


class Population(object):
    """
    Manages all individuals in a population
    """
    def __init__(self, population_size=0):
        self.individuals = [Individual() for _ in range(population_size)]  # list of individuals

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
        _, element = max(enumerate(self.individuals.fitness()), key=itemgetter(1))
        return element

    @property
    def size(self):
        """
        Population size
        """
        return len(self.individuals)
