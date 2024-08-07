def puanHesaplama():
    print("Cevap anahtarını kaydediniz:(çıkmak için q yazıp entera basınız)")
    cevaplar=[]
    yanitlar=[]
    Cevap=" "
    Cevap2=" "
    a=1
    dogru=0
    yanlis=0
    while Cevap!="q":
        Cevap=input(f"{a}. sorunun cevabı?")
        a+=1
        if Cevap !="": cevaplar.append(Cevap)
    print("-"*20)
    print("Ogrencinin cevaplarini kaydediniz:(çıkmak için q yazıp entera basınız)")
    a=1
    loop=(len(cevaplar))
    loop=loop-1
    for a in range(loop):
        a+=1
        Cevap2=input(f"{a}. sorunun cevabı?")
        if Cevap2 !="": yanitlar.append(Cevap2)
    b=0
    for b in range (loop):
        if (cevaplar[b]==yanitlar[b]):
            dogru+=1
        else:
            yanlis+=1
    print(f"Puanı: {(100/loop)*dogru}")       
def main():
    puanHesaplama()

if __name__ == "__main__":
    main()