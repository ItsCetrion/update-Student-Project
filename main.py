dict_ = {1:"Января", 2:"Февраля", 3:"Марта", 4:"Апреля", 5:"Мая", 6:"Июня", 7:"Июля", 8:"Августа", 9:"Сентября", 10:"Октября", 11:"Ноября", 12:"Декабря"}
class Currency:
    "Информация о валюте в рублях"
    def __init__(self, FirstRate: str, SecondRate: str, rate: float, data) -> None:
        self.FirstRate, self.SecondRate, self.rate, self.data = FirstRate, SecondRate, rate, data
class Data:
    def __init__(self, data: str):
        data = data.split(".")
        self.day = int(data[0])
        self.month = int(data[1])
        self.year = int(data[2])
    def __str__(self):
        return f"{self.day} {dict_.get(self.month)} {self.year}"

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

            data = Data(data)
            CurrencyInformation.append(Currency(FirstRate, SecondRate, rate, data))
    for i in CurrencyInformation:
        print(f"Курс {i.SecondRate} на {i.FirstRate} составляет {i.rate} на {i.data}")
file_operations()


