def ritmiksay():
    print("╔════════════════════════════════════╗")
    print("║\033[1;31;40m  RİTMİK SAYMAYA HOŞGELDİNİZ \033[1;32;40m       ║")
    a=int(input("║Kaçtan baslamasini istiyorsunuz?    ║"))
    b=int(input("║Kaça kadar saymasini istiyorsunuz?  ║"))
    c=int(input("║Kaçar kaçar saymasiini istiyorsunuz?║"))
    print("╚════════════════════════════════════╝")
    for x in range(a,b,c):
        print(x)
def main():
    ritmiksay()

if __name__ == "__main__":
    main()