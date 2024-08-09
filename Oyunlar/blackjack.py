import random
import time
def blackjackOyna():
    deste=[1,2,3,4,5,6,7,8,9,10]
    anaPara=100
    bahis=0
    oyuncuEli=0
    masa=0
    karar=""
    oyuncuEli=random.randint(1,10)
    masa=random.randint(1,10)
    print("╔════════════════════════╗")
    print("║\033[1;31;40mBlackJack'e hoşgeldiniz:\033[1;32;40m║")
    print("║Lütfen bahis giriniz    ║")
    bahis=int(input("║Bahsiniz:               ║"))
    print(f"║Bahsiniz: {bahis}            ║")
    print(f"║Kalan Ana paranız     {anaPara-bahis}║")
    print("╚════════════════════════╝")
    anaPara=anaPara-bahis
    print(f"Masanin eli {masa}")
    print("══════"*4)
    time.sleep(1)
    print(f"Sizin eliniz {oyuncuEli}\n Kart çekmek için 'c' kalmak için 'k' basınız")
    while oyuncuEli<=21:
        time.sleep(0.1)
        karar=str(input("Karar: "))
        if karar=="c":
            a=(random.randint(1,10))
            oyuncuEli+=a
            print(f"Sizin eliniz: {oyuncuEli}\nKart çekmek için 'c' veya kalmak için 'k' basınız")
        if karar=="k":
            ##masanın elini ayarla masa<17 ise çek yoksa kal
            time.sleep(0.1)
            while masa<17:
                b=(random.randint(5,10))
                masa+=b
                time.sleep(2)
                print(f"Masa {b} çekti, masanın puanı {masa}")
            else:
                if masa>21:
                    time.sleep(0.5)
                    print(f"Masa {masa} puan ile 21'i geçti, KAZANDINIZ ")
                    anaPara=(bahis*2)+anaPara
                    time.sleep(0.5)
                    print(f"Kazandığınız para {bahis*2};\n Ana paranız {anaPara}")
                    break
                print(f"Masanın puanu: {masa}")
                if masa>oyuncuEli:
                    time.sleep(0.7)
                    print(f"Maalesef {masa} puan ile masa kazandı; Sizin puaniniz ise {oyuncuEli}")
                    time.sleep(0.5)
                    print(f"Ana paranız {anaPara}")
                    break
                elif masa==oyuncuEli:
                    time.sleep(0.7)
                    print(f"Berabere Kaldınız, puanınız {masa}")
                    anaPara=bahis+anaPara
                    time.sleep(0.5)
                    print(f"Ana paranız {anaPara}")
                    break
                else:
                    time.sleep(0.7)
                    print(f"Tebrikler {oyuncuEli} puan ile Kazandınız; Masanın puanı ise {masa}")
                    anaPara=(bahis*2)+anaPara
                    time.sleep(0.5)
                    print(f"Kazandığınız para {bahis*2};\n Ana paranız {anaPara}")
                    break

    else:
        print("21'i geçtiniz!!!! KAYBETİNİZ")

def main():
    blackjackOyna()

if __name__ == "__main__":
    main()