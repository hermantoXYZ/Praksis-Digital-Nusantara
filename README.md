
# 🌐 IDPMI - Ikatan Dosen Pasar Modal Indonesia

Selamat datang di repository resmi website **IDPMI (Ikatan Dosen Pasar Modal Indonesia)**.  
Website ini dikembangkan sebagai portal digital resmi bagi para dosen, peneliti, dan praktisi pasar modal di Indonesia untuk berkolaborasi, berbagi pengetahuan, serta mengelola kegiatan organisasi secara profesional dan terintegrasi.

---

## 🚀 Tujuan Proyek

Platform ini dirancang untuk:
- Menjadi wadah komunikasi dan kolaborasi antar dosen pasar modal di Indonesia.  
- Menyediakan informasi terkini seputar penelitian, pendidikan, dan kegiatan pengabdian masyarakat.  
- Menjadi pusat data keanggotaan, kepakaran, dan publikasi anggota IDPMI.  
- Mendukung tata kelola organisasi IDPMI yang lebih modern, transparan, dan efisien.

---

## 🧩 Fitur Utama

### 👤 **Manajemen Pengguna**
- **Multi-role system**:
  - **Admin**: mengelola seluruh data, pengguna, dan konten.
  - **Anggota / Dosen**: mengelola profil, publikasi, penelitian, dan kegiatan akademik.
  - **Publik**: dapat mengakses berita, artikel, dan direktori pakar.
- Registrasi & autentikasi menggunakan sistem Django Authentication.
- Profil pengguna lengkap: biodata, foto, akun akademik (Google Scholar, Sinta, Scopus, LinkedIn).

### 🎓 **Modul Kepakaran Dosen**
- Data kepakaran disusun berdasarkan bidang ilmu dan program studi.  
- Setiap dosen dapat memilih dan menampilkan **Bidang Kepakaran**, **Minat Penelitian**, dan **Program Studi**.  
- Fitur **Tagging (Django Taggit)** untuk klasifikasi otomatis minat penelitian.

### 📚 **Modul Pendidikan, Penelitian, dan Pengabdian**
- Input dan manajemen data kegiatan tridarma dosen:
  - **Pendidikan**: kegiatan pengajaran dan kurikulum.
  - **Penelitian**: publikasi, proyek riset, dan kolaborasi.
  - **Pengabdian**: kegiatan sosial dan pemberdayaan masyarakat.
- Data bisa difilter per dosen, bidang, atau tahun kegiatan.

### 📰 **Portal Berita & Publikasi**
- Modul **PostNews** untuk menampilkan berita terkini IDPMI.
- Kategori artikel dan berita berdasarkan topik pasar modal, ekonomi, dan pendidikan.
- Tampilan berita dengan thumbnail, slug URL otomatis, dan SEO friendly.

### 🧠 **Direktori Pakar (Pakar IDPMI)**
- Halaman khusus berisi daftar dosen beserta kepakaran dan afiliasinya.  
- Pencarian dan filter berdasarkan:
  - Nama
  - Bidang Kepakaran
  - Program Studi
  - Minat Penelitian

### 🏛️ **Organisasi & Keanggotaan**
- Struktur organisasi IDPMI ditampilkan secara dinamis.
- Modul **Organisasi** untuk menampilkan dewan pengurus dan bidang kerja.
- Data keanggotaan dikelola melalui modul **UserAnggota**.

### 📦 **Modul Lainnya**
- **Category & Theme**: pengelompokan tema digital (seperti template undangan digital IDPMI).
- **Asset Management**: pengelolaan aset dengan QR Code.
- **Export Data**: fitur ekspor CSV/Excel untuk admin.

---

## 🧱 Teknologi yang Digunakan

| Kategori | Teknologi |
|-----------|------------|
| Framework | Django 5.x |
| Database | MySQL (via XAMPP atau server production) |
| Frontend | HTML5, CSS3, JavaScript (dengan Tailwind & FontAwesome) |
| Template Engine | Django Template |
| Admin Panel | django-admin-interface / django-unfold |
| Tagging System | django-taggit |
| Import/Export Data | django-import-export |
| Authentication | Django Auth System |
| Version Control | Git & GitHub |

---

## 🧭 Struktur Proyek

```

idpmi/
├── accounts/           # Modul akun dan manajemen pengguna
├── kepakaran/          # Modul kepakaran dosen dan bidang penelitian
├── pendidikan/         # Modul pendidikan
├── penelitian/         # Modul penelitian
├── pengabdian/         # Modul pengabdian masyarakat
├── organisasi/         # Struktur organisasi dan pengurus
├── services/           # Modul layanan tambahan (tema, aset, dll.)
├── static/             # File CSS, JS, dan gambar statis
├── templates/          # Template HTML
├── core/               # Pengaturan utama Django (urls, settings)
└── manage.py

````

---

## ⚙️ Instalasi & Konfigurasi

### 1. Clone Repository
```bash
git clone https://github.com/username/idpmi.git
cd idpmi
````

### 2. Buat Virtual Environment

```bash
python -m venv env
source env/bin/activate  # macOS / Linux
env\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Database

Edit file `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'idpmi_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Jalankan Server

```bash
python manage.py runserver
```

Akses di: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Login Default (Development)

| Role  | Username | Password |
| ----- | -------- | -------- |
| Admin | admin    | admin123 |

---

## 📊 Screenshot (opsional)

> Tambahkan tangkapan layar halaman dashboard, direktori pakar, dan berita di sini jika sudah tersedia.

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
Dapat digunakan dan dimodifikasi untuk tujuan pendidikan dan pengembangan komunitas akademik.

---

## 🤝 Kontributor

* **Andi Hermanto** – Developer utama
* Tim IT & Riset IDPMI
* Komunitas Dosen Pasar Modal Indonesia

---

## 💬 Kontak

📧 Email: [info@idpmi.or.id](mailto:info@idpmi.or.id)
🌍 Website: [https://idpmi.or.id](https://idpmi.or.id)
🏢 Sekretariat: Fakultas Ekonomi dan Bisnis, [Universitas / Lembaga terkait]

---

> *"Bersama membangun ekosistem pasar modal yang akademis, inklusif, dan berintegritas."*
> **— IDPMI (Ikatan Dosen Pasar Modal Indonesia)**

```

---

Apakah kamu ingin saya buatkan **versi README yang lebih singkat dan ringkas** (misalnya untuk tampilan GitHub utama), atau tetap versi **panjang seperti di atas** untuk dokumentasi lengkap internal proyek Django-mu?
```
