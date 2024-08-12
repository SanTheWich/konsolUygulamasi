def dereceMenu():
    print("\033[1;32;40m")
    print("╔════════════════════════╗")
    print("║\033[1;31;40m   DERECE DONUSTURUCU\033[1;32;40m   ║"),
    print("║  ANA ÖLÇEK║DONUSTURULEN║")
    print("║1-  °F     ║     °C     ║")
    print("║2-  °C     ║     °F     ║")
    print("║3-  °K     ║     °C     ║")
    print("║4-  °C     ║     °K     ║")
    print("╚════════════════════════╝")
    secim=int(input("Seçim Yapınız: "))
    import DereceDonusturme.c_f,DereceDonusturme.c_k,DereceDonusturme.f_c,DereceDonusturme.k_c
    if secim==1:
        DereceDonusturme.f_c.fahrenheitCelsius()
    elif secim==2:
        DereceDonusturme.c_f.celsiusFahrenheit()
    elif secim==3:
        DereceDonusturme.k_c.kelvincelsius()
    elif secim==4:
        DereceDonusturme.c_k.celsiusKelvin()
    else:
        print("Eksik ya da hatalı seçim yaptınız")

def main():
    dereceMenu()

if __name__ == "__main__":
    main() 