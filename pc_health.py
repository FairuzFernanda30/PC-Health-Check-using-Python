# Import library (Import library)
import psutil
import platform
import datetime
import os
import subprocess
import shutil

def get_system_info():
    """Mengambil informasi dasar sistem operasi secara aman (tanpa data sensitif)."""
    # Informasi dasar sistem operasi (Basic operating system information)
    return {
        "waktu": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "komputer": platform.node(),
        "sistem": f"{platform.system()} {platform.release()}"
    }

def get_cpu_usage():
    """Mengambil persentase penggunaan CPU."""
    # Penggunaan CPU (CPU usage)
    return psutil.cpu_percent(interval=1)

def get_cpu_temperature():
    """Mengambil suhu CPU secara aman (lintas platform)."""
    # Suhu CPU (CPU temperature)
    
    # 1. Coba menggunakan psutil (bekerja langsung di Linux/macOS/WSL jika didukung)
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                if name.lower() in ['cpu', 'coretemp', 'k10temp']:
                    for entry in entries:
                        return f"{entry.current} C"
            for name, entries in temps.items():
                if entries:
                    return f"{entries[0].current} C"
    except AttributeError:
        pass

    # 2. Coba menggunakan query WMI di Windows (memerlukan hak Administrator)
    if platform.system() == "Windows":
        try:
            import wmi
            w = wmi.WMI(namespace="root/wmi")
            thermal_zones = w.MSAcpi_ThermalZoneTemperature()
            if thermal_zones:
                # Konversi Kelvin*10 ke Celsius
                temp_c = (thermal_zones[0].CurrentTemperature - 2732) / 10
                return f"{temp_c:.1f} C"
        except ImportError:
            # Pustaka 'wmi' opsional tidak terinstal
            pass
        except Exception as e:
            # Biasanya gagal karena 'Access denied' jika bukan Administrator
            if "Access denied" in str(e) or "0x80041003" in str(e):
                return "Perlu Admin"
            
    return "Tidak didukung"

def get_gpu_status():
    """Mengambil status GPU (NVIDIA) secara aman via nvidia-smi."""
    # Status GPU (GPU status)
    if not shutil.which("nvidia-smi"):
        return None
    
    try:
        # Jalankan nvidia-smi untuk mengambil nama dan suhu GPU
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,temperature.gpu", "--format=csv,noheader,nounits"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        output = result.stdout.strip()
        if output:
            parts = output.split(",")
            gpu_name = parts[0].strip()
            temp = parts[1].strip()
            return {
                "name": gpu_name,
                "temp": f"{temp} C"
            }
    except Exception:
        pass
    return None

def get_ram_usage():
    """Mengambil detail penggunaan RAM."""
    # Penggunaan RAM (RAM usage)
    ram = psutil.virtual_memory()
    return {
        "percent": ram.percent,
        "used": ram.used // (1024**3),
        "total": ram.total // (1024**3)
    }

def get_disk_usage():
    """Mengambil detail penggunaan Penyimpanan (Disk)."""
    # Penggunaan penyimpanan / disk (Storage / disk usage)
    disk = psutil.disk_usage('/')
    return {
        "percent": disk.percent,
        "free": disk.free // (1024**3),
        "total": disk.total // (1024**3)
    }

def get_uptime():
    """Mengambil durasi aktif komputer (Uptime)."""
    # Waktu aktif komputer / uptime (Computer uptime)
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    days = uptime.days
    hours = uptime.seconds // 3600
    minutes = (uptime.seconds // 60) % 60
    return f"{days} hari, {hours} jam, {minutes} menit"

def get_battery_status():
    """Mengambil informasi baterai (persentase & status) secara aman."""
    # Status baterai (Battery status)
    battery = psutil.sensors_battery()
    if battery is None:
        return None
    
    # Status pengisian daya baterai (Battery charging status)
    status_charge = "Di-charge (AC)" if battery.power_plugged else "Menggunakan Baterai"
    
    # Estimasi sisa waktu baterai (Estimated battery time remaining)
    secs = battery.secsleft
    if secs == psutil.POWER_TIME_UNLIMITED:
        time_left = "Tersambung ke daya AC"
    elif secs == psutil.POWER_TIME_UNKNOWN:
        time_left = "Menghitung sisa waktu..."
    else:
        hours = secs // 3600
        mins = (secs % 3600) // 60
        time_left = f"{hours} jam {mins} menit"
        
    return {
        "percent": battery.percent,
        "status": status_charge,
        "time_left": time_left
    }

def generate_report(sys_info, cpu_percent, cpu_temp, gpu, ram, disk, uptime, battery):
    """Menyusun teks laporan kesehatan PC."""
    # Pembuatan teks laporan (Report text generation)
    lines = []
    lines.append("="*50)
    lines.append("PC HEALTH CHECK REPORT")
    lines.append("="*50)
    lines.append(f"Waktu: {sys_info['waktu']}")
    lines.append(f"Komputer: {sys_info['komputer']}")
    lines.append(f"Sistem: {sys_info['sistem']}")
    lines.append("-"*50)
    
    # Menambahkan info CPU dan Suhu jika tersedia
    if cpu_temp and cpu_temp != "Tidak didukung":
        lines.append(f"CPU usage: {cpu_percent}% (Suhu: {cpu_temp})")
    else:
        lines.append(f"CPU usage: {cpu_percent}%")
        
    lines.append(f"RAM usage: {ram['percent']}% ({ram['used']} GB / {ram['total']} GB)")
    lines.append(f"Storage usage: {disk['percent']}%")
    lines.append(f"Disk usage: {disk['percent']}% (Free: {disk['free']} GB / Total {disk['total']} GB)")
    lines.append(f"Uptime: {uptime}")
    
    # Menambahkan info GPU jika terdeteksi (Add GPU info if detected)
    if gpu:
        lines.append("-"*50)
        lines.append(f"GPU: {gpu['name']}")
        lines.append(f"Suhu GPU: {gpu['temp']}")
    
    # Menambahkan info baterai ke laporan jika tersedia (Add battery info to report if available)
    if battery:
        lines.append("-"*50)
        lines.append(f"Status Baterai: {battery['percent']}% ({battery['status']})")
        lines.append(f"Sisa Waktu Baterai: {battery['time_left']}")
        
    lines.append("="*50)
    lines.append("Health check selesai!")
    return "\n".join(lines)

def main():
    # Mengambil informasi sistem (Retrieve system information)
    sys_info = get_system_info()
    
    # Mengambil penggunaan CPU (Retrieve CPU usage)
    cpu_percent = get_cpu_usage()
    
    # Mengambil suhu CPU jika didukung (Retrieve CPU temperature if supported)
    cpu_temp = get_cpu_temperature()
    
    # Mengambil status GPU jika didukung (Retrieve GPU status if supported)
    gpu = get_gpu_status()
    
    # Mengambil penggunaan RAM (Retrieve RAM usage)
    ram = get_ram_usage()
    
    # Mengambil penggunaan disk (Retrieve disk usage)
    disk = get_disk_usage()
    
    # Mengambil uptime komputer (Retrieve computer uptime)
    uptime = get_uptime()
    
    # Mengambil status baterai jika ada (Retrieve battery status if available)
    battery = get_battery_status()
    
    # Membuat teks laporan (Generate report text)
    report = generate_report(sys_info, cpu_percent, cpu_temp, gpu, ram, disk, uptime, battery)
    
    # Menampilkan laporan ke layar terminal (Print report to terminal screen)
    try:
        print(report)
    except UnicodeEncodeError:
        print(report.encode('ascii', errors='replace').decode('ascii'))
    
    # Menentukan lokasi file log (Determine log file path)
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"health_log_{timestamp}.txt"
    
    # Menyimpan di folder 'log_file' jika folder tersebut ada (Save in 'log_file' folder if it exists)
    log_dir = "log_file"
    if os.path.exists(log_dir) and os.path.isdir(log_dir):
        log_file = os.path.join(log_dir, filename)
    else:
        log_file = filename
        
    # Menyimpan laporan ke file log (Save report to log file)
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write(report + "\n")
        print(f"[SAVED] Laporan disimpan ke: {log_file}")
    except Exception as e:
        print(f"[ERROR] Gagal menyimpan laporan ke file: {e}")

# Menjalankan program utama (Run the main program)
if __name__ == "__main__":
    main()
