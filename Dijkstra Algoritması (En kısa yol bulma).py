import heapq

def dijkstra(graph, start):
    # Mesafeleri sonsuz yap, başlangıç noktasının mesafesi 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (mesafe, düğüm)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

# Örnek grafik (Adjacency list ile, ağırlıklı)
graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print(f"{start_node} düğümünden diğer düğümlere en kısa mesafeler:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
