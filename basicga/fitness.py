"""
fitness calculation
"""
from .individual import Individual


class FitnessCalc(object):
    """
    fitness calculation class
    """
    def __init__(self, default_length=64):
        self.default_length = default_length
        self.solution = Individual(bitstring_or_list=[0 for _ in range(default_length)])


    def set_solution(self, bitstring_or_list):
        """
        set the solution as a string of bits or a list of ints
        """
        if isinstance(bitstring_or_list, str):
            self.solution = Individual(length=self.default_length)
            self.solution.genes = [int(b) for b in bitstring_or_list]
        elif isinstance(bitstring_or_list, list):
            self.solution = Individual(length=self.default_length, bitstring_or_list=bitstring_or_list)


    def fitness(self, individual):
        """
        compute individual fitness
        """
        fitness = sum([a == b for a, b in zip(individual.genes, self.solution.genes)])
        return fitness


    def max_fitness(self):
        """
        return maximum fitness
        """
        return self.default_length


"""
package simpleGa;

public class FitnessCalc {

    static byte[] solution = new byte[64];

    /* Public methods */
    // Set a candidate solution as a byte array
    public static void setSolution(byte[] newSolution) {
        solution = newSolution;
    }

    // To make it easier we can use this method to set our candidate solution
    // with string of 0s and 1s
    static void setSolution(String newSolution) {
        solution = new byte[newSolution.length()];
        // Loop through each character of our string and save it in our byte
        // array
        for (int i = 0; i < newSolution.length(); i++) {
            String character = newSolution.substring(i, i + 1);
            if (character.contains("0") || character.contains("1")) {
                solution[i] = Byte.parseByte(character);
            } else {
                solution[i] = 0;
            }
        }
    }

    // Calculate inidividuals fittness by comparing it
    // to our candidate solution
    static int getFitness(Individual individual) {
        int fitness = 0;
        // Loop through our individuals genes and compare them to our cadidates
        for (int i = 0; i < individual.size() && i < solution.length; i++) {
            if (individual.getGene(i) == solution[i]) {
                fitness++;
            }
        }
        return fitness;
    }

    // Get optimum fitness
    static int getMaxFitness() {
        int maxFitness = solution.length;
        return maxFitness;
    }
}
"""
