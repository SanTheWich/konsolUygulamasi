#! °F = °C × 1.8 + 32
def celsiusFahrenheit():
    celsius=float(input("Lütfen derecenizi celsius cinsinden giriniz:"))
    fahrenheit=((celsius*1.8)+32)
    print(f"Dereceniz fahrenheit cinsinden {fahrenheit} °F")
def main():
    celsiusFahrenheit()

if __name__ == "__main__":
    main() 