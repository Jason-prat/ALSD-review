from soal1 import *

x = nilaiakhir("WOWOK",100,100,100)

def nilai(nilai_akhir):
    if nilai_akhir >=85:
        print(f"Nilai {nilai_akhir} -> Grade A")
    elif 70<=nilai_akhir<85:
        print(f"Nilai {nilai_akhir} -> Grade B")
    elif 60<= nilai_akhir<70:
        print(f"Nilai {nilai_akhir} -> Grade C")
    elif 50<=nilai_akhir<60:
        print(f"Nilai {nilai_akhir} -> Grade D")
    else:
        print(f"Nilai {nilai_akhir} -> Grade E")

nilai(x)