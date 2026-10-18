
# 1. PETA GAME (15 x 15) & BOBOT MEDAN
# ==============================================================================
# S = Titik Awal, G = Tujuan, # = Dinding, . = Jalan Biasa (1), ~ = Lumpur (3)
maze = [
    ["S", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", "#", ".", "#", ".", "#", "#", "#", "#", "#", ".", "#", "#", "."],
    [".", "#", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#", "."],
    [".", "#", ".", "#", "#", "#", "#", "#", "#", ".", "#", "#", ".", "#", "."],
    [".", ".", ".", "#", "~", "~", "~", "~", "#", ".", ".", "#", ".", ".", "."],
    ["#", "#", ".", "#", "~", "#", "#", "~", "#", "#", ".", "#", "#", "#", "."],
    [".", ".", ".", "#", "~", "#", ".", "~", "~", "~", ".", ".", ".", ".", "."],
    [".", "#", "#", "#", "~", "#", ".", "#", "#", "~", "#", "#", "#", "#", "."],
    [".", ".", ".", ".", "~", ".", ".", ".", "#", "~", ".", ".", ".", ".", "."],
    ["#", "#", "#", ".", "#", "#", "#", ".", "#", "~", "~", "~", "#", ".", "."],
    [".", ".", ".", ".", ".", ".", "#", ".", "#", "#", "#", "~", "#", ".", "#"],
    [".", "#", "#", "#", "#", ".", "#", ".", ".", ".", ".", "~", "#", ".", "."],
    [".", "#", ".", ".", ".", ".", "#", "#", "#", "#", ".", "~", ".", ".", "."],
    [".", "#", ".", "#", "#", ".", ".", ".", ".", "#", ".", "~", "~", "#", "."],
    [".", ".", ".", ".", "#", "#", "#", "#", ".", ".", ".", ".", ".", ".", "G"],
]

ROWS = len(maze)
COLS = len(maze[0])

# Bobot medan (Terrain Cost)
TERRAIN_COST = {
    ".": 1,  # Jalan biasa
    "~": 3,  # Lumpur / medan berat
    "S": 0,  # Titik awal
    "G": 1,  # Titik tujuan
}

# 4 Arah gerak (Atas, Bawah, Kiri, Kanan)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# ==============================================================================
# 2. FUNGSI HEURISTIK (MANHATTAN DISTANCE)
# ==============================================================================
def heuristic(node, goal):
    # Manhattan distance: |x1 - x2| + |y1 - y2|
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


# ==============================================================================
# 3. ALGORITMA DIJKSTRA
# ==============================================================================
def dijkstra(start, goal):
    pq = [(0, start)]  # (jarak_kumulatif, posisi)
    distances = {start: 0}
    previous = {}
    visited = set()
    explored_count = 0

    while pq:
        cost, current = heapq.heappop(pq)

        if current in visited:
            continue
        visited.add(current)
        explored_count += 1

        if current == goal:
            break

        r, c = current
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc

            if not (0 <= nr < ROWS and 0 <= nc < COLS):
                continue
            if maze[nr][nc] == "#":
                continue

            neighbor = (nr, nc)
            step_cost = TERRAIN_COST[maze[nr][nc]]
            new_cost = cost + step_cost

            if new_cost < distances.get(neighbor, float("inf")):
                distances[neighbor] = new_cost
                previous[neighbor] = current
                heapq.heappush(pq, (new_cost, neighbor))

    if goal not in distances:
        return None, explored_count, float("inf")

    # Rekonstruksi jalur dari goal ke start
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = previous[curr]
    path.append(start)
    path.reverse()

    return path, explored_count, distances[goal]
