
def tarih():
    print("\033[1;32;40m")
    print("╔════════════════════════╗")
    print("║\033[1;31;40m      Tarih Goster \033[1;32;40m     ║")
    print("║1-Tarih                 ║")
    print("║2-Tarih Ve Saat         ║")
    print("╚════════════════════════╝")
    secim=int(input("Seçiminiz ? "))
    if secim==1:
        import datetime
        print("Bugün:", datetime.date.today())
    elif secim==2:
        from datetime import datetime   
        print("Şimdi =", datetime.now())
def main():
    tarih()

if __name__ == "__main__":
    main()