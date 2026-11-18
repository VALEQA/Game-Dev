# 🎮 Game Development — Kumpulan Tugas & Implementasi Algoritma

Kumpulan tugas mata kuliah **Game Development** (Teknik Informatika): jawaban teori beserta implementasi Python yang bisa langsung dijalankan. Fokusnya pada algoritma yang dipakai di dalam game — pencarian jalur (pathfinding), pencarian heuristik, dan perilaku gerak karakter (steering behaviour).

Semua skrip hanya memakai **standard library Python** (`heapq`, `math`) — tidak perlu install apa pun.

---

## 📚 Daftar Tugas

| # | Topik | Materi | Kode | Dokumentasi |
|---|---|---|---|---|
| 1 | AI Enemy: Deteksi Player + A* Pathfinding | Euclidean distance, threshold checking, algoritma A\*, path following | [snippet di jawaban](Tugas%20Pertemuan%201.md) | [Tugas Pertemuan 1.md](Tugas%20Pertemuan%201.md) |
| 3 | Menara Hanoi dengan Greedy Best-First Search | Representasi state, heuristic berbobot cakram, generate gerakan valid | [`tugas pertemuan 3/soal.py`](tugas%20pertemuan%203/soal.py) | [`Penjelasan.md`](tugas%20pertemuan%203/Penjelasan.md) |
| 4 | Perbandingan Dijkstra vs A\* pada Grid Berbobot | Terrain cost (jalan/lumpur), Manhattan heuristic, perbandingan jumlah node dieksplorasi | [`tugas pertemuan 4/pathfinding.py`](tugas%20pertemuan%204/pathfinding.py) | [`Penjelasan_Pathfinding.docx`](tugas%20pertemuan%204/Penjelasan_Pathfinding.docx) |
| 7 | Steering Behaviour & Collision Avoidance | Seek, flee, arrival, separation, prediksi tabrakan, studi kasus AGV | — (teori) | [Tugas petemuan 7.md](Tugas%20petemuan%207.md) |

---

## 🔍 Ringkasan Tiap Tugas

### Tugas 1 — AI Enemy di Dungeon
Enemy menjalankan siklus per frame: **deteksi** jarak ke player dengan Euclidean distance → **cek jangkauan** terhadap detection radius → jika masuk radius, cari jalur dengan **A\*** (`f(n) = g(n) + h(n)`, heuristic Manhattan) → **bergerak** mengikuti waypoint. Jika player di luar radius, enemy idle/patroli. Disertai flowchart Mermaid dan snippet implementasi `Enemy` class.

### Tugas 3 — Menara Hanoi (Greedy Best-First Search)
Menyelesaikan puzzle 3 tiang / 3 cakram sebagai persoalan pencarian ruang keadaan:
- **State**: tuple 3 tiang, masing-masing berisi cakram (mis. `((3,2,1), (), ())`).
- **Heuristic**: jumlah bobot cakram yang belum berada di tiang tujuan, dengan bobot cakram ke-*i* = `2^(i-1)`.
- **Suksesor**: semua perpindahan 1 cakram teratas yang legal (cakram besar tidak boleh menimpa cakram kecil).

Hasil: solusi **7 langkah** optimal, ditampilkan langkah demi langkah beserta visualisasi state tiap tiang.

### Tugas 4 — Dijkstra vs A\* pada Grid 15×15
Peta maze 15×15 dengan bobot medan berbeda (`S` start, `G` goal, `#` dinding, `.` jalan = cost 1, `~` lumpur = cost 3). Kedua algoritma dijalankan pada peta yang sama lalu dibandingkan.

Hasil eksekusi (dapat direproduksi):

| Metrik | Dijkstra | A\* |
|---|---|---|
| Status | Ditemukan | Ditemukan |
| Total biaya (cost) | 30 | 30 |
| Jumlah langkah | 30 | 30 |
| **Node dieksplorasi** | **133** | **46** |

Kesimpulan: keduanya menghasilkan jalur optimal dengan biaya identik, tetapi A\* mengeksplorasi **±65% lebih sedikit node** karena heuristic Manhattan mengarahkan pencarian menuju goal.

### Tugas 7 — Steering Behaviour & Collision Avoidance
Penjelasan teori (seek, flee, arrival, leader following, flocking; collision avoidance sebagai prediksi titik tabrakan dari posisi + kecepatan), pembuktian bahwa perilaku ini murni operasi vektor sehingga bisa dinyatakan secara matematis, rencana simulasi Python (NumPy + Matplotlib), dan studi kasus navigasi **AGV di gudang logistik pintar**.

---

## 🚀 Cara Menjalankan

Prasyarat: **Python 3.8+** (tanpa dependency eksternal).

```bash
# Menara Hanoi — Greedy Best-First Search
python "tugas pertemuan 3/soal.py"

# Perbandingan Dijkstra vs A*
python "tugas pertemuan 4/pathfinding.py"
```

Keduanya mencetak hasil langsung ke terminal (langkah penyelesaian / visualisasi peta dan tabel perbandingan).

---

## 📁 Struktur Folder

```text
Game-Dev/
├── Tugas Pertemuan 1.md                    # Teori + flowchart + snippet A* enemy AI
├── Tugas petemuan 7.md                     # Teori steering behaviour & collision avoidance
├── tugas pertemuan 3/
│   ├── soal.py                             # Implementasi Greedy Best-First Search (Hanoi)
│   ├── Penjelasan.md                       # Penjelasan aturan, heuristic, langkah manual
│   └── foto/                               # Screenshot soal & hasil
└── tugas pertemuan 4/
    ├── pathfinding.py                      # Dijkstra + A* + perbandingan metrik
    ├── Penjelasan_Pathfinding.docx         # Laporan penjelasan
    └── image.png                           # Screenshot hasil
```

---

## 🧹 Catatan

- `tugas pertemuan 4/tempCodeRunnerFile.py` adalah file sementara bawaan Code Runner dan tidak dipakai — aman dihapus.
- Nama folder/file mengikuti penomoran pertemuan; penulisan "petemuan" pada Tugas 7 dipertahankan sesuai nama asli file.
- Lisensi: bebas dipakai untuk keperluan belajar.
