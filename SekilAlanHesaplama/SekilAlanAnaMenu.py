def sekilAlanMenu():    
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40mŞEKİL ALAN HESAPLAMA\033[1;32;40m ║")
    print("║    ŞEKLİ SEÇİNİZ    ║")
    print("║     1-KARE          ║")
    print("║     2-ESKENAR ÜÇGEN ║")
    print("║     3-DAİRE         ║")
    print("║     4-DİKTÖRGEN     ║")
    print("╚═════════════════════╝")
    secim=int(input(""))
    def kare():
        a=int(input("Kenar uzunluğu:"))
        print(f"Alan={a*a}")
    def ucgen():
        a=int(input("Tabanın uzunluğu:"))
        b=int(input("Yüksekliğin uzunluğu:"))
        print(f"Alan={(a*b)/2}")
    def daire():
        a=int(input("Yarıçap uzunluğu:"))
        print(f"Alan={a*3.14*3.14}")
    def dikdortgen():
        a=int(input("Uzun kenar uzunluğu:"))
        b=int(input("Kısa kenar uzunluğu:"))
        print(f"Alan={a*b}")
    if secim==1:
        kare()
    elif secim==2:
        ucgen()
    elif secim==3:
        daire()
    else:
        dikdortgen()
def main():
    sekilAlanMenu()

if __name__ == "__main__":
    main()