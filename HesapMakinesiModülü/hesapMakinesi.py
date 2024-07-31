def hesapMakinesiMenu():
    print("\033[1;32;40m")
    #print("╔"+"═"*20+"╗")
    print("╔═════════════════════╗")
    print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
    print("║    HANGİ İŞLEMİ     ║")
    print("║    YAPACAKSINIZ???? ║")
    print("║     (+,-,/,*)       ║")
    print("╚═════════════════════╝")
    hesaplama=str(input())
    a=int(input("Lütfen ilk sayınızı giriniz: "))
    b=int(input("Lütfen ikinci sayınızı giriniz: "))
    toplama = '+'
    bolme = '/'
    carpma= '*'
    cikarma= '-'

    if hesaplama == toplama:
        print(f"{a} + {b} = {a+b}")
    elif hesaplama == bolme:
            if b==0:
                 print("HATA!!")
            else:print("{} / {} = {}".format(a,b,a/b))
                
    elif hesaplama == carpma:
        print("{} * {} = {}".format(a,b,a*b))
    elif hesaplama == cikarma:
        print("{} - {} = {}".format(a,b,a-b))
#hesapMakinesiMenu()