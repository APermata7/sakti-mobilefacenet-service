<p align="center">
  <img src="https://drive.google.com/thumbnail?id=1H4wEo0GWMfvY6SQcp_e7bVzZ10VRTufI&sz=w2000" alt="Banner SAKTI MobileFaceNet Service" width="100%">
</p>

<h1 align="center">
SAKTI MobileFaceNet Service
</h1>

<p align="center">
Layanan Verifikasi Wajah menggunakan MobileFaceNet dan InsightFace untuk Sistem Presensi KOPEGTEL Malang.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-3776AB?style=for-the-badge&logo=python" alt="Python">
  &nbsp;
  <img src="https://img.shields.io/badge/FastAPI-0.115-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  &nbsp;
  <img src="https://img.shields.io/badge/InsightFace-0.7.3-FF6B6B?style=for-the-badge" alt="InsightFace">
  &nbsp;
  <img src="https://img.shields.io/badge/ONNX-1.19.2-000000?style=for-the-badge&logo=onnx" alt="ONNX">
  &nbsp;
  <img src="https://img.shields.io/badge/cPanel-Deployment-FF6C2C?style=for-the-badge&logo=cpanel" alt="cPanel">
</p>

---

## 🎯 Tentang Proyek

**SAKTI MobileFaceNet Service** adalah layanan mikro (microservice) yang bertanggung jawab untuk melakukan **verifikasi wajah** menggunakan model **MobileFaceNet** dan library **InsightFace**.

Layanan ini digunakan oleh backend SAKTI untuk memvalidasi identitas karyawan saat melakukan presensi (check-in dan check-out). Dengan adanya layanan ini, sistem dapat memastikan bahwa karyawan yang melakukan presensi adalah orang yang sama dengan foto referensi yang tersimpan di database.

---

## 🚀 Tujuan Pengembangan

Pengembangan layanan ini bertujuan untuk:

- Menyediakan API verifikasi wajah yang cepat dan akurat.
- Mendukung validasi identitas karyawan secara real-time.
- Mengintegrasikan model MobileFaceNet untuk pengenalan wajah.
- Menyediakan layanan yang ringan dan dapat di-deploy secara terpisah.
- Mempermudah proses presensi dengan teknologi face recognition.

---

## ✨ Fitur Utama

### 🔍 Verifikasi Wajah

- **Endpoint:** `POST /api/v1/verify`
- **Deskripsi:** Membandingkan dua gambar wajah (referensi dan selfie) dan menentukan apakah keduanya adalah orang yang sama.
- **Parameter:**
  - `reference_url` (string): URL gambar referensi (foto karyawan dari database)
  - `selfie_url` (string): URL gambar selfie (foto yang diambil saat presensi)
- **Response:**
  - `match` (boolean): Apakah wajah cocok
  - `similarity` (float): Skor kemiripan (0-1)
  - `threshold` (float): Ambang batas yang digunakan (0.65)
  - `message` (string): Pesan keterangan

### 📊 Health Check

- **Endpoint:** `GET /health`
- **Deskripsi:** Mengecek status kesehatan layanan.
- **Response:**
  - `status`: "ok"
  - `service`: "mobilefacenet-service"
  - `version`: "1.0.0"
  - `model`: Nama model yang digunakan
  - `threshold`: Ambang batas verifikasi
  - `provider`: Provider yang digunakan (CPU)

### 🎯 Konfigurasi Fleksibel

Layanan ini dapat dikonfigurasi melalui environment variables:

| Variable | Deskripsi | Default |
|----------|-----------|---------|
| `MODEL_NAME` | Nama model InsightFace | `buffalo_l` |
| `VERIFICATION_THRESHOLD` | Ambang batas kemiripan | `0.65` |
| `FACE_DET_SIZE` | Ukuran deteksi wajah | `640` |
| `PROVIDERS` | Provider inference (CPU/GPU) | `["CPUExecutionProvider"]` |
| `PORT` | Port aplikasi | `5002` |
| `RELOAD` | Auto-reload (development) | `false` |

---

## 🛠 Teknologi yang Digunakan

| Komponen | Teknologi |
|----------|-----------|
| Bahasa Pemrograman | Python 3.9 |
| Framework | FastAPI |
| Face Recognition | InsightFace 0.7.3 |
| Model | MobileFaceNet (buffalo_l) |
| Inference Engine | ONNX Runtime 1.19.2 |
| Image Processing | OpenCV, Pillow |
| Deployment | cPanel (Passenger + a2wsgi) |

---

## 🏛 Arsitektur Sistem

Layanan ini berjalan sebagai microservice terpisah dan berkomunikasi dengan backend utama melalui REST API.

```
Backend (SAKTI)

↓

POST /api/v1/verify

↓

MobileFaceNet Service

↓

Load Model (Lazy Loading)

↓

Ekstrak Embedding

↓

Cosine Similarity

↓

match = similarity >= threshold

↓

Response
```

Keuntungan:

- Mudah diskalakan secara horizontal
- Dapat di-deploy secara terpisah
- Mengurangi beban backend utama
- Memudahkan maintenance dan update

---

## 📂 Struktur Folder

```text
sakti_mobilefacenet_service/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── health.py
│   │   │   └── verify.py 
│   │   └── schemas/
│   │       └── face.py
│   ├── core/
│   │   └── config.py
│   ├── infrastructure/
│   │   └── ml/
│   │       └── model_loader.py 
│   ├── services/
│   │   └── face_service.py  
│   ├── utils/
│   │   ├── image_utils.py  
│   │   └── logger.py          
│   └── main.py                
│
├── models_data/              
├── logs/   
├── passenger_wsgi.py
├── requirements.txt           
├── .env.example                            
└── README.md
```

## ⚙ Instalasi

Clone repository

```bash
git clone https://github.com/APermata7/sakti_mobilefacenet_service.git
```

Masuk ke direktori proyek

```bash
cd sakti_mobilefacenet_service
```

Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate     # Windows
```

Install dependency

```bash
pip install -r requirements.txt
```
---

## 🔑 Konfigurasi Environment

Salin file contoh environment.

```bash
cp .env.example .env
```

---

## ▶ Menjalankan Aplikasi

### Development

```bash
uvicorn app.main:app --host 0.0.0.0 --port 5002 --reload
```

Aplikasi akan berjalan pada

```
http://localhost:5002
```

### Production

Aplikasi dideploy di cPanel menggunakan Passenger WSGI dengan file passenger_wsgi.py.

Domain:

```bash
https://presensi.kopegtelmalang.co.id
```
---

## 📡 API Endpoint

Layanan menyediakan beberapa endpoint:

| Method | Endpoint | Deskripsi |
|-------|-----------|-----------------|
| **GET** | `/health` | Health check |
| **GET** | `/docs` | Swagger UI Documentation |
| **GET** | `/redoc` | ReDoc Documentation |
| **POST** | `/api/v1/verify` | Verifikasi wajah |