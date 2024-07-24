print("\033[1;32;40m")
#print("╔"+"═"*20+"╗")
print("╔═════════════════════╗")
print("║\033[1;31;40m   HESAP MAKİNESİ  \033[1;32;40m  ║")
print("║                     ║")
print("║  1-Toplama(+)       ║")
print("║  2-Çıkarma(-)       ║")
print("║  3-Bölme(/)         ║")
print("║  4-Çarpma(*)        ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")
hesaplama=str(input())
a=int(input("Lütfen ilk sayınızı giriniz: "))

b=int(input("Lütfen ikinci sayınızı giriniz: "))
toplama = '+'
bolme = '/'
carpma= '*'
cikarma= '-'

if hesaplama == toplama:
    print("{} + {} = {}".format(a,b,a+b))
    input()
elif hesaplama == bolme:
        print("{} / {} = {}".format(a,b,a/b))
elif hesaplama == carpma:
     print("{} * {} = {}".format(a,b,a*b))
elif hesaplama == cikarma:
    print("{} - {} = {}".format(a,b,a-b))