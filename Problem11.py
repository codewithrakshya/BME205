#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
Given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text. The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).

De Bruijn Graph from a String Problem

Construct the de Bruijn graph of a string.

Given: An integer k and a string Text.

Return:DeBruijnk(Text), in the form of an adjacency list.
"""

class de_bruijn:
    def __init__(self, file):
        self.file = file
        self.adjacency_list = {}
    def graph(self):
        with open(self.file,'r') as file:
            k = int(file.readline().strip())
            kmer = file.read().strip()

        for i in range(len(kmer) - k + 1):
            kmers = kmer[i:i + k]
            prefix = kmers[:-1]
            suffix = kmers[1:]

            if prefix in self.adjacency_list:
                self.adjacency_list[prefix].append(suffix)
            else:
                self.adjacency_list[prefix] = [suffix]
    def adj_list(self):
        return self.adjacency_list

file_path = input("Enter the path to file: ")
graph_constructor = de_bruijn(file_path)
graph_constructor.graph()

adjacency_list = graph_constructor.adj_list()
for node, neighbors in sorted(adjacency_list.items()):
    print(f"{node} -> {', '.join(sorted(neighbors))}")