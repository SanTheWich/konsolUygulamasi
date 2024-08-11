import random
import time
def yaziTuraAt():
    secim=str(input("Yazi mi?Tura mi?\nYazi için 'y' Tura için 't': "))
    yaziTura = ["tura","yazı"]
    secim
    sans=(random.choice(yaziTura)) 
    if secim=="y":
        secim="yazı"
    else:
        secim="tura"
    if secim==sans:
        time.sleep(0.5)
        print(f"Doğru bildiniz {sans} geldi")
    else:
        time.sleep(0.5)
        print(f"Yanlış bildiniz {sans} geldi")

def main():
    yaziTuraAt()

if __name__ == "__main__":
    main()