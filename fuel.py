def main():
        while True:
                try:
                    fraction = str(input("Fraction: "))
                    percent = round(convert(fraction))
                    if percent <= 100:
                          break
                except (ValueError, ZeroDivisionError):
                    pass

        if percent <= 1:
                print("E")
        elif percent >= 99:
                print("F")
        else:
                print(f"{percent}%")

def convert(fraction):
        x, y = fraction.split("/")
        return (int(x) / int(y)) * 100

main()
