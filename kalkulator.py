#kode kalkulator

print("PERHITUNGAN BMI (BODY MASS INDEX)")
print("---------------------------------")

berat_badan = input("Masukkan berat badan anda (kilogram): ")
berat_badan = float(berat_badan)
tinggi_badan = input("Masukkan tinggi badan anda (meter): ")
tinggi_badan = float(tinggi_badan)

bmi = berat_badan/(tinggi_badan**2)

berat_badan_ideal = dict()
berat_badan_ideal ['minimal'] = 18.5*(tinggi_badan**2)
berat_badan_ideal ['maksimal'] = 25*(tinggi_badan**2)

print(f"Nilai BMI anda adalah {bmi:.2f} kg/m^2")
print("Nilai BMI normal adalah 18 kg/m^2 - 25 kg/m^2")
print(f"Berat badan ideal anda dalam rentang " 
      f"{berat_badan_ideal['minimal']:.2f} kg- {berat_badan_ideal['maksimal']:.2f} kg")

print("Terima kasih sudah menjalankan prpogram ini")
