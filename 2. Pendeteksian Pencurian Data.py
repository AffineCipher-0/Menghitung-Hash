import re

def detect_data_breach(log_files):
    """
    Mendeteksi indikasi pencurian data atau pelanggaran keamanan dari file log yang diberikan.
    """
    suspicious_patterns = ['unauthorized access', 'data breach', 'security breach']
    detected_entries = []

    for log_file in log_files:
        with open(log_file, 'r') as file:
            for line in file:
                for pattern in suspicious_patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        detected_entries.append(line)
                        break

    return detected_entries

# Contoh penggunaan fungsi detect_data_breach
log_files = ['path/to/logfile1.txt', 'path/to/logfile2.txt']
detected_entries = detect_data_breach(log_files)
print("Entri yang terdeteksi:", detected_entries)


# Fungsi detect_data_breach menggunakan modul re untuk mendeteksi indikasi pencurian data atau pelanggaran keamanan dari file log yang diberikan. Fungsi ini melakukan iterasi melalui setiap baris di setiap file log, dan untuk setiap pola yang mencurigakan, menggunakan re.search untuk mencari kecocokan dalam baris tersebut. Jika kecocokan ditemukan, baris tersebut ditambahkan ke daftar entri yang terdeteksi.

# Dalam contoh di atas, fungsi detect_data_breach menerima daftar file log sebagai masukan. Fungsi ini membaca setiap file log, kemudian memeriksa setiap baris log untuk adanya pola yang mencurigakan yang dapat menunjukkan indikasi pencurian data atau pelanggaran keamanan. Pola-pola mencurigakan tersebut ditentukan dalam variabel suspicious_patterns.

# Pada setiap baris log, fungsi re.search digunakan untuk mencari pola-pola yang mencurigakan. Jika ditemukan kecocokan dengan pola, baris log tersebut ditambahkan ke dalam daftar detected_entries.

# Penting untuk dicatat bahwa algoritma pendeteksian pencurian data yang lebih canggih biasanya melibatkan analisis yang lebih mendalam, termasuk metode-metode seperti analisis perilaku anomali, pemantauan lalu lintas jaringan, analisis log sistem, dan penggunaan algoritma machine learning untuk mengidentifikasi pola-pola yang mencurigakan. Kode di atas hanya menggambarkan pendekatan sederhana untuk memahami konsep dasar pendeteksian pencurian data dalam digital forensik.