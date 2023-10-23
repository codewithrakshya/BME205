#!/usr/bin/env python3
#BME205 Fall23
#Rakshya Sharma
class count_dna:
    def __init__(self):
        self.A = 0
        self.C = 0
        self.G = 0
        self.T = 0
    def count_sequence(self, sequence):
        self.A = sequence.count('A')
        self.C = sequence.count('C')
        self.G = sequence.count('G')
        self.T = sequence.count('T')
seq = input()
counter = count_dna()
counter.count_sequence(seq)
print(f"{counter.A} {counter.C} {counter.G} {counter.T}")