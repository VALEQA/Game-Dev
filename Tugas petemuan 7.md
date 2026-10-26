Cari teori mengenai Steering Behaviour & Collison Avoidance, lalu jelaskan. 
apakah teori yang ada dapat memiliki persamaan matematis? jika iya / tidak jelaskan. 
bagaimana jika diterapkan menggunakan python ? apakah dapat dilakukan simulasi secara dasar ? 
buatlah studi kasus yang berkaitan dengan Steering Behaviour & Collison Avoidance

Jawaban :
1.
  Steering Behaviour adalah kumpulan aturan gerak yang menentukan bagaimana sebuah karakter mengarahkan dirinya sendiri di dalam lingkungan game atau animasi. 
  Setiap aturan menjawab satu kebutuhan gerak, misalnya seek untuk mendekati suatu tujuan, flee untuk menjauhi bahaya, arrival untuk melambat lalu berhenti tepat di tujuan, 
  serta leader following atau flocking untuk mengikuti pemimpin atau bergerak bersama kelompok. Bahasa kasarrnya adalah bagaimana cara bergeraknya sebuah karakter 

  sedangkan 
  Collision avoidance adalah salah satu aturan dalam steering behaviors yang bertugas khusus mencegah tabrakan dengan karakter lain yang sedang bergerak. 
  Pertama, karakter memeriksa karakter-karakter lain di sekitarnya, lalu memprediksi apakah mereka akan berpapasan terlalu dekat dengan melihat arah dan kecepatan masing-masing. 
  Jika ada kemungkinan tabrakan, karakter menghitung di mana dan kapan titik bahaya itu akan terjadi.
  dengan demikian Collision avoidance bisa disebut bagaimana karakter ini dapat menghidar dari sebuah rintangan/tabrakan 

2. Ya, teori ini dapat dinyatakan secara matematis karena semua perilakunya hanyalah perhitungan arah dan jarak yang sederhana.
   Setiap perilaku menghasilkan satu dorongan arah yang menentukan ke mana karakter bergerak, misalnya menuju target atau menjauhi bahaya.
   Pada collision avoidance, komputer menghitung apakah dua karakter akan berpapasan terlalu dekat berdasarkan posisi dan kecepatan keduanya, lalu mengarahkan karakter menjauhi titik tabrakan.
   Jika ada beberapa perilaku sekaligus, dorongan masing-masing dijumlahkan sesuai tingkat kepentingannya.
   knpa si bisa dibilang matematis karena mengguanakan vektor untuk menentukan hasil pergerakan

3. Jika diterapkan menggunakan Python, simulasi dasar steering behaviors dan collision avoidance dapat dilakukan.
   Python menyediakan pustaka seperti NumPy untuk menghitung vektor (posisi, kecepatan, dan arah dorongan)
   serta Matplotlib untuk menampilkan hasil gerak karakter dalam bentuk gambar atau animasi.
   dengan cara setiap karakter diberi posisi awal,setiap karakter diberi posisi awal, kecepatan, dan tujuan.
   trus setiap langkah waktu, komputer menghitung dorongan arah dari tiap perilaku, yaitu dorongan menuju tujuan (seek atau arrival)
   dan dorongan menghindar bila diperkirakan akan berpapasan terlalu dekat dengan karakter lain (collision avoidance).
   lalu kedua dorongan dijumlahkan, dibatasi nilai maksimumnya, lalu dipakai untuk memperbarui kecepatan dan posisi karakter.
   Proses ini diulang terus sampai karakter tiba di tujuan.

4. Studi kasus ini membahas navigasi AGV (Automated Guided Vehicle) di gudang logistik pintar, tempat puluhan robot mengangkut rak barang ke stasiun pengepakan secara bersamaan.
   Jika robot hanya diprogram berjalan lurus ke target (seek), robot akan sering menabrak rak statis atau saling berhadapan di lorong sempit. Untuk mengatasinya, AGV memakai arrival agar bergerak cepat menuju rak lalu melambat halus saat mendekat sehingga barang tidak jatuh akibat rem mendadak.
   AGV juga memakai collision avoidance dengan sensor LiDAR yang memindai bagian depan, sehingga bila ada pekerja atau robot lain melintas, AGV bergeser ke sisi lorong tanpa berhenti total, ditambah separation untuk menjaga jarak aman antar-robot yang berjalan beriringan.
   Hasilnya, lalu lintas gudang lebih lancar, waktu pengambilan barang lebih efisien, dan risiko tabrakan berkurang.
