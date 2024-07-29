print("╔════════════════════════╗")
print("║  Python Çalışmaları    ║")
print("║1-HESAP MAKİNESİ        ║")
print("║2-OYUNLAR               ║")
print("║3-ŞEKİL ÇİZDİRME        ║")
print("║4-TAKVİM                ║")
print("║5-RİTMİK SAYMA          ║")
print("║6-NOT HESAPLAMA         ║")
print("║7-ÇARPIM TABLOSU        ║")
print("║8-BMI HESAPLAMA         ║")
print("║9-DÖVİZ DURUMU          ║")
print("║10-ŞEKİL ALAN HESAPLAMA ║")
print("║11-ÇIKIŞ  (e)           ║")
print("║  Seçiminizi Yapınız    ║")
print("╚════════════════════════╝")
secim=int(input("Seçiminiz:"))
for i in range(6):
    if i==secim:
        print(f"{secim} seçtiniz")
import HesapMakinesiModülü.hesapMakinesi as hm #bunu hm olarak çağıracağım demektir
import Oyunlar.OyunMenu as om
if secim==1:
   print(hm.hesapMakinesiMenu())
elif secim==2:
    print(om.oyunMenusu())