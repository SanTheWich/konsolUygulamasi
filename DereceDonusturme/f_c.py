#! °C = (°F – 32) / 1.8
def fahrenheitCelsius():
    fahrenheit=float(input("Lütfen derecenizi Fahrenheit cinsinden giriniz: "))
    celsius=((fahrenheit-32)/1.8)
    print(f"Dereceniz celsius cinsinden {celsius}°C")
def main():
    fahrenheitCelsius()

if __name__ == "__main__":
    main() 