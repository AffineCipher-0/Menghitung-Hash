import hashlib

def calculate_hash(filepath):
    """
    Menghitung hash MD5 dari file yang diberikan.
    """
    with open(filepath, 'rb') as file:
        content = file.read()
        hash_value = hashlib.md5(content).hexdigest()
    return hash_value

# Contoh penggunaan fungsi calculate_hash untuk menghitung hash MD5 dari file
file_path = 'path/to/file'
hash_value = calculate_hash(file_path)
print("Hash MD5:", hash_value)


# Menggunakan algoritma hash MD5 (Message Digest 5) untuk menghitung hash dari sebuah file. Hash digunakan dalam forensik digital untuk memverifikasi integritas data dan untuk membantu dalam proses identifikasi dan pemeriksaan file.

# Fungsi calculate_hash membaca isi file menggunakan mode baca biner 'rb', kemudian menghitung hash MD5 dari kontennya menggunakan hashlib.md5. Hasil hash kemudian dikonversi menjadi format heksadesimal dengan menggunakan metode hexdigest().

# Anda dapat menggunakan fungsi calculate_hash untuk menghitung hash dari file yang relevan dalam proses digital forensik. Hasil hash dapat dibandingkan dengan hash yang ditemukan di tempat lain (misalnya, dalam database atau catatan hash) untuk verifikasi integritas file tersebut.