import cv2
import numpy as np

def match_fingerprint(fingerprint1, fingerprint2):
    """
    Membandingkan dan mencocokkan dua sidik jari digital.
    """
    # Konversi sidik jari ke citra biner
    _, fingerprint1_bin = cv2.threshold(fingerprint1, 127, 255, cv2.THRESH_BINARY)
    _, fingerprint2_bin = cv2.threshold(fingerprint2, 127, 255, cv2.THRESH_BINARY)

    # Bandingkan kedua citra sidik jari menggunakan perbandingan piksel
    difference = cv2.subtract(fingerprint1_bin, fingerprint2_bin)
    match_percentage = np.count_nonzero(difference) / difference.size

    return match_percentage

# Contoh penggunaan fungsi match_fingerprint
fingerprint1 = cv2.imread('path/to/fingerprint1.png', cv2.IMREAD_GRAYSCALE)
fingerprint2 = cv2.imread('path/to/fingerprint2.png', cv2.IMREAD_GRAYSCALE)

match_percentage = match_fingerprint(fingerprint1, fingerprint2)
print("Persentase kecocokan sidik jari:", match_percentage)


# Menggunakan library OpenCV untuk memproses citra sidik jari digital. Fungsi match_fingerprint menerima dua citra sidik jari (dalam format grayscale) sebagai masukan. Pertama, kedua citra sidik jari dikonversi menjadi citra biner menggunakan fungsi cv2.threshold. Kemudian, kedua citra sidik jari dibandingkan menggunakan perbandingan piksel. Persentase kecocokan dihitung berdasarkan jumlah piksel yang berbeda dibagi dengan jumlah total piksel dalam citra.

# Perlu dicatat bahwa contoh kode di atas hanya menggambarkan konsep dasar dari algoritma pencocokan sidik jari. Dalam praktiknya, algoritma pencocokan sidik jari yang lebih canggih dan kompleks digunakan, seperti algoritma minutiae-based matching yang mencocokkan titik-titik khusus dalam sidik jari atau penggunaan teknik machine learning untuk pengenalan sidik jari.