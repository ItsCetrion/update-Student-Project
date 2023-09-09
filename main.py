dict_ = {1:"Января", 2:"Февраля", 3:"Марта", 4:"Апреля", 5:"Мая", 6:"Июня", 7:"Июля", 8:"Августа", 9:"Сентября", 10:"Октября", 11:"Ноября", 12:"Декабря"}
class Currency:
    "Информация о валюте в рублях"
    def __init__(self, FirstRate: str, SecondRate: str, rate: float, data: str) -> None:
        data = data.split(".")
        self.FirstRate, self.SecondRate, self.rate, self.data = FirstRate, SecondRate, rate, Data(data[0], data[1], data[2])
class Data:
    def __init__(self, day: str, month: str, year: str):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

def file_operations() -> None:
    with open("test.txt") as file:
        CurrencyInformation = list()
        while True:
            FirstRate = file.readline()
            if FirstRate == "":
                break
            else:
                FirstRate = FirstRate[:-1]
            SecondRate = file.readline()[:-1]
            rate = file.readline()[:-1]
            data = file.readline()
            if data[-1] == "\n":
                data = data[:-1]
            CurrencyInformation.append(Currency(FirstRate, SecondRate, rate, data))
    for i in CurrencyInformation:
        print(f"Курс {i.SecondRate} на {i.FirstRate} составляет {i.rate} на {i.data.day} {dict_.get(i.data.month)} {i.data.year}")
file_operations()


