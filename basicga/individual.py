"""
Individual class
"""
import os
from . import fitness


class Individual(object):
    """
    Manage an individual
    """

    defaultGeneLength = 64

    def __init__(self):
        self._fitness = 0
        self.genes = bytearray(os.urandom(self.defaultGeneLength))  # random array of bytes
        self.repr = None


    @property
    def gene(self, idx):
        """
        Return gene at index idx
        """
        return self.genes[idx]

    @gene.setter
    def gene(self, idx, value):
        """
        Set a new gene at index idx
        """
        self.genes[idx] = value

    @property
    def size(self):
        """
        Return gene length
        """
        return len(self.genes)

    def fitness(self):
        """
        Return memoized fitness value
        """
        if self._fitness:
            self._fitness = fitness.compute(self)
        return self._fitness

    def __repr__(self):
        if not self.repr:
            self.repr = bin(int.from_bytes(self.genes, 'little'))
        return self.repr
