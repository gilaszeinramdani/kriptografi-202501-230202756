# Laporan Praktikum Kriptografi
Minggu ke-: 13  
Topik: TinyChain – Proof of Work (PoW)
Nama: Gilas Zein Ramdani  
NIM: 230202756  
Kelas: 5IKRB 

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami peran fungsi hash dalam blockchain, melakukan simulasi mekanisme Proof of Work (PoW), serta menganalisis aspek keamanan cryptocurrency berbasis kriptografi.

---

## 2. Dasar Teori
Blockchain merupakan sistem pencatatan terdistribusi yang menyimpan data dalam bentuk blok yang saling terhubung menggunakan fungsi hash kriptografi. Setiap blok memiliki hash unik yang bergantung pada isi data, waktu pembuatan, nonce, dan hash blok sebelumnya. Hal ini menjamin integritas data karena perubahan kecil pada data akan menghasilkan hash yang berbeda.

Proof of Work (PoW) adalah mekanisme konsensus yang digunakan untuk menambahkan blok baru ke dalam blockchain. Pada PoW, miner harus mencari nilai nonce yang menghasilkan hash dengan pola tertentu, misalnya diawali sejumlah nol. Proses ini membutuhkan usaha komputasi sehingga menyulitkan pemalsuan data.
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
- Pertanyaan 1: Mengapa fungsi hash sangat penting dalam blockchain?
- Jawab       : Fungsi hash menjamin integritas data dan menghubungkan setiap blok secara kriptografis sehingga perubahan data dapat terdeteksi.
- Pertanyaan 2: Bagaimana Proof of Work mencegah double spending?
- Jawab       : PoW mempersulit pemalsuan transaksi karena setiap perubahan data memerlukan proses mining ulang yang mahal secara komputasi.
- Pertanyaan 3: Apa kelemahan PoW dalam hal efisiensi energi?
- Jawab       : PoW membutuhkan daya komputasi dan energi listrik yang besar sehingga kurang efisien dan berdampak pada lingkungan.
---

## 8. Kesimpulan
Dari praktikum ini dapat disimpulkan bahwa fungsi hash dan Proof of Work merupakan komponen utama dalam menjaga keamanan blockchain. Meskipun efektif, PoW memiliki kelemahan dalam konsumsi energi yang tinggi.
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
