#kode kalkulator

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("---------------------------------")

berat_badan = float(input("Masukkan berat badan anda (kilogram): "))
tinggi_badan = float(input("Masukkan tinggi badan anda (meter): "))

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal ['minimal'] = 18.5*(tinggi_badan**2)
berat_badan_ideal ['maksimal'] = 25*(tinggi_badan**2)

if bmi< 18.5:
      kategori = "Anda kekurangan berat badan"
elif bmi< 25:
      kategori = "Nilai BMI Anda adalah Normal"
elif bmi< 30:
      kategori = "Anda kelebihan Berat Badan"
else:
      kategori = "Anda mengalami Obesitas"

print("\nHasil kalkulator BMI Anda adalah: ")
print("----------------------------------")
print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print(kategori)
print(f"Berat badan ideal anda dalam rentang " 
      f"{berat_badan_ideal['minimal']:.2f} kg- {berat_badan_ideal['maksimal']:.2f} kg")

print("Terima kasih sudah menjalankan prpogram ini")
