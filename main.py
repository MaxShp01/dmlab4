def max_flow(graph, source, sink):
    n = len(graph)
    flow = 0
    flow_matrix = [[0 for _ in range(n)] for _ in range(n)]

    while True:
        parent = bfs(graph, flow_matrix, source, sink)
        if not parent:
            break
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s] - flow_matrix[parent[s]][s])
            s = parent[s]
        flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            flow_matrix[u][v] += path_flow
            flow_matrix[v][u] -= path_flow
            v = u

    return flow, flow_matrix


def bfs(graph, flow_matrix, source, sink):
    n = len(graph)
    visited = [False] * n
    queue = [source]
    visited[source] = True
    parent = [-1] * n

    while queue:
        u = queue.pop(0)
        for v in range(n):
            if not visited[v] and graph[u][v] - flow_matrix[u][v] > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)
    if visited[sink]:
        return parent
    return None


graph = [
    [0, 20, 20, 20, 0, 0, 0, 0],
    [0, 0, 0, 0, 30, 0, 0, 0],
    [0, 10, 0, 0, 0, 10, 20, 0],
    [0, 0, 0, 0, 0, 15, 0, 0],
    [0, 0, 10, 0, 0, 10, 0, 20],
    [0, 0, 0, 0, 0, 0, 10, 20],
    [0, 0, 0, 10, 0, 0, 0, 20],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

source = 0
sink = 7

print(max_flow(graph, source, sink))
