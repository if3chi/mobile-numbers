import phonenumbers
from phonenumbers import geocoder, carrier

class Mobile:
    lang: str
    number: str

    def __init__(self, number: str, lang: str):
        self.lang = lang
        self.number = self.__parse_number(number)

    def __parse_number(self, number: str):
        return phonenumbers.parse(number, None)

    def get_country(self) -> str:
        return geocoder.description_for_number(self.number, self.lang)

    def get_carrier(self) -> str:
        return carrier.name_for_number(self.number, self.lang)
