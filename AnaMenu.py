print("\033[1;32;40m")
print("╔════════════════════════╗")
print("║\033[1;31;40mPython Calismalari \033[1;32;40m     ║")
print("║1-HESAP MAKİNESİ        ║")
print("║2-OYUNLAR               ║")
print("║3-RİTMİK SAYMA          ║")
#!print("║4-ORTALAMAHESAPLAMA     ║")
print("║5-ÇARPIM TABLOSU        ║")
print("║6-ŞEKİL ALAN HESAPLAMA  ║")
print("║7-TARİH                 ║")
print("║8-NOT HESAPLAMA         ║")
#!print("║9-MESAİ ÜCRET HESAPLA   ║")
#!print("║10-DERECE DONUSTURME    ║")
print("║11-ÇIKIŞ  (e)            ║")
print("║  Seçiminizi Yapınız    ║")
print("╚════════════════════════╝")
secim=int(input("Seçiminiz:"))
for i in range(6):
    if i==secim:
        print(f"{secim} seçtiniz")
import HesapMakinesiModülü.hesapMakinesi as hm #bunu hm olarak çağıracağım demektir
import Oyunlar.OyunMenu as om
import RitmikSayma.ritmikSayma as rt
import CarpimTablosu.carpimTablosu as ct
import Tarih.tarihGoster as tg
import SekilAlanHesaplama.SekilAlanAnaMenu as sh
import NotHesaplama.NotHesaplama as nh
if secim==1:
   hm.hesapMakinesiMenu()
elif secim==2:
    om.oyunMenusu()
elif secim==4:
    rt.ritmiksay()
elif secim==6:
    ct.Carpim()
elif secim==7:
    sh.sekilAlanMenu()
elif secim==8:
    tg.tarih()
elif secim==10:
    nh.puanHesaplama()