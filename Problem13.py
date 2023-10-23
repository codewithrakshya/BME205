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
class Eulerian:
    def __init__(self):
        self.graph = {}  # Initialize an empty graph represented as an adjacency list
        self.eulerian_path = []  # Initialize an empty list to store the Eulerian path

    def addEdge(self, start, end_str):
        # Add an edge to the graph
        ends = end_str.split(',')
        if start in self.graph:
            self.graph[start].extend(ends)
        else:
            self.graph[start] = ends

    def depthfirstSearch(self, current_node):
        # Use an explicit stack for DFS
        stack = [current_node]
        while stack:
            node = stack[-1]
            if node in self.graph and self.graph[node]:
                next_node = self.graph[node].pop()  # Pop from the end for efficiency
                stack.append(next_node)
            else:
                self.eulerian_path.append(stack.pop())

    def startNode(self):
        start, end = self.In_Out_degrees()
        if end is None:
            return start
        else:
            return end

    def In_Out_degrees(self):
        # Calculate in-degrees and out-degrees for each node
        in_degrees = {}
        out_degrees = {}
        start_node = None
        end_node = None

        for node in self.graph:
            out_degree = len(self.graph[node])
            out_degrees[node] = out_degree

            if node not in in_degrees:
                in_degrees[node] = 0

            for neighbor in self.graph[node]:
                if neighbor not in in_degrees:
                    in_degrees[neighbor] = 1
                else:
                    in_degrees[neighbor] += 1

        for node in self.graph:
            if out_degrees[node] - in_degrees[node] == 1:
                start_node = node
            elif in_degrees[node] - out_degrees[node] == 1:
                end_node = node

        return start_node, end_node


    def findEulerianPath(self):
        # Find the Eulerian path starting from the appropriate node
        start = self.startNode()
        self.depthfirstSearch(start)
        return ' -> '.join(reversed(self.eulerian_path))

# Accept the input file path from the user
input_file_path = input("Enter the input file path: ")

eulerian_graph = Eulerian()

# Read the input from the specified file
with open(input_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(' -> ')
        start_node = parts[0]
        end_nodes = parts[1]
        eulerian_graph.addEdge(start_node, end_nodes)

eulerian_path = eulerian_graph.findEulerianPath()
print(eulerian_path)


