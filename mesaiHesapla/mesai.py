def Mesaihesapla():
    print("Mesai ücreti dahil maaş hesaplayıcıya hoşgeldiniz.")
    calisanlar=[]
    maaslar=[]
    mesaiSaatleri=[]
    mesaiUcretleri=[]
    eklencek=" "
    eklencek2=" "
    i=0
    #çalışan isim kayıt kısmı
    while eklencek!="":
        i+=1
        eklencek=input(f"Çalışan {i}: ")
        if eklencek !="": calisanlar.append(eklencek)
    print("Girdiğiniz çalişanlar: ",*calisanlar,sep="\n")
    #maaş kayıt kısmı
    i=0
    while eklencek2!="":
        i+=1
        eklencek2=int(input(f"Calisan {i} maasi: "))
        if eklencek2 !="": maaslar.append(eklencek2)
    print("Girdiğiniz maaşlar: ",*maaslar,sep="\n")


def main():
    Mesaihesapla()

if __name__ == "__main__":
    main()