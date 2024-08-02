def oyunMenusu():
    print("╔════════════════════════╗")
    print("║        OYUNLAR         ║")
    print("║1-YILAN                 ║")
    print("║2-TETRIS                ║")
    print("║3-SAYI TAHMIN ETME      ║")
    print("║  Seçiminizi Yapınız    ║")
    print("╚════════════════════════╝")
    secim=int(input("Seçiminiz:"))
    import yilanOyunu
    import tetris
    import sayiTahmin
    if secim==1:
       yilanOyunu.yilanOyna()
    elif secim ==2:
        tetris.tetrisOyna()
    elif secim==3:
        sayiTahmin.sayiBilmeceOyna()
def main():
    oyunMenusu()

if __name__ == "__main__":
    main()