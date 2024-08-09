import random
import time
def blackjackOyna():
    deste=[1,2,3,4,5,6,7,8,9,10]
    oyuncuEli=0
    masa=0
    karar=""
    oyuncuEli=random.randint(1,10)
    masa=random.randint(1,10)
    print(f"Masanin eli {masa}\n ")
    print(f"Eliniz {oyuncuEli}\n Kart çekmek için 'c' kalmak için 'k' basınız")
    while oyuncuEli<21:
        time.sleep(1)
        karar=str(input("Karar: "))
        if karar=="c":
            a=(random.randint(1,10))
            oyuncuEli+c=a
            print(f"Eliniz {oyuncuEli}\n Kart çekmek için 'c' kalmak için 'k' basınız")
        if karar=="k":
            ##masanın elini ayarla masa<17 ise çek yoksa kal
            print("")
    else:
        print("21'i geçtiniz!!!!")

"""
# print(random.randint(1,100))
# print(random.random())
# yaziTura = ["Tura","Yazı"]
# print(random.choice(yaziTura)) 
"""
def main():
    blackjackOyna()

if __name__ == "__main__":
    main()