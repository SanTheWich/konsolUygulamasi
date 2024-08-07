def ortalama():
    print("\033[1;32;40m")
    print("╔════════════════════════╗")
    print("║\033[1;31;40mOrtalama Hesaplamaya Hosgeldiniz \033[1;32;40m     ║")
    flag="c"
    dersAdi=[]
    dersSaati=[]
    i=0
    while True:
        if flag=="e":
            break
        else:
                #!array add bak dersAdi[i]=str(input("║Ders adi giriniz║"))
                i+=1
                flag=str(input("Devam mı(c), Tamam mı(e)"))
 
 
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
    ortalama()

if __name__ == "__main__":
    main()