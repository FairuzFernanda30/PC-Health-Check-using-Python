# PC Health Check Utility (English)

A lightweight Python utility to monitor computer health parameters (CPU, RAM, Storage/Disk usage, Uptime, Temperatures, and Battery Status) in real-time, and log the reports locally.

This program is built with a focus on privacy. It **does not collect or share any sensitive data** (such as IP addresses, MAC addresses, or usernames).

---

## 🚀 Key Features

- **CPU Monitoring & Temperature:** Displays current CPU usage percentage and CPU temperature (on Linux/macOS, or Windows with Admin rights).
- **GPU Monitoring & Temperature (NVIDIA):** Detects NVIDIA GPU model and queries its current core temperature via `nvidia-smi`.
- **RAM Monitoring:** Displays RAM usage percentage with detailed used and total capacities.
- **Storage (Disk) Monitoring:** Displays storage usage percentage with free capacity in GB.
- **Uptime Tracker:** Tracks how long the computer has been active since the last boot.
- **Battery Information:** Detects battery percentage, charging status (AC power vs battery), and estimated time remaining (for laptops).
- **Automated Logging:** Automatically saves reports to the `log_file/` folder with timestamped filenames.
- **Safe & Lightweight:** Uses only standard libraries and the `psutil` module.

---

## 🛠️ Prerequisites & Installation

Before running this utility, ensure you have **Python 3.12.1** and the required libraries installed.

1. **Clone or Download This Repository:**
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Install Dependencies:**
   Install the required `psutil` library using the provided `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 How to Run

Run the script using Python from your terminal or command prompt:

```bash
python pc_health.py
```

---

## 📋 Sample Report Output

The report displayed in the terminal and saved to the log files will look like this:

```text
==================================================
PC HEALTH CHECK REPORT
==================================================
Waktu: 2026-06-10 12:04:48
Komputer: LAPTOP-xxxxxxxx
Sistem: Windows 11
--------------------------------------------------
CPU usage: 9.5%
RAM usage: 87.7% (13 GB / 15 GB)
Storage usage: 99.5%
Disk usage: 99.5% (Free: 0 GB / Total 181 GB)
Uptime: 2 hari, 19 jam, 23 menit
--------------------------------------------------
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Suhu GPU: 47 C
--------------------------------------------------
Status Baterai: 77% (Di-charge (AC))
Sisa Waktu Baterai: Tersambung ke daya AC
==================================================
Health check selesai!
[SAVED] Laporan disimpan ke: log_file\health_log_20260610_120449.txt
```

---
---

# Utilitas Cek Kesehatan PC (Bahasa Indonesia)

Sebuah program utilitas ringan berbasis Python untuk memantau kesehatan komputer (penggunaan CPU, RAM, Penyimpanan/Disk, Uptime, Temperatur, dan Status Baterai) secara langsung (*real-time*) dan menyimpannya ke dalam file log secara lokal.

Program ini dibuat dengan fokus pada privasi, sehingga **tidak mengumpulkan atau membagikan data sensitif** (seperti IP address, MAC address, atau nama pengguna).

---

## 🚀 Fitur Utama

- **Pemantauan CPU & Suhu:** Menampilkan persentase penggunaan CPU saat ini beserta suhu CPU (didukung pada Linux/macOS, atau Windows dengan hak Administrator).
- **Pemantauan GPU & Suhu (NVIDIA):** Mendeteksi jenis GPU NVIDIA dan menampilkan suhu kerjanya saat ini via `nvidia-smi`.
- **Pemantauan RAM:** Menampilkan persentase penggunaan RAM beserta detail kapasitas yang terpakai dan total kapasitas.
- **Pemantauan Penyimpanan (Disk):** Menampilkan persentase penggunaan penyimpanan utama beserta sisa kapasitas (*free space*) dalam GB.
- **Waktu Aktif (Uptime):** Menghitung berapa lama komputer telah menyala sejak *boot* terakhir.
- **Informasi Baterai:** Mendeteksi persentase baterai, status pengisian daya (sedang di-charge atau tidak), dan estimasi sisa waktu pemakaian (khusus laptop).
- **Penyimpanan Log Otomatis:** Menyimpan laporan pemeriksaan ke dalam folder `log_file/` secara teratur dengan penamaan berbasis waktu (*timestamp*).
- **Aman & Ringan:** Hanya menggunakan pustaka standar dan modul `psutil`.

---

## 🛠️ Prasyarat & Instalasi

Sebelum menjalankan program ini, pastikan Anda telah menginstal **Python 3.x** dan pustaka dependensi yang diperlukan.

1. **Clone atau Unduh Repositori Ini:**
   ```bash
   git clone https://github.com/username/repo-name.git
   cd repo-name
   ```

2. **Instal Dependensi:**
   Instal pustaka `psutil` menggunakan file `requirements.txt` yang tersedia:
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Cara Menjalankan

Jalankan skrip menggunakan Python dari terminal atau command prompt Anda:

```bash
python pc_health.py
```

---

## 📋 Contoh Output Laporan

Laporan yang ditampilkan di terminal dan disimpan di dalam file log akan terlihat seperti ini:

```text
==================================================
PC HEALTH CHECK REPORT
==================================================
Waktu: 2026-06-10 12:04:48
Komputer: LAPTOP-xxxxxxxx
Sistem: Windows 11
--------------------------------------------------
CPU usage: 9.5%
RAM usage: 87.7% (13 GB / 15 GB)
Storage usage: 99.5%
Disk usage: 99.5% (Free: 0 GB / Total 181 GB)
Uptime: 2 hari, 19 jam, 23 menit
--------------------------------------------------
GPU: NVIDIA GeForce RTX 3050 6GB Laptop GPU
Suhu GPU: 47 C
--------------------------------------------------
Status Baterai: 77% (Di-charge (AC))
Sisa Waktu Baterai: Tersambung ke daya AC
==================================================
Health check selesai!
[SAVED] Laporan disimpan ke: log_file\health_log_20260610_120449.txt
```
