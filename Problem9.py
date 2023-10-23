#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
String Spelled by a Genome Path Problem

Find the string spelled by a genome path.

Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.

Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.

"""
class KmerProcessor:

    def sequence(self, kmer):
        kmers = kmer[0]
        for k in kmer[1:]:
            kmers += k[-1]
        return kmers

    def read_file(self, filename):
        with open(filename, 'r') as file:
            motif = [line.strip() for line in file]
        return motif

    def process(self, filename):
        kmer_list = self.read_file(filename)
        genome = self.sequence(kmer_list)
        return genome

if __name__ == '__main__':
    processor = KmerProcessor()
    filename = input("Enter path to file: ")
    genome = processor.process(filename)
    print(genome)
