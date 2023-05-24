import os

def recover_deleted_files(directory):
    """
    Memulihkan berkas yang dihapus dari direktori yang diberikan.
    """
    recovered_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

            # Periksa apakah berkas terhapus
            if not os.path.exists(file_path):
                recovered_files.append(file_path)
                os.rename(file_path + ".recover", file_path)

    return recovered_files

# Contoh penggunaan fungsi recover_deleted_files
directory_path = 'path/to/directory'
recovered_files = recover_deleted_files(directory_path)
print("Berkas yang pulih:", recovered_files)


# Dalam contoh di atas, fungsi recover_deleted_files menggunakan modul os untuk melakukan pemulihan berkas yang dihapus. Fungsi ini melakukan iterasi melalui seluruh struktur direktori, dan untuk setiap berkas di dalamnya, memeriksa apakah berkas tersebut masih ada di sistem menggunakan os.path.exists. Jika berkas tidak ada (artinya terhapus), maka berkas tersebut dipulihkan dengan mengubah namanya menggunakan os.rename.

# Perlu dicatat bahwa pemulihan berkas yang dihapus dapat lebih kompleks tergantung pada faktor-faktor seperti sistem operasi, sistem file, dan tingkat kegiatan yang telah terjadi setelah penghapusan berkas. Oleh karena itu, algoritma pemulihan data yang lebih canggih dan spesifik mungkin diperlukan tergantung pada situasi dan kondisi yang terlibat dalam penyelidikan forensik.