#!°C = °K – 273.15
def kelvincelsius():
    kelvin=float(input("Lütfen derecenizi kelvin cinsinden giriniz:"))
    celsius=(kelvin-273.150)
    print(f"Dereceniz celsius cinsinden {celsius} °K")
def main():
    kelvincelsius()

if __name__ == "__main__":
    main() 