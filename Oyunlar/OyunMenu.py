def oyunMenusu():
    import Oyunlar.yilanOyunu
    import Oyunlar.tetris
    import Oyunlar.sayiTahmin
    print("╔════════════════════════╗")
    print("║        OYUNLAR         ║")
    print("║1-YILAN                 ║")
    print("║2-TETRIS                ║")
    print("║3-SAYI TAHMIN ETME      ║")
    print("║4-BLACKJACK(21)         ║")
    print("║  Seçiminizi Yapınız    ║")
    print("╚════════════════════════╝")
    secim=int(input("Seçiminiz:"))
    if secim==1:
        Oyunlar.yilanOyunu.yilanOyna()
    elif secim ==2:
        Oyunlar.tetris.tetrisOyna()
    elif secim==3:
        Oyunlar.sayiTahmin.sayiBilmeceOyna()
def main():
    oyunMenusu()

if __name__ == "__main__":
    main()