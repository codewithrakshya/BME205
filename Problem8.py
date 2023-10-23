#!/usr/bin/env python3
#BME205 Fall23
#Rakshya Sharma
"""
String Spelled by a Genome Path Problem

Find the string spelled by a genome path.

Given: A sequence of k-mers Pattern1, ... , Pattern n such that the last k - 1 symbols of Pattern i are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.

Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Pattern i for all i.
"""
class comp:
    def string_comp(self, k, sequence):
        kmer = [sequence[i:i+k] for i in range(len(sequence)-k + 1)]
        return "\n".join(sorted(kmer))

comp_string = comp()
k = int(input("Enter k value: "))
sequence = input("Enter the sequence: ")
kmer_list = comp_string.string_comp(k, sequence)
print(kmer_list)