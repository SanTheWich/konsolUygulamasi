#!°K = °C + 273.15
def celsiusKelvin():
    celsius=float(input("Lütfen derecenizi celsius cinsinden giriniz:"))
    kelvin=(celsius+273.150)
    print(f"Dereceniz kelvin cinsinden {kelvin} °K")
def main():
    celsiusKelvin()

if __name__ == "__main__":
    main() 