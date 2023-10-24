"""
Given an arbitrary collection of k-mers Patterns (where some k-mers may appear multiple times), we define CompositionGraph(Patterns) as a graph with |Patterns| isolated edges. Every edge is labeled by a k-mer from Patterns, and the starting and ending nodes of an edge are labeled by the prefix and suffix of the k-mer labeling that edge. We then define the de Bruijn graph of Patterns, denoted DeBruijn(Patterns), by gluing identically labeled nodes in CompositionGraph(Patterns), which yields the following algorithm.

    DEBRUIJN(Patterns)
        represent every k-mer in Patterns as an isolated edge between its prefix and suffix
        glue all nodes with identical labels, yielding the graph DeBruijn(Patterns)
        return DeBruijn(Patterns)
De Bruijn Graph from k-mers Problem

Construct the de Bruijn graph from a collection of k-mers.

Given: A collection of k-mers Patterns.

Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.


"""
def read_patterns_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def deBruijn(patterns):
    adjacency_list = {}
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        if prefix not in adjacency_list:
            adjacency_list[prefix] = []
        adjacency_list[prefix].append(suffix)
    return adjacency_list

def deBruijn_from_patterns(patterns):
    adjacency_list = deBruijn(patterns)
    output = []
    for key, values in sorted(adjacency_list.items()):
        output.append(f"{key} -> {','.join(values)}")
    return '\n'.join(output)

file_path = input("Enter the path to file: ")
patterns_from_file = read_patterns_from_file(file_path)
print(deBruijn_from_patterns(patterns_from_file))
