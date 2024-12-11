# input tinggi badan dan berat badan
tinggi= float(input("Masukkan tinggi badan (dalam meter) : "))
berat= float(input("Masukkan berat badan (dalam kilogram) : "))

# Mengonversi tinggi dari cm ke meter
tinggi = tinggi / 100

# Menghitung BMI
bmi = berat / (tinggi ** 2)

# mencetak hasil dengan format string
print(f"skor BMI anda adalah : {bmi:.2f}")
