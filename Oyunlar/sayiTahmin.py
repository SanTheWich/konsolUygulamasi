def sayiBilmeceOyna():
    import random
    sayi=(random.randint(1,10))
    hak=5
    puan=100
    for a in range (3):
        tahmin=int(input("1 ile 10 arasindan sayi tahmin ediniz: "))
        if sayi==tahmin:
            print(f"Doğru bildiniz \n Puaniniz {puan}")
            break
        elif hak>1:
            hak=hak-1
            puan=puan-10
            print(f"Bilemediniz {hak} hakkiniz kaldi")
        else:
            print("Hakkin kalmadi kaybettin.")
def main():
    sayiBilmeceOyna()

if __name__ == "__main__":
    main()