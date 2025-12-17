# Laporan Praktikum Kriptografi
Minggu ke-: 10  
Topik: Public Key Infrastructure (PKI) & Certificate Authority  
Nama: Gilas Zein Ramdani  
NIM: 230202756  
Kelas: 5IKRB  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep Public Key Infrastructure (PKI) dan peran Certificate Authority (CA) dalam sistem keamanan modern. Mahasiswa diharapkan mampu membuat sertifikat digital sederhana, memahami proses verifikasi sertifikat, serta menjelaskan peran PKI dalam mendukung komunikasi aman seperti HTTPS/TLS.

---

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan sebuah kerangka kerja yang digunakan untuk mengelola kunci kriptografi asimetris dan sertifikat digital. PKI memungkinkan proses autentikasi, kerahasiaan, dan integritas data melalui penggunaan pasangan kunci publik dan kunci privat yang terikat pada identitas tertentu.

Certificate Authority (CA) adalah pihak tepercaya yang bertugas menerbitkan, menandatangani, dan memvalidasi sertifikat digital. Sertifikat digital berbasis standar X.509 berisi informasi identitas pemilik sertifikat beserta kunci publiknya, yang ditandatangani oleh CA menggunakan kunci privat CA. Dengan demikian, pihak lain dapat memverifikasi keaslian sertifikat menggunakan kunci publik CA.

Dalam praktiknya, PKI banyak digunakan pada protokol keamanan seperti HTTPS/TLS, email aman (S/MIME), dan tanda tangan digital. Keberadaan PKI memungkinkan pengguna untuk berkomunikasi secara aman di jaringan publik seperti internet.

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
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
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
- Pertanyaan 1: Apa fungsi utama Certificate Authority (CA)?
- Jawab       : CA berfungsi sebagai pihak tepercaya yang menerbitkan dan menandatangani sertifikat digital untuk menjamin keaslian identitas pemilik sertifikat.
- Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?
- Jawab       : Karena sertifikat self-signed tidak diverifikasi oleh pihak tepercaya sehingga mudah dipalsukan dan akan ditolak oleh browser.
- Pertanyaan 2: Bagaimana PKI mencegah serangan MITM dalam TLS/HTTPS?
- Jawab       : PKI mencegah MITM dengan memverifikasi identitas server melalui sertifikat yang ditandatangani CA tepercaya dan menggunakan enkripsi TLS.
---

## 8. Kesimpulan
Praktikum ini menunjukkan bahwa PKI memiliki peran penting dalam menjamin keamanan komunikasi digital. Dengan memahami proses pembuatan dan verifikasi sertifikat, mahasiswa dapat memahami bagaimana kepercayaan dibangun dalam sistem keamanan modern.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
```
commit 23f8ff59ee88d14cb6800c0178ad3ea36753993d (HEAD -> main, origin/main, origin/HEAD)
Author: gilaszeinramdani <gilaszeinramdani@gmail.com>
Date:   Wed Dec 17 11:55:38 2025 +0700

    week10-pki
```
