def NotHesapla():
    print("\033[1;32;40m")
    print("╔════════════════════════╗")
    print("║\033[1;31;40mNot Hesaplamaya Hosgeldiniz \033[1;32;40m     ║")
    flag="c"
    dersAdi[100]=("")
    while True:
        if flag=="e":
            break
        else:
            while True:
                if flag=="e":
                    break
            else:
                dersAdi[i]=str(input("║Ders adi giriniz║"))
            
 
 
    # print("║1-HESAP MAKİNESİ        ║")
    # print("║2-OYUNLAR               ║")
    # print("║3-!ŞEKİL ÇİZDİRME        ║")
    # print("║4-RİTMİK SAYMA          ║")
    # print("║5-!NOT HESAPLAMA         ║")
    # print("║6-ÇARPIM TABLOSU        ║")
    # print("║7-!ŞEKİL ALAN HESAPLAMA  ║")
    # print("║8-ÇIKIŞ  (e)            ║")
    # print("║  Seçiminizi Yapınız    ║")
    # print("╚════════════════════════╝")

def main():
    NotHesapla()

if __name__ == "__main__":
    main()