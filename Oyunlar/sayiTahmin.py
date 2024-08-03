def sayiBilmeceOyna():
    import random
    sayi=(random.randint(1,10))
    hak=3
    puan=100
    for a in range (3):
        tahmin=int(input("\033[1;31;40m1 ile 10 arasindan sayi tahmin ediniz: \033[1;32;40m  "))
        if sayi==tahmin:
            print(f"Doğru bildiniz \n Puaniniz {puan}")
            break
        elif hak>1:
            hak=hak-1
            puan=puan-10
            if sayi<tahmin:
               print(f"Bilemediniz {hak} hakkiniz kaldi (Sayini küçült ↓)")
            else:
                print(f"Bilemediniz {hak} hakkiniz kaldi (Sayini büyült ↑)")
        else:
            print("Hakkin kalmadi kaybettin.")
def main():
    sayiBilmeceOyna()

if __name__ == "__main__":
    main()