def nilaiakhir(nama, nilai_tugas,nilai_uts,nilai_uas):
    # nama = input("Masukkan nama: ")
    # nilai_tugas = float(input("Masukkan Nilai Tugas: "))
    # nilai_uts = float(input("Masukkan Nilai UTS: "))
    # nilai_uas = float(input("Masukkan Nilai UAS: "))

    nilai_akhir = nilai_tugas * 0.3 + nilai_uts * 0.3 + nilai_uas * 0.4


    print(f"| {'Nama':11} :", nama, type(nama))
    print(f"| {'Nilai Akhir':12}: {nilai_akhir:.2f}", type(nilai_akhir))
    return nilai_akhir

# nilaiakhir("Wowok",100,90,80)