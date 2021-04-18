import random


def checkBirthDate(year: int, month: int, day: int):
    if year >= 1800 and year <= 1899:
        month = month + 80
    elif year >= 2000 and year <= 2099:
        month = month + 20
    elif year >= 2100 and year <= 2199:
        month = month + 40
    elif year >= 2200 and year <= 2299:
        month = month + 60
    elif year >= 1900 and year <= 1999:
        month = month + 0
        if len(str(month)) == 1:
            month = str(month).zfill(2)
    if len(str(day)) == 1:
        day = str(day).zfill(2)
    year = str(year)[2:]
    month = str(month)
    day = str(day)
    date = year + month + day
    # print("Pesel: " + date)
    list = []
    for i in date:
        list.append(int(i))
    return list


class PeselGen:
    import random
    def __init__(self):
        super().__init__()

    def generate(self, year, month, day, sex):
        # print(year, month, day, sex)
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.sex = int(sex)
        # print(self.year, self.month, self.day, self.sex)
        birthDate = checkBirthDate(self.year, self.month, self.day)
        controlNumbers = str(random.randrange(1000)).zfill(3)
        for i in controlNumbers:
            birthDate.append(int(i))

        if sex == 2:
            sexNum = random.randrange(0, 10, 2)
        elif sex == 1:
            sexNum = random.randrange(1, 10, 2)
        else:
            sexNum = random.randrange(0, 10, 1)
        birthDate.append(sexNum)

        controlCheck = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        sum = 0
        for i in birthDate:
            sum = sum + birthDate[i] * controlCheck[i]
        print(sum)
        birthDate.append(sum%10)
        print(birthDate)

        birthDateStr = ""
        for i in birthDate:
            birthDateStr = birthDateStr + str(i)
        print("BirthDateStr " + birthDateStr)

        return birthDateStr

        # print("trzy cyfry random: " + str(random.randrange(1000)).zfill(3))
        # print("Parzyste - kobiety: " + str(random.randrange(0,10,2)))
        # print("Nieparzyste - mężczyźni: " + str(random.randrange(1,10,2)))

