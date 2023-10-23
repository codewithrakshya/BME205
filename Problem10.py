#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
In this chapter, we use the terms prefix and suffix to refer to the first k − 1 nucleotides and last k − 1 nucleotides of a k-mer, respectively.

Given an arbitrary collection of k-mers Patterns, we form a graph having a node for each k-mer in Patterns and connect k-mers Pattern and Pattern' by a directed edge if Suffix(Pattern) is equal to Prefix(Pattern'). The resulting graph is called the overlap graph on these k-mers, denoted Overlap(Patterns).

Overlap Graph Problem

Construct the overlap graph of a collection of k-mers.

Given: A collection Patterns of k-mers.

Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
"""

class graph:

    def overlap_graph(self, patterns):
        adjacency_list = {}
        for pattern in patterns:
            adjacency_list[pattern] = []
            for kmer in patterns:
                if kmer != pattern and pattern[1:] == kmer[:-1]:
                    adjacency_list[pattern].append(kmer)
        return adjacency_list

    def read_kmers_from_file(self, filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    filename = input("Enter path to the k-mers file: ")
    call_graph = graph()
    patterns = call_graph.read_kmers_from_file(filename)
    graph_structure = call_graph.overlap_graph(patterns)

    for key, values in graph_structure.items():
        for value in values:
            print(key, "->", value)
