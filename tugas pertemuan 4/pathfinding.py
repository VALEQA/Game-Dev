import heapq

# ==============================================================================
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


# ==============================================================================
# 4. ALGORITMA A* (A-STAR)
# ==============================================================================
def astar(start, goal):
    start_h = heuristic(start, goal)
    open_list = [(start_h, 0, start)]  # (f_score, g_score, posisi)
    came_from = {}
    g_score = {start: 0}
    closed = set()
    explored_count = 0

    while open_list:
        f, current_g, current = heapq.heappop(open_list)

        if current in closed:
            continue
        if current_g != g_score.get(current, float("inf")):
            continue

        closed.add(current)
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
            tentative_g = current_g + step_cost

            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, tentative_g, neighbor))

    if goal not in g_score:
        return None, explored_count, float("inf")

    # Rekonstruksi jalur dari goal ke start
    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = came_from[curr]
    path.append(start)
    path.reverse()

    return path, explored_count, g_score[goal]


# ==============================================================================
# 5. MENAMPILKAN PETA JALUR & PROGRAM UTAMA
# ==============================================================================
def display_maze(path, title):
    print(f"\n{'='*15} {title} {'='*15}")
    display = [row[:] for row in maze]
    if path:
        for r, c in path[1:-1]:
            display[r][c] = "*"

    for row in display:
        print(" ".join(row))


if __name__ == "__main__":
    start = (0, 0)
    goal = (14, 14)

    # Menjalankan kedua algoritma
    d_path, d_explored, d_cost = dijkstra(start, goal)
    a_path, a_explored, a_cost = astar(start, goal)

    # Cetak visualisasi peta dengan jalur yang ditemukan
    display_maze(d_path, "HASIL JALUR DIJKSTRA")
    display_maze(a_path, "HASIL JALUR A*")

    # Tabel Perbandingan
    print("\n" + "=" * 50)
    print(f"{'Metrik':<25} | {'Dijkstra':<10} | {'A*':<10}")
    print("-" * 50)
    print(
        f"{'Status':<25} | {'Ditemukan':<10} | {'Ditemukan':<10}"
    )
    print(f"{'Total Biaya (Cost)':<25} | {d_cost:<10} | {a_cost:<10}")
    print(
        f"{'Jumlah Langkah (Steps)':<25} | {len(d_path)-1:<10} | {len(a_path)-1:<10}"
    )
    print(
        f"{'Node Dieksplorasi':<25} | {d_explored:<10} | {a_explored:<10}"
    )
    print("=" * 50)