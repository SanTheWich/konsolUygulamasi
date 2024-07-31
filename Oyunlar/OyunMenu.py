def oyunMenusu():
    print("╔════════════════════════╗")
    print("║        OYUNLAR         ║")
    print("║1-YILAN                 ║")
    print("║2-TETRİS                ║")
    print("║3-ŞEKİL ÇİZDİRME        ║")
    print("║  Seçiminizi Yapınız    ║")
    print("╚════════════════════════╝")
    secim=str(input("Seçiminiz:"))
    import yilanOyunu
    import tetris
    if secim=="1":
       yilanOyunu.yilanOyna()
    elif secim == "2" :
        tetris.tetrisOyna()
    elif secim=="13":
        print("Oyun yok")
# oyunMenusu()
def main():
    oyunMenusu()

if __name__ == "__main__":
    main()