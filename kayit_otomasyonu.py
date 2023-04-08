#coder by muerdoga

def ogrenci_ekle():
    global kayit
    dosya = open("kayit.txt", "a", encoding="utf-8")
    ogrenci_adi = input("Öğrenci adı :")
    ogrenci_soyadi = input("Öğrenci soyadı :")
    ogrenci_no = input("Öğrenci no :")
    dosya.write("{0}: {1} {2} {3}".format(kayit, ogrenci_adi, ogrenci_soyadi, ogrenci_no))
    kayit += 1
    dosya.write("\n")
    dosya.close()

def ogrenci_sil():
    ogrenci_no = input("Silmek istediğiniz öğrencinin numarasını girin: ")
    dosya = open("kayit.txt", "r", encoding="utf-8")
    satirlar = dosya.readlines()
    dosya = open("kayit.txt", "w", encoding="utf-8")
    kayit = 1
    for satir in satirlar:
        if ogrenci_no not in satir:
            dosya.write(str(kayit)+": " + satir.split(" ", 1)[1])
            kayit += 1
        else:
            ogrenci_ad, ogrenci_soyad = satir.split()[1:3]
            print("Öğrenci silindi: "+ogrenci_ad+" "+ogrenci_soyad)
    dosya.close()

def ogrenci_liste():
    dosya = open("kayit.txt", "r", encoding="utf-8")
    print("Öğrenci Listesi\n")
    for satir in dosya:
        print(satir)
    dosya.close()

kayit = 1
dosya = open("kayit.txt", "w+")

print("Öğrenci Kayıt Otomasyonu\n")
print("(1) Öğrenci Ekle\n")
print("(2) Öğrenci Sil\n")
print("(3) Öğrencileri Listele\n")
print("(4) Çıkış\n")

while True:
    try:
        secim = input("\nYapmak istediğiniz işlemi seçin : ")
        if secim == "1":
            ogrenci_ekle()
        elif secim == "2":
            ogrenci_sil()
        elif secim == "3":
            ogrenci_liste()
        elif secim == "4":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Hatalı işlem yaptınız")
    except KeyboardInterrupt:
        print("\nProgramdan çıkılıyor...")
        break
dosya.close()