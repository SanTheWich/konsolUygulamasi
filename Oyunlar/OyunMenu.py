def oyunMenusu():
    print("╔════════════════════════╗")
    print("║        OYUNLAR         ║")
    print("║1-YILAN                 ║")
    print("║2-TETRİS                ║")
    print("║3-ŞEKİL ÇİZDİRME        ║")
    print("║  Seçiminizi Yapınız    ║")
    print("╚════════════════════════╝")
    secim=int(input("Seçiminiz:"))
    for i in range(6):
        if i==secim:
            print(f"{secim} seçtiniz")