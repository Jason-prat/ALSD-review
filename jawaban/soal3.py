def hitung_rata2(list_nilai):
    jumlah_data=0
    total_nilai=0
    for i in list_nilai:
        if i == -1:
            break
        elif 0>i or i>100:
            continue
        jumlah_data+=1
        print(f"Nilai ke-{jumlah_data}: {i}")
        total_nilai+=i
    rata2=total_nilai/jumlah_data
    return(f"Rata-rata: {rata2:.1f}")
nilai_mhs = [80, 75, 90, 65, 88]

# nilai_mhs=eval(input("Masukkan List Nilai Mahasiswa:"))
print(hitung_rata2(nilai_mhs))