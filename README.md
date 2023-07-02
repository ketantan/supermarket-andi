# supermarket-andi
Aplikasi sederhana untuk membantu pelanggan Supermarket Andi berbelanja secara mandiri (self-service checkout).
Aplikasi ini menggunakan bahasa pemrograman Python.

# latar belakang permasalahan
1. Andi memiliki sebuah usaha supermarket.
2. Dalam rangka menyederhanakan dan meningkatkan efisiensi proses di supermarketnya, Andi berencana untuk mengimplementasikan sistem
self-service checkout.
3. Maka dari itu, Andi membutuhkan sebuah aplikasi yang dapat membantu pelanggannya untuk bisa berbelanja secara mandiri.

# persyaratan aplikasi
Aplikasi tersebut harus bisa membantu pelanggan untuk melakukan hal-hal berikut secara mandiri:
1. Memasukkan barang belanjaan sendiri, dengan mencantumkan nama barang, jumlah yang ingin dibeli, dan harga per piece dari barang tersebut.
2. Memanipulasi isi keranjang: menghapus barang di dalam keranjang (satu per satu, maupun sekaligus), mengganti nama barang / jumlah barang / harga per piece dari barang yang ada di dalam keranjang.
3. Mengecek isi keranjang, menghitung total belanjaan, dan juga mengenakan diskon sesuai dengan ketentuan yang berlaku.

# hasil test case
Test case #1: Customer menambahkan 2 item baru ke dalam keranjang.

<img width="225" alt="Screenshot 2023-07-02 at 16 27 38" src="https://github.com/ketantan/supermarket-andi/assets/137242990/2e93f59d-d7f8-4e12-bf83-07887fe65d49">

Test case #2: Customer menghapus item pasta gigi dari dalam keranjang.

<img width="225" alt="Screenshot 2023-07-02 at 16 28 01" src="https://github.com/ketantan/supermarket-andi/assets/137242990/073cb529-c831-491d-b3ab-62b5e35f5dd3">

Test case #3: Customer menghapus semua isi keranjang.

<img width="221" alt="Screenshot 2023-07-02 at 16 28 17" src="https://github.com/ketantan/supermarket-andi/assets/137242990/f7182485-5ffa-4eb2-b3cb-a6bd348b9584">

Test case #4: Customer mengisi barang belanjaan, menghitung total belanja, dan membayar.

<img width="230" alt="Screenshot 2023-07-02 at 16 28 39" src="https://github.com/ketantan/supermarket-andi/assets/137242990/5b7b3b91-04f9-421d-920f-ddd0cd854a84">
<img width="250" alt="Screenshot 2023-07-02 at 16 28 49" src="https://github.com/ketantan/supermarket-andi/assets/137242990/939113af-3221-4c27-b038-e06e2b55233e">

# kesimpulan dan evaluasi
Kesimpulan:
Dari project ini, saya baru pertama kali belajar bahasa pemrograman Python, object-oriented programming, dan sekaligus juga meng-upload dokumentasi ini ke github. Menurut saya, hal yang paling menantang adalah membentuk program menjadi modular, sulit sekali untuk saya menangkap bagaimana modul-modul ini bekerja. Dan hal kedua yang paling menantang adalah logika dari try-catch error, terlebih bagaimana membuat aplikasi tersebut untuk meminta inputan ulang jika terjadi kesalahan penginputan (yang ternyata solusinya lebih simpel dari yang bayangkan).

Hal yang menarik dan bikin saya ketagihan adalah merapihkan tampilan output, seperti belajar membuat tabel, dan error message yang rapi dan enak dibaca. Begitu pula dengan spacing antara aktivitas yang satu dengan lainnya.

Evaluasi untuk aplikasi yang lebih baik:
Kalau ke depannya saya punya staff atau kemampuan programming yang lebih hebat lagi, akan lebih baik kalau aplikasi ini bisa memiliki database. Sehingga aplikasi makin mirip dunia nyata, yang di mana customer tidak memasukkan nama item, tapi hanya kode yang kemudian akan disambungkan ke database inventori dari supermarket.
