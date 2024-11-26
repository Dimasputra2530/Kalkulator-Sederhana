def calculator():
    print("=== Kalkulator Sederhana ===")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    # buat input pengguna
    choice = input("Masukkan pilihan (1/2/3/4): ")

    # Memastikan pilihan valid
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))

            # Menjalankan operasi berdasarkan pilihan
            if choice == '1':
                print(f"Hasil: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Hasil: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Hasil: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"Hasil: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Pembagian dengan nol tidak diperbolehkan.")
        except ValueError:
            print("Error: Masukkan angka yang valid.")
    else:
        print("Error: Pilihan tidak valid.")

# untuk Memanggil fungsi kalkulator
calculator()
