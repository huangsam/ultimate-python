# ======================================================
# 📘 GRAPH DATA STRUCTURE AND ALGORITHMS IN PYTHON
# ======================================================
# This single Python file acts as a full tutorial and code
# implementation for all the most common Graph concepts.
#
# What this file includes:
# 1️⃣ Graph Representation (Adjacency List)
# 2️⃣ Breadth-First Search (BFS)
# 3️⃣ Depth-First Search (DFS)
# 4️⃣ Topological Sort (DFS + Kahn’s Algorithm)
# 5️⃣ Dijkstra’s Algorithm (Shortest Path)
# 6️⃣ Bellman-Ford Algorithm (Shortest Path + Negative Edges)
# 7️⃣ Floyd-Warshall Algorithm (All-Pairs Shortest Paths)
# 8️⃣ Kruskal’s Algorithm (Minimum Spanning Tree)
# 9️⃣ Prim’s Algorithm (Minimum Spanning Tree)
# 🔟 Cycle Detection (Directed and Undirected Graphs)
# 11️⃣ Connected Components
#
# Each algorithm is explained with *conceptual comments*
# and *code-level explanations*.
# ======================================================

from collections import defaultdict, deque
import heapq

# ======================================================
# 🧱 1. GRAPH REPRESENTATION (Adjacency List)
# ======================================================
# A graph consists of nodes (vertices) and edges (connections).
# To efficiently represent and traverse a graph, we often use an
# adjacency list — a dictionary where:
#   key   = node/vertex
#   value = list of (neighbor, weight)
#
# Example (unweighted):
#   A: [B, C]
#   B: [A, D]
#   C: [A, D]
#   D: [B, C]
#
# Example (weighted):
#   A: [(B, 2), (C, 5)]
#   B: [(A, 2), (C, 1)]
# ======================================================

class Graph:
    def __init__(self, directed=False):
        # defaultdict creates a dictionary where each key
        # automatically starts with an empty list.
        self.graph = defaultdict(list)
        # directed=False → means undirected graph (A→B also implies B→A)
        self.directed = directed

    def add_edge(self, u, v, w=1):
        """Add an edge between u and v with optional weight."""
        self.graph[u].append((v, w))  # add neighbor and weight
        if not self.directed:
            # for undirected graphs, add the reverse edge too
            self.graph[v].append((u, w))

    def show(self):
        """Display the adjacency list representation."""
        print("\nAdjacency List Representation:")
        for node, edges in self.graph.items():
            print(f"{node} -> {edges}")

# ======================================================
# 🔁 2. BREADTH-FIRST SEARCH (BFS)
# ======================================================
# BFS explores the graph *level by level* (like a wave).
# It uses a QUEUE to visit neighbors in order of discovery.
# It’s ideal for finding the shortest path in an unweighted graph.
#
# Time Complexity: O(V + E)
# Space Complexity: O(V)
# ======================================================

def bfs(graph, start):
    """Perform BFS traversal from a start node."""
    visited = set()         # keeps track of visited nodes
    queue = deque([start])  # queue for processing nodes in FIFO order

    print("\n🟦 BFS Traversal Order:")
    while queue:
        node = queue.popleft()  # dequeue the first element
        if node not in visited:
            print(node, end=" ")  # visit the node
            visited.add(node)
            # add all unvisited neighbors to queue
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    print()

# ======================================================
# 🔂 3. DEPTH-FIRST SEARCH (DFS)
# ======================================================
# DFS explores *as far as possible* along a branch before backtracking.
# Think of it like going down one path deeply before exploring others.
# It can be implemented recursively or using a stack.
#
# Time Complexity: O(V + E)
# Space Complexity: O(V)
# ======================================================

def dfs(graph, start, visited=None):
    """Perform recursive DFS traversal."""
    if visited is None:
        visited = set()
        print("\n🟩 DFS Traversal Order:")
    print(start, end=" ")
    visited.add(start)
    # Explore each neighbor recursively
    for neighbor, _ in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# ======================================================
# ⏫ 4. TOPOLOGICAL SORT
# ======================================================
# Used ONLY for Directed Acyclic Graphs (DAG).
# It gives a linear order of vertices such that for every edge u → v,
# vertex u comes before vertex v.
#
# Example use cases:
# - Task Scheduling
# - Course Prerequisites
# ======================================================

# (A) Using DFS
def topological_sort_dfs(graph):
    visited = set()
    stack = []  # will store reverse order of completion

    def dfs_helper(node):
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                dfs_helper(neighbor)
        # when all neighbors processed, push node onto stack
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs_helper(node)
    stack.reverse()  # reverse for correct order
    print("\n🧭 Topological Sort (DFS-based):", stack)

# (B) Using Kahn’s Algorithm (BFS)
# Step 1: Compute indegree of all vertices
# Step 2: Add nodes with indegree=0 into a queue
# Step 3: Remove from queue, add to result, decrease neighbors’ indegree
# Step 4: Repeat until queue is empty
def topological_sort_kahn(graph):
    indegree = defaultdict(int)
    for u in graph:
        for v, _ in graph[u]:
            indegree[v] += 1

    queue = deque([u for u in graph if indegree[u] == 0])
    order = []

    while queue:
        u = queue.popleft()
        order.append(u)
        for v, _ in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    print("🧭 Topological Sort (Kahn’s Algorithm):", order)

# ======================================================
# 🗺️ 5. DIJKSTRA’S ALGORITHM (Shortest Path)
# ======================================================
# Used for finding shortest paths from a source node
# in a weighted graph with *non-negative weights*.
# Uses a priority queue (min-heap) for efficiency.
#
# Time Complexity: O(E log V)
# ======================================================

def dijkstra(graph, start):
    """Find shortest distance from start to all nodes."""
    dist = {node: float('inf') for node in graph}  # initialize all distances as infinity
    dist[start] = 0
    pq = [(0, start)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue
        for neighbor, weight in graph[node]:
            # Relaxation step: update if new path is shorter
            if dist[node] + weight < dist[neighbor]:
                dist[neighbor] = dist[node] + weight
                heapq.heappush(pq, (dist[neighbor], neighbor))

    print("\n🚗 Dijkstra’s shortest distances:", dist)

# ======================================================
# 🕒 6. BELLMAN-FORD ALGORITHM
# ======================================================
# Used for graphs with negative weights.
# Can detect negative-weight cycles.
# Works by relaxing all edges (V-1) times.
#
# Time Complexity: O(V * E)
# ======================================================

def bellman_ford(edges, vertices, start):
    """Find shortest paths & detect negative weight cycles."""
    dist = {v: float('inf') for v in range(vertices)}
    dist[start] = 0

    # Relax all edges V-1 times
    for _ in range(vertices - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Check for negative weight cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            print("❌ Negative weight cycle detected!")
            return
    print("\n📉 Bellman-Ford shortest paths:", dist)

# ======================================================
# 🌍 7. FLOYD-WARSHALL ALGORITHM (All-Pairs Shortest Path)
# ======================================================
# Computes shortest paths between all pairs of vertices.
# Dynamic Programming approach.
#
# Time Complexity: O(V³)
# ======================================================

def floyd_warshall(matrix):
    """Compute all-pairs shortest path distances."""
    n = len(matrix)
    dist = [row[:] for row in matrix]  # deep copy
    for k in range(n):       # k = intermediate vertex
        for i in range(n):   # i = source
            for j in range(n):  # j = destination
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    print("\n🌐 Floyd-Warshall Matrix:")
    for row in dist:
        print(row)

# ======================================================
# 🌳 8. KRUSKAL’S ALGORITHM (Minimum Spanning Tree)
# ======================================================
# Builds MST by adding smallest edge that doesn't form a cycle.
# Uses Disjoint Set Union (Union-Find).
#
# Time Complexity: O(E log E)
# ======================================================

class DSU:
    """Disjoint Set Union (Union-Find) for Kruskal's algorithm."""
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        # path compression optimization
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def kruskal(edges, vertices):
    """Build MST using Kruskal’s Algorithm."""
    dsu = DSU(vertices)
    edges.sort(key=lambda x: x[2])  # sort edges by weight
    mst, total = [], 0

    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, w))
            total += w
    print("\n🌲 Kruskal’s MST edges:", mst)
    print("Total MST weight:", total)

# ======================================================
# 🪵 9. PRIM’S ALGORITHM (Minimum Spanning Tree)
# ======================================================
# Another way to find MST — starts from a node and grows the tree.
# Uses a priority queue (min-heap) to always pick the smallest edge.
#
# Time Complexity: O(E log V)
# ======================================================

def prim(graph, start):
    """Build MST using Prim’s Algorithm."""
    visited = set()
    pq = [(0, start)]  # (weight, node)
    total = 0
    print("\n🪵 Prim’s MST edges:")
    while pq:
        weight, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        total += weight
        print(f"Include node {node} with edge weight {weight}")
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor))
    print("Total MST weight:", total)

# ======================================================
# 🔁 10. CYCLE DETECTION
# ======================================================
# Detects if a graph has cycles.
# (A) For undirected graphs → use DFS with parent tracking
# (B) For directed graphs → use recursion stack
# ======================================================

def detect_cycle_undirected(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                print("\n⚠️ Cycle detected (Undirected).")
                return
    print("\n✅ No cycle found (Undirected).")

def detect_cycle_directed(graph):
    visited, rec_stack = set(), set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited and dfs(neighbor):
                return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                print("\n⚠️ Cycle detected (Directed).")
                return
    print("\n✅ No cycle found (Directed).")

# ======================================================
# 🔗 11. CONNECTED COMPONENTS
# ======================================================
# A connected component is a subgraph where every node
# is reachable from every other node in that component.
#
# Used in undirected graphs.
# ======================================================

def connected_components(graph):
    visited = set()
    components = []

    def dfs(node, comp):
        visited.add(node)
        comp.append(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, comp)

    for node in graph:
        if node not in visited:
            comp = []
            dfs(node, comp)
            components.append(comp)

    print("\n🔗 Connected Components:", components)

# ======================================================
# 🧪 TESTING SECTION
# ======================================================
if __name__ == "__main__":
    # Create an undirected graph
    g = Graph(directed=False)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    g.show()

    # Perform traversals
    bfs(g.graph, 'A')
    dfs(g.graph, 'A')
    detect_cycle_undirected(g.graph)
    connected_components(g.graph)

    # Weighted graph for shortest path and MST
    gw = Graph(directed=False)
    gw.add_edge('A', 'B', 1)
    gw.add_edge('A', 'C', 4)
    gw.add_edge('B', 'C', 2)
    gw.add_edge('B', 'D', 7)
    gw.add_edge('C', 'D', 3)
    dijkstra(gw.graph, 'A')
    prim(gw.graph, 'A')
