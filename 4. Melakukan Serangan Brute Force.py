import itertools
import string
import hashlib

def brute_force_password(password_hash):
    """
    Melakukan serangan Brute Force untuk menguraikan password dengan mencoba semua kemungkinan kombinasi.
    """
    characters = string.ascii_letters + string.digits  # Kombinasi karakter yang mungkin dalam password
    password_length = 4  # Panjang password yang diasumsikan

    for password in itertools.product(characters, repeat=password_length):
        password = ''.join(password)
        hashed_password = hashlib.md5(password.encode()).hexdigest()

        if hashed_password == password_hash:
            return password

    return None

# Contoh penggunaan fungsi brute_force_password
hashed_password = '5f4dcc3b5aa765d61d8327deb882cf99'  # Hash dari password "password"
password = brute_force_password(hashed_password)
if password:
    print("Password ditemukan:", password)
else:
    print("Password tidak ditemukan.")

# Mmenggunakan pendekatan Brute Force untuk menguraikan password dengan mencoba semua kemungkinan kombinasi karakter dalam password. Fungsi brute_force_password melakukan iterasi melalui semua kombinasi karakter yang mungkin menggunakan modul itertools. Setiap kombinasi karakter diubah menjadi string dan di-hash menggunakan algoritma MD5. Jika hash yang dihasilkan cocok dengan hash password yang diberikan, maka password ditemukan.

# Perlu diingat bahwa Brute Force adalah metode yang sangat lambat dan tidak efisien, terutama untuk password yang lebih panjang atau kompleks. Dalam praktiknya, ada berbagai teknik dan algoritma yang lebih canggih yang digunakan dalam penguraian password, seperti serangan kamus (dictionary attack), serangan rainbow table, dan pengoptimalan serangan Brute Force menggunakan GPU.