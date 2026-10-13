import heapq

# 1. FUNGSI HEURISTIK
def heuristic(state, goal_peg=2):
    """
    Menghitung bobot cakram yang belum berada di tiang tujuan (Goal = tiang C / index 2).
    Cakram ke-i berbobot 2**(i - 1).
    """
    h = 0
    for peg_idx, peg in enumerate(state):
        if peg_idx != goal_peg:
            for disk in peg:
                h += 2 ** (disk - 1)
    return h

# 2. GENERATE GERAKAN VALID
def get_neighbors(state):
    """
    Mengecek semua kemungkinan perpindahan cakram yang valid.
    """
    neighbors = []
    peg_names = ['A', 'B', 'C']
    for src in range(3):
        if not state[src]:
            continue
        disk = state[src][-1]  # Cakram teratas pada tiang asal
        for dst in range(3):
            if src == dst:
                continue
            # Syarat: Tiang tujuan kosong ATAU cakram teratas lebih besar
            if not state[dst] or state[dst][-1] > disk:
                new_state = [list(peg) for peg in state]
                new_state[src].pop()
                new_state[dst].append(disk)
                action_text = f"Pindahkan cakram {disk} dari {peg_names[src]} ke {peg_names[dst]}"
                neighbors.append((tuple(tuple(p) for p in new_state), action_text))
    return neighbors

def format_state(state):
    names = ['A', 'B', 'C']
    return "[" + ", ".join(f"{names[i]}:{list(state[i])}" for i in range(3)) + "]"

# 3. ALGORITMA GREEDY BEST-FIRST SEARCH
def best_first_search(start, goal):
    # Priority Queue: (f(n), tie_counter, state)
    open_list = []
    counter = 0
    heapq.heappush(open_list, (heuristic(start), counter, start))

    # Menyimpan node yang sudah dikunjungi
    visited = set()

    # Menyimpan parent untuk reconstruct path
    parent = {start: None}
    action_taken = {}

    print("Output Pencarian:\n")
    while open_list:
        # Mengambil node dengan f(n) terkecil
        f, _, current = heapq.heappop(open_list)

        # Jika sudah dikunjungi, skip
        if current in visited:
            continue

        visited.add(current)
        print(f"Visit {format_state(current)}, h(n) = {f}")

        # Jika goal ditemukan
        if current == goal:
            return reconstruct_path(parent, action_taken, goal)

        # Mengecek semua kemungkinan gerakan
        for next_state, action in get_neighbors(current):
            if next_state not in visited:
                if next_state not in parent:
                    parent[next_state] = current
                    action_taken[next_state] = action
                
                counter += 1
                # Greedy Best-First Search: f(n) = h(n)
                h = heuristic(next_state)
                heapq.heappush(open_list, (h, counter, next_state))

    return None, None

# 4. RECONSTRUCT PATH
def reconstruct_path(parent, action_taken, goal):
    """
    Membuat kembali path dari Goal menuju Start.
    """
    path = []
    actions = []
    current = goal
    while current is not None:
        path.append(current)
        if current in action_taken:
            actions.append(action_taken[current])
        current = parent[current]
    
    # Balik urutan: Start -> Goal
    path.reverse()
    actions.reverse()
    return path, actions

# 5. MENAMPILKAN VISUALISASI LANGKAH
def print_game_steps(path, actions):
    print("\nVisualisasi Langkah Game:")
    for i in range(len(path)):
        if i == 0:
            print("Keadaan Awal (Start):")
        else:
            print(f"Langkah {i}: {actions[i - 1]}")
        print(f"  {format_state(path[i])}")

# ==================== MAIN EXECUTION ====================
# Start: A = [3, 2, 1], B = [], C = []
start = ((3, 2, 1), (), ())
# Goal:  A = [], B = [], C = [3, 2, 1]
goal = ((), (), (3, 2, 1))

path, actions = best_first_search(start, goal)

if path:
    print("\nPath ditemukan:")
    print(" -> \n".join(format_state(p) for p in path))
    print(f"\nJumlah langkah: {len(path) - 1}")
    print_game_steps(path, actions)
else:
    print("\nPath tidak ditemukan.")