#!/usr/bin/env python3
#BME205
#Rakshya Sharma
"""
In “Find an Eulerian Cycle in a Graph”, we defined an Eulerian cycle. A path that traverses each edge of a graph exactly once (but does not necessarily return to its starting node is called an Eulerian path.

Eulerian Path Problem

Find an Eulerian path in a graph.

Given: A directed graph that contains an Eulerian path, where the graph is given in the form of an adjacency list.

Return: An Eulerian path in this graph.
"""
from collections import Counter, defaultdict
def parse_adjacency_list(inFile):
    """Parse adjacency list format [u -> v1,v2,v3]
    and return corresponding graph.
    """
    graph = {}
    for line in inFile.readlines():
        u, vs = line.strip().split(' -> ')
        u, vs = int(u), list(map(int, vs.split(',')))
        if u not in graph:
            graph[u] = []
        graph[u].extend(vs)
    return graph

def find_cycle(graph, start):
    """Return a sequence of nodes which form a cycle
    starting from a node 'start'.
    """
    cycle = []
    u = graph[start].pop()
    while u != start:
        cycle.append(u)
        u = graph[u].pop()
    cycle.append(u)

    # Clean up nodes which have no edges.
    toRemove = [k for k, v in graph.items() if not v]
    for k in toRemove:
        del graph[k]

    return cycle

def find_eulerian_cycle(graph, start=0):
    """Return an eulerian cycle of the graph."""
    cycle = [start] + find_cycle(graph, start)
    updated = True
    while updated:
        updated = False
        for i, start in enumerate(cycle):
            # If an edge starting from the node still exists,
            # insert new cycle.
            if start in graph:
                updated = True
                cycle = cycle[:i+1] + find_cycle(graph, start) + cycle[i+1:]
                break

    return cycle

def add_imaginary_edge(graph):
    """Add imaginary edge (start, end), where start is the node
    with surplus incoming edges, and end is the node with surplus
    outgoing edges.
    """
    outgoingEdgeCounts = {}
    incomingEdgeCounts = {}
    for u in graph:
        if u not in outgoingEdgeCounts:
            outgoingEdgeCounts[u] = 0
        outgoingEdgeCounts[u] += len(graph[u])
        for v in graph[u]:
            if v not in incomingEdgeCounts:
                incomingEdgeCounts[v] = 0
            incomingEdgeCounts[v] += 1

    # Compute the difference between incoming and outgoing edges manually
    surplus_incoming = {k: incomingEdgeCounts[k] - outgoingEdgeCounts.get(k, 0)
                        for k in incomingEdgeCounts if k not in outgoingEdgeCounts
                        or incomingEdgeCounts[k] > outgoingEdgeCounts[k]}
    surplus_outgoing = {k: outgoingEdgeCounts[k] - incomingEdgeCounts.get(k, 0)
                        for k in outgoingEdgeCounts if k not in incomingEdgeCounts
                        or outgoingEdgeCounts[k] > incomingEdgeCounts[k]}

    start = list(surplus_incoming.keys())[0]
    end = list(surplus_outgoing.keys())[0]

    # Add imaginary edge.
    graph[start].append(end)
    return start, end

def find_eulerian_path(graph):
    """Return an eulerian path of the graph."""
    start, end = add_imaginary_edge(graph)
    cycle = find_eulerian_cycle(graph, start=end)[:-1]
    for i in range(len(cycle)):
        if cycle[i] == start and cycle[(i+1) % len(cycle)] == end:
            path = cycle[i+1:] + cycle[:i+1]

    return path

# Now, utilize the defined functions to find the Eulerian path
graph = parse_adjacency_list(open("/Users/rausharm/Downloads/rosalind_ba3g-6.txt", 'r'))
eulerian_path_new = find_eulerian_path(graph)
eulerian_path_new_str = '->'.join(map(str, eulerian_path_new))
print(eulerian_path_new_str)