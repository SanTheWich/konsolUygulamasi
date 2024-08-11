


def oyunMenusu():
    import yilanOyunu
    import tetris
    import sayiTahmin
    import blackjack
    import yaziTura
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
        yilanOyunu.yilanOyna()
    elif secim ==2:
        tetris.tetrisOyna()
    elif secim==3:
        sayiTahmin.sayiBilmeceOyna()
    elif secim==4:
        blackjack.blackjackOyna()
    elif secim==5:
        yaziTura.yaziTuraAt()
def main():
    oyunMenusu()

if __name__ == "__main__":
    main()