import random

def replace_x(template, karakter_unik):
    result = []
    for char in template:
        if char == 'x':
            result.append(random.choice(karakter_unik))
        else:
            result.append(char)
    return ''.join(result)

def ambil_input():
    template = input("Masukkan template: ")
    print("Pilih karakter unik yang ingin digunakan:")
    print("1. Huruf besar (ABCDEFGHIJKLMNOPQRSTUVWXYZ)")
    print("2. Huruf kecil (abcdefghijklmnopqrstuvwxyz)")
    print("3. Angka (0123456789)")
    print("4. Huruf besar dan angka")
    print("5. Huruf kecil dan angka")
    print("6. Simbol (!@#$%^&*()_-+=\|[]{};:'\",.<>/?")
    print("7. Alfanumerik (ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789)")
    print("8. Hexadecimal (0123456789abcdef)")
    pilihan = input("Masukkan pilihan (1-8): ")

    if pilihan == '1':
        karakter_unik = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    elif pilihan == '2':
        karakter_unik = "abcdefghijklmnopqrstuvwxyz"
    elif pilihan == '3':
        karakter_unik = "0123456789"
    elif pilihan == '4':
        karakter_unik = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    elif pilihan == '5':
        karakter_unik = "abcdefghijklmnopqrstuvwxyz0123456789"
    elif pilihan == '6':
        karakter_unik = "!@#$%^&*()_-+=\|[]{};:'\",.<>/?"
    elif pilihan == '7':
        karakter_unik = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    elif pilihan == '8':
        karakter_unik = "0123456789abcdef"
    else:
        print("Pilihan tidak valid.")
        exit()

    return template, karakter_unik

# meminta masukan dari pengguna
template, karakter_unik = ambil_input()

# ... (bagian jumlah hasil dan nama file tidak berubah)

# meminta masukan dari pengguna untuk jumlah hasil dan nama file
jumlah_hasil = int(input("Masukkan jumlah hasil yang diinginkan: "))
nama_file = input("Masukkan nama file: ")

hasil = []
for i in range(jumlah_hasil):
    string_acak = replace_x(template, karakter_unik)
    hasil.append(string_acak)

# menyimpan hasil acakan ke dalam file txt
with open(nama_file + '.txt', 'w') as file:
    file.write(f"{jumlah_hasil} string acak dengan karakter unik {karakter_unik} dan template {template}:\n")
    for i in hasil:
        file.write(i + '\n')

print(f"Sukses tersimpan di file {nama_file}.txt")
