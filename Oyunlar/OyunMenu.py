


def oyunMenusu():
    import Oyunlar.yilanOyunu
    import Oyunlar.tetris
    import Oyunlar.sayiTahmin
    import Oyunlar.blackjack
    import Oyunlar.yaziTura
    print("╔════════════════════════╗")
    print("║        OYUNLAR         ║")
    print("║1-YILAN                 ║")
    print("║2-TETRIS                ║")
    print("║3-SAYI TAHMIN ETME      ║")
    print("║4-BLACKJACK(21)         ║")
    print("║5-YAZI TURA             ║")
    print("║  Seçiminizi Yapınız    ║")
    print("╚════════════════════════╝")
    secim=int(input("Seçiminiz:"))
    if secim==1:
        Oyunlar.yilanOyunu.yilanOyna()
    elif secim ==2:
        Oyunlar.tetris.tetrisOyna()
    elif secim==3:
        Oyunlar.sayiTahmin.sayiBilmeceOyna()
    elif secim==4:
        Oyunlar.blackjack.blackjackOyna()
    elif secim==5:
        Oyunlar.yaziTura.yaziTuraAt()
def main():
    oyunMenusu()

if __name__ == "__main__":
    main()