# FIT1045 - Intro to Python
## Algorithms
Firstly, we need to know what computational problems are. A computational problem is an infinite collection of questions, with at least one answer for every question.
For example - Addition
- computational problem: addition
- problem instance: 17+4
- algorithm: the steps find the solution of the problem instance 

###### Graph Theory
graph G = (V, E) with set of vertices V = {v1,...,vn) and edges = {e1,...,em} where ei = (v,w)

- Path - sequence of edges which join a sequence of uniqe vertices.
- Cycle - path (non-self-intersecting) with same start and end vertex
- Connected Graph - every vertex can be reached from every other vertex
- Directed Graphs - edges have a direction

How to represent a graph?
- ***adjacency matrix:*** table with one column and one row per vertex
  - e.g. [[row1],[row2],...,[rown]]  
  - adjMatrix[1][2]: indicates that vertex 1 and 2 have an edge between them
- ***adjacency list:*** at index i, have list of vertices that has an edge with vertex i
  - adjList[0]: gets the list of vertices that are connected to vertex 
- ***edge list:*** every element is a tuple (a,b) indicating an edge between vertex 'a' and 'b'
  
***Trees***

A graph is a tree if it is:
- connected; and
- has no cycles
Properties:
- minimally connected
- unique path between any two vertices

Spanning Tree: a subgraph of G that contains all vertices of G and is a tree.

###### Prim's Algorithm
Purpose: find spanning tree of a graph

 
