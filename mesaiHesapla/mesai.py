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
    loop=(len(calisanlar))
    for a in range(loop):
        i+=1
        eklencek2=int(input(f"Calisan {i} maasi: "))
        if eklencek2 !="": maaslar.append(eklencek2)
    print("Girdiğiniz maaşlar: ",*maaslar,sep="\n")
    i=0
    for a in range(loop):
        i+=1
        eklencek2=int(input(f"Calisan {i} ek mesai saati: "))
        if eklencek2 !="": mesaiSaatleri.append(eklencek2)
    print("Girdiğiniz mesai saatleri: ",*mesaiSaatleri,sep="\n")
    
    i=0
    for a in range(loop):
        i+=1
        eklencek2=int(input(f"Calisan {i} saat başı ek mesai ücreti: "))
        if eklencek2 !="": mesaiUcretleri.append(eklencek2)
    print("Girdiğiniz mesai ek ücretleri: ",*mesaiUcretleri,sep="\n")
    i=0
    for a in range(loop):
        maaslar[i]=(maaslar[i]+(mesaiSaatleri[i]*mesaiUcretleri[i]))
        print(f"Çalışan {i+1} maaşı: {maaslar[i]}")
        i+=1
def main():
    Mesaihesapla()

if __name__ == "__main__":
    main()