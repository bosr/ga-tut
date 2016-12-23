"""
Algorithm module
"""

import random
from .population import Population
from .individual import Individual


class Algorithm(object):
    """
    The Algorithm class holds crossover, mutation and tournament methods
    """
    def __init__(self):
        self.uniform_rate = 0.5
        self.mutation_rate = 0.015
        self.tournament_size = 5
        # self.elitism = True
        self.default_length = 64

    def crossover(self, individual_1, individual_2):
        """
        crossover between two individuals
        """
        new_individual = Individual(length=self.default_length)
        # import ipdb; ipdb.set_trace()
        for k in range(self.default_length):
            event = random.random() < self.uniform_rate
            new_individual.genes[k] = individual_1.genes[k] if event else individual_2.genes[k]
        return new_individual

    def mutate(self, individual):
        """
        individual mutation
        """
        for k in range(self.default_length):
            event = random.random() < self.mutation_rate
            individual.genes[k] = random.getrandbits(1) if event else individual.genes[k]

    def evolve_population(self, population):
        """
        evolution steps
        """
        new_population = Population(
            size=population.size(),
            fitness_calc=population.fitness_calc)
        for idx in range(population.size()):
            indiv1 = population.select(10).fittest()[0]
            indiv2 = population.select(10).fittest()[0]
            indiv = self.crossover(indiv1, indiv2)
            new_population.individuals[idx] = indiv

        for indiv in new_population.individuals:
            self.mutate(indiv)

        return new_population

"""
package simpleGa;

public class Algorithm {

    /* GA parameters */
    private static final double uniformRate = 0.5;
    private static final double mutationRate = 0.015;
    private static final int tournamentSize = 5;
    private static final boolean elitism = true;

    /* Public methods */

    // Evolve a population
    public static Population evolvePopulation(Population pop) {
        Population newPopulation = new Population(pop.size(), false);

        // Keep our best individual
        if (elitism) {
            newPopulation.saveIndividual(0, pop.getFittest());
        }

        // Crossover population
        int elitismOffset;
        if (elitism) {
            elitismOffset = 1;
        } else {
            elitismOffset = 0;
        }
        // Loop over the population size and create new individuals with
        // crossover
        for (int i = elitismOffset; i < pop.size(); i++) {
            Individual indiv1 = tournamentSelection(pop);
            Individual indiv2 = tournamentSelection(pop);
            Individual newIndiv = crossover(indiv1, indiv2);
            newPopulation.saveIndividual(i, newIndiv);
        }

        // Mutate population
        for (int i = elitismOffset; i < newPopulation.size(); i++) {
            mutate(newPopulation.getIndividual(i));
        }

        return newPopulation;
    }

    // Crossover individuals
    private static Individual crossover(Individual indiv1, Individual indiv2) {
        Individual newSol = new Individual();
        // Loop through genes
        for (int i = 0; i < indiv1.size(); i++) {
            // Crossover
            if (Math.random() <= uniformRate) {
                newSol.setGene(i, indiv1.getGene(i));
            } else {
                newSol.setGene(i, indiv2.getGene(i));
            }
        }
        return newSol;
    }

    // Mutate an individual
    private static void mutate(Individual indiv) {
        // Loop through genes
        for (int i = 0; i < indiv.size(); i++) {
            if (Math.random() <= mutationRate) {
                // Create random gene
                byte gene = (byte) Math.round(Math.random());
                indiv.setGene(i, gene);
            }
        }
    }

    // Select individuals for crossover
    private static Individual tournamentSelection(Population pop) {
        // Create a tournament population
        Population tournament = new Population(tournamentSize, false);
        // For each place in the tournament get a random individual
        for (int i = 0; i < tournamentSize; i++) {
            int randomId = (int) (Math.random() * pop.size());
            tournament.saveIndividual(i, pop.getIndividual(randomId));
        }
        // Get the fittest
        Individual fittest = tournament.getFittest();
        return fittest;
    }
}
"""
