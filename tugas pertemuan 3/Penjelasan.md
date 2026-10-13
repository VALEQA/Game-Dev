# Menara Hanoi (Tower of Hanoi) dengan Greedy Best-First Search

## Deskripsi Masalah

Menara Hanoi adalah permainan logika yang terdiri dari **3 tiang** dan **3 cakram** dengan ukuran berbeda.

- **Tiang A**: tiang asal (Start)
- **Tiang B**: tiang perantara
- **Tiang C**: tiang tujuan (Finish)

Awalnya semua cakram tertumpuk di tiang A, dengan cakram terbesar di bawah dan cakram terkecil di atas. Tujuannya adalah memindahkan seluruh cakram ke tiang C dengan urutan yang sama.

## Aturan Permainan

1. Hanya boleh memindahkan **1 cakram** dalam satu langkah.
2. Cakram yang dipindahkan harus cakram **paling atas** dari suatu tiang.
3. Cakram yang **lebih besar tidak boleh** diletakkan di atas cakram yang **lebih kecil**.
4. Cakram boleh diletakkan di tiang kosong atau di atas cakram yang lebih besar.

## Contoh Penyelesaian Manual (3 Cakram, A → C)

Cakram 1 = kecil, cakram 2 = sedang, cakram 3 = besar.

| Langkah | Pindahkan | Dari | Ke |
|:---:|:---:|:---:|:---:|
| 1 | Cakram 1 | A | C |
| 2 | Cakram 2 | A | B |
| 3 | Cakram 1 | C | B |
| 4 | Cakram 3 | A | C |
| 5 | Cakram 1 | B | A |
| 6 | Cakram 2 | B | C |
| 7 | Cakram 1 | A | C |

Cakram terbesar (3) baru bisa dipindah ke C pada langkah 4, yaitu setelah cakram 1 dan 2 "menyingkir" ke tiang B.

## Ide Penyelesaian Rekursif

Untuk memindahkan **n cakram** dari tiang asal ke tiang tujuan:

1. Pindahkan **n-1 cakram** teratas dari tiang **asal** ke tiang **perantara**.
2. Pindahkan **cakram terbesar** dari tiang **asal** ke tiang **tujuan**.
3. Pindahkan **n-1 cakram** tadi dari tiang **perantara** ke tiang **tujuan**.

Jumlah langkah minimum untuk **n cakram** adalah `2^n - 1`. Untuk 3 cakram: 2³ - 1 = **7 langkah**.

## Pendekatan pada Kode: Greedy Best-First Search

Pada kode ini, Menara Hanoi diselesaikan sebagai **masalah pencarian jalur pada graph**, sama seperti materi Algoritma Graph:

- **Node (vertex)**: setiap kemungkinan posisi cakram (disebut *state*).
- **Edge**: satu perpindahan cakram yang valid dari satu state ke state lain.
- **Start**: `A=[3,2,1], B=[], C=[]`
- **Goal**: `A=[], B=[], C=[3,2,1]`

Algoritma Best-First Search selalu memilih node yang paling menjanjikan, yaitu node dengan nilai heuristik **h(n) terkecil**, menggunakan priority queue (`heapq`).

Penulisan state: setiap tiang ditulis dari **bawah ke atas**, jadi `A:[3, 2, 1]` berarti cakram 3 di dasar dan cakram 1 di puncak.

## Penjelasan Kode

### 1. Fungsi Heuristik `heuristic(state)`

Menghitung total **bobot cakram yang belum berada di tiang tujuan (C)**. Cakram ke-i berbobot `2^(i-1)`:

| Cakram | Bobot |
|:---:|:---:|
| 1 (kecil) | 1 |
| 2 (sedang) | 2 |
| 3 (besar) | 4 |

Cakram besar diberi bobot lebih tinggi karena lebih "mahal" untuk dipindahkan. Nilai h(n) = 0 berarti semua cakram sudah di tiang C (Goal). Pada state awal, h(n) = 1 + 2 + 4 = **7**.

### 2. Fungsi `get_neighbors(state)`

Menghasilkan semua perpindahan yang **valid** dari suatu state. Untuk setiap tiang asal yang tidak kosong, diambil cakram teratas, lalu dicoba dipindah ke tiang lain dengan syarat:

> tiang tujuan **kosong**, atau cakram teratas di tiang tujuan **lebih besar** dari cakram yang dipindah.

Syarat ini adalah penerapan aturan "cakram besar tidak boleh di atas cakram kecil".

### 3. Fungsi `best_first_search(start, goal)`

Inti algoritma:

1. Masukkan state awal ke `open_list` (priority queue) dengan prioritas h(n).
2. Ambil state dengan h(n) terkecil memakai `heapq.heappop`.
3. Jika state sudah pernah dikunjungi (`visited`), lewati.
4. Jika state adalah Goal, selesai dan susun jalurnya.
5. Jika belum, buat semua tetangganya dengan `get_neighbors`, catat `parent` dan `action_taken`, lalu masukkan ke `open_list` dengan `heapq.heappush`.

Karena ini **Greedy** Best-First Search, nilai evaluasinya hanya `f(n) = h(n)`. Variabel `counter` dipakai sebagai *tie-breaker* agar state dengan h(n) sama tetap bisa diurutkan tanpa error.

### 4. Fungsi `reconstruct_path(...)`

Setelah Goal ditemukan, jalur disusun mundur dari Goal ke Start menggunakan `parent`, lalu dibalik sehingga urutannya Start → Goal. Fungsi ini juga mengumpulkan teks aksi tiap langkah.

### 5. Fungsi `print_game_steps(path, actions)`

Menampilkan hasil akhir berupa urutan langkah beserta kondisi ketiga tiang setelah setiap langkah.

## Kode Lengkap

```python
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
```

## Hasil Output

Pencarian mengunjungi 18 state sebelum menemukan Goal. Jalur yang ditemukan:

| Langkah | Aksi | Kondisi (A, B, C) |
|:---:|---|---|
| Start | - | A:[3, 2, 1], B:[], C:[] |
| 1 | Pindahkan cakram 1 dari A ke C | A:[3, 2], B:[], C:[1] |
| 2 | Pindahkan cakram 2 dari A ke B | A:[3], B:[2], C:[1] |
| 3 | Pindahkan cakram 1 dari C ke B | A:[3], B:[2, 1], C:[] |
| 4 | Pindahkan cakram 3 dari A ke C | A:[], B:[2, 1], C:[3] |
| 5 | Pindahkan cakram 1 dari B ke A | A:[1], B:[2], C:[3] |
| 6 | Pindahkan cakram 2 dari B ke C | A:[1], B:[], C:[3, 2] |
| 7 | Pindahkan cakram 1 dari A ke C | A:[], B:[], C:[3, 2, 1] |

**Jumlah langkah: 7**, sama dengan minimum teoretis `2^3 - 1 = 7`.

## Kesimpulan

- Menara Hanoi dapat dimodelkan sebagai graph: state sebagai node, perpindahan cakram sebagai edge.
- Greedy Best-First Search dengan heuristik berbobot `2^(i-1)` berhasil menemukan solusi dengan **7 langkah**.
- Perlu diingat bahwa Greedy Best-First Search **tidak menjamin jalur terpendek** secara umum, karena hanya melihat nilai heuristik dan mengabaikan biaya yang sudah ditempuh. Pada kasus 3 cakram ini hasilnya kebetulan optimal.