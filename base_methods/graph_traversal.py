from collections import deque

def bfs(graph, start):
    """
    Performs a breadth-first search on a graph, starting at the given vertex.

    Example:
        >>> graph = {
        ...     'A': set('BC'),
        ...     'B': set('AD'),
        ...     'C': set('AE'),
        ...     'D': set('BF'),
        ...     'E': set('CF'),
        ...     'F': set('DE')
        ... }
        >>> bfs(graph, 'A')
        ['A', 'B', 'C', 'D', 'E', 'F']

    :param graph: A dictionary of adjacency lists.
    :param start: The starting vertex.
    :return: A list of vertices in the order they were visited.
    """
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex] - visited)

    return result

def dfs(graph, start, visited=None):
    """
    Performs a depth-first search on a graph, starting at the given vertex.

    Example:
        >>> graph = {
        ...     'A': set('BC'),
        ...     'B': set('AD'),
        ...     'C': set('AE'),
        ...     'D': set('BF'),
        ...     'E': set('CF'),
        ...     'F': set('DE')
        ... }
        >>> dfs(graph, 'A')
        ['A', 'B', 'D', 'F', 'E', 'C']

    :param graph: A dictionary of adjacency lists.
    :param start: The starting vertex.
    :param visited: A set of vertices that have already been visited.
    :return: A list of vertices in the order they were visited.
    """
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph[start] - visited:
        result += dfs(neighbor, visited)
    return result
