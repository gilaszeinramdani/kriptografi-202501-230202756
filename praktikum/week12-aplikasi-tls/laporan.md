# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: Aplikasi TLS & E-commerce
Nama: Gilas Zein Ramdani 
NIM: 230202756 
Kelas: 5IKRB

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk menganalisis penerapan kriptografi pada protokol SSL/TLS, khususnya pada layanan email dan e-commerce. Mahasiswa diharapkan mampu memahami fungsi sertifikat digital, mekanisme enkripsi dalam transaksi online, serta mengevaluasi isu etika dan privasi dalam penggunaan kriptografi di kehidupan sehari-hari.
---

## 2. Dasar Teori
Transport Layer Security (TLS) adalah protokol keamanan yang digunakan untuk melindungi komunikasi data melalui jaringan dengan menyediakan enkripsi, autentikasi, dan integritas data. TLS merupakan pengembangan dari Secure Socket Layer (SSL) dan saat ini menjadi standar keamanan pada komunikasi berbasis HTTPS.

Dalam TLS, sertifikat digital digunakan untuk memverifikasi identitas server melalui Certificate Authority (CA). Proses handshake TLS melibatkan pertukaran kunci menggunakan algoritma kriptografi asimetris seperti RSA atau ECDHE, kemudian komunikasi dilanjutkan menggunakan kriptografi simetris seperti AES karena lebih efisien.

Pada sistem e-commerce, TLS berperan penting dalam melindungi data sensitif seperti kredensial login dan informasi pembayaran. Tanpa enkripsi, data tersebut rentan terhadap serangan seperti Man-in-the-Middle (MITM) dan pencurian data.

---

## 3. Alat dan Bahan
(- Python 3.12  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
- Pertanyaan 1: Apa perbedaan utama antara HTTP dan HTTPS?
- Jawab       : HTTP tidak menggunakan enkripsi sehingga data dikirim dalam bentuk plaintext, sedangkan HTTPS menggunakan TLS untuk mengenkripsi data sehingga lebih aman.
- Pertanyaan 2: Mengapa sertifikat digital penting dalam komunikasi TLS?
- Jawab       : Sertifikat digital digunakan untuk memverifikasi identitas server dan mencegah serangan penyamaran atau Man-in-the-Middle.
- Pertanyaan 3: Bagaimana kriptografi mendukung privasi dan menimbulkan tantangan etika?
- Jawab       : Kriptografi melindungi privasi pengguna dengan enkripsi, namun dapat menyulitkan proses pengawasan dan penegakan hukum sehingga menimbulkan dilema etika dan hukum.
---

## 8. Kesimpulan
TLS dan kriptografi berperan penting dalam menjaga keamanan komunikasi digital, khususnya pada layanan email dan e-commerce. Penerapan TLS mampu melindungi data pengguna, namun juga memunculkan tantangan etika terkait privasi dan pengawasan.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
