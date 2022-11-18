from model.number import number
from services.mobile import Mobile

LANG: str = "en"

def main():
    print("Mobile Number Info")

    mobile = Mobile(number, LANG)

    print(f"Country: {mobile.get_country()}\nCarrier: {mobile.get_carrier()}")

if __name__ == "__main__":
    main()
