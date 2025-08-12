import heapq

def prim(graph, start):
    mst = []
    visited = set([start])
    edges = [(weight, start, to) for to, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for to_next, w in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (w, to, to_next))
    return mst

# Örnek ağırlıklı graf
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1},
    'C': {'A': 3, 'B': 1, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

start_node = 'A'
mst = prim(graph, start_node)
print("Prim algoritması ile bulunan minimum kapsayan ağaç:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} ağırlık: {edge[2]}")









class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False

def kruskal(graph):
    edges = []
    for u in graph:
        for v, w in graph[u].items():
            if (v, u, w) not in edges:
                edges.append((u, v, w))
    edges.sort(key=lambda x: x[2])

    ds = DisjointSet(graph.keys())
    mst = []

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
    return mst

# Örnek grafik
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}

mst = kruskal(graph)
print("Kruskal algoritması ile bulunan minimum kapsayan ağaç:")
for edge in mst:
    print(f"{edge[0]} - {edge[1]} ağırlık: {edge[2]}")
