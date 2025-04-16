
```markdown
# Kontrol Servo dengan Webcam dan Flask

Proyek ini memungkinkan kontrol **servo motor** menggunakan deteksi sudut dari **tangan** yang dikenali melalui webcam. Aplikasi web ini menggunakan **Flask** untuk backend dan **MediaPipe** untuk mendeteksi posisi tangan dan menghitung sudut jari/jempol.

## Fitur
- Menggunakan webcam untuk mendeteksi posisi tangan.
- Menghitung sudut antara jempol dan telunjuk untuk kontrol.
- Tampilan responsif yang dapat diakses melalui berbagai perangkat.
- WebSocket atau API untuk mengirim data ke perangkat keras (seperti servo).

## Teknologi yang Digunakan
- **Python**: Bahasa pemrograman utama.
- **Flask**: Framework untuk aplikasi web.
- **MediaPipe**: Untuk mendeteksi landmark tangan secara real-time.
- **OpenCV**: Untuk pemrosesan gambar dan video.

## Prasyarat
- **Python 3.9+**
- **Pip** (untuk mengelola dependensi)

## Instalasi
1. **Clone repository** ini:
   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```

2. **Buat virtual environment** dan aktifkan:
   - Di Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - Di macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instal dependensi**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:
   ```bash
   python backend/app.py
   ```

5. **Akses aplikasi** di browser:
   - Buka **http://localhost:5000** di browser pilihan kamu.

## Menjalankan Aplikasi
1. **Setelah aplikasi berjalan**, webcam akan menampilkan video real-time.
2. **Sudut antara jempol dan telunjuk** akan dihitung dan ditampilkan di layar.
3. Jika ingin mengontrol servo atau perangkat lainnya, kamu bisa menambahkan logika untuk mengirim data sudut ke perangkat keras melalui **serial port** atau API.

## Struktur Folder
```
servohand/
├── backend/
│   ├── app.py               # File utama untuk menjalankan Flask
│   ├── camera.py            # Untuk pengolahan webcam dan deteksi tangan
│   ├── servo_control.py     # Untuk mengirimkan data ke servo (optional)
│   └── templates/
│       └── index.html       # Halaman web utama
├── venv/                    # Virtual environment
├── .gitignore               # Mengabaikan file/folder tertentu di Git
├── requirements.txt         # Daftar dependensi Python
└── README.md                # Dokumentasi proyek ini
```

## Menggunakan MediaPipe untuk Deteksi Tangan
Proyek ini menggunakan **MediaPipe Hands** untuk mendeteksi landmark tangan secara real-time. Di dalam kode ini, kita menghitung sudut antara jempol dan telunjuk untuk mendapatkan **gesture** yang bisa diubah menjadi aksi (seperti menggerakkan servo).

## Kontribusi
Jika kamu ingin berkontribusi dalam proyek ini, silakan lakukan **fork**, lakukan **modifikasi** pada kode, dan buat **pull request**. Pastikan kamu mengikuti standar pengkodean yang ada.

## Lisensi
Proyek ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

```

---

### Penjelasan:

- **Fitur**: Menjelaskan fitur utama dari aplikasi (kontrol servo dengan tangan via webcam).
- **Teknologi**: Memberikan gambaran singkat tentang teknologi yang digunakan (Python, Flask, MediaPipe, OpenCV).
- **Instalasi**: Menyediakan instruksi untuk mengatur proyek di lokal, termasuk langkah-langkah untuk meng-clone repository, membuat virtual environment, dan menginstal dependensi.
- **Menjalankan Aplikasi**: Menjelaskan cara menjalankan aplikasi dan mengaksesnya melalui browser.
- **Struktur Folder**: Memberikan gambaran tentang struktur folder proyek.
- **Penggunaan MediaPipe**: Menjelaskan cara MediaPipe digunakan untuk mendeteksi tangan dan sudut jari.
- **Kontribusi**: Mendorong orang untuk berkontribusi dengan memberi instruksi cara fork dan pull request.
- **Lisensi**: Informasi lisensi untuk proyek ini (dalam hal ini MIT License).

---

