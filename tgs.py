def caesar_encrypt(plain_text, shift):
    encrypted_text = ""  # Membuat variabel untuk menyimpan teks terenkripsi
    for char in plain_text:  # Loop melalui setiap karakter dalam teks asli
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf alfabet
            if char.isupper():  # Jika huruf kapital
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65)  # Menggeser huruf kapital
            else:  # Jika huruf kecil
                shifted_char = chr((ord(char) - 97 + shift) % 26 + 97)  # Menggeser huruf kecil
            encrypted_text += shifted_char  # Menambahkan huruf yang telah digeser ke teks terenkripsi
        else:
            encrypted_text += char  # Jika bukan huruf, tambahkan karakter tanpa mengubahnya
    return encrypted_text  # Mengembalikan teks terenkripsi

# Contoh penggunaan
plain_text = input("Masukkan teks yang ingin dienkripsi: ")
shift = int(input("Masukkan jumlah pergeseran (angka): "))

encrypted_text = caesar_encrypt(plain_text, shift)
print("Teks setelah dienkripsi: " + encrypted_text)
def caesar_decrypt(encrypted_text, shift):
    decrypted_text = ""  # Membuat variabel untuk menyimpan teks terdekripsi
    for char in encrypted_text:  # Loop melalui setiap karakter dalam teks terenkripsi
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf alfabet
            if char.isupper():  # Jika huruf kapital
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65)  # Menggeser kembali huruf kapital
            else:  # Jika huruf kecil
                shifted_char = chr((ord(char) - 97 - shift) % 26 + 97)  # Menggeser kembali huruf kecil
            decrypted_text += shifted_char  # Menambahkan huruf yang telah digeser kembali ke teks terdekripsi
        else:
            decrypted_text += char  # Jika bukan huruf, tambahkan karakter tanpa mengubahnya
    return decrypted_text  # Mengembalikan teks terdekripsi

# Contoh penggunaan
decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Teks setelah didekripsi: " + decrypted_text)
