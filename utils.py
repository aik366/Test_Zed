from config import *
from datetime import datetime
import shutil

now = datetime.now()
year = now.strftime("%y")
year_1 = str(int(year) - 1)
month = now.month
day = now.day


def order_year(god: str = year) -> list:
    shutil.copyfile(f'{put}{god}.RSB', f'DATA/22.txt')
    with open(r"DATA\22.txt", "r", encoding='utf-8') as file:
        return [i.strip().split("\n") for i in file.read().split("#@#\n")[1:]]


def order_two_year(god: str = year) -> list:
    shutil.copyfile(f'{put}{god}.RSB', f'DATA/22.txt')
    shutil.copyfile(f'{put}{int(god) - 1}.RSB', f'DATA/22_two.txt')
    with open(r"DATA\22.txt", "r") as file:
        with open(r"DATA\22_two.txt", "a") as file_two:
            file_two.write(file.read())
    with open(r"DATA\22_two.txt", "r") as file_two:
        return [i.strip().split("\n")[:2] for i in file_two.read().split("#@#\n")[1:]]


def metraj_year(god: int = year, months: int = month) -> float:
    summ = 0.0
    for i in order_two_year(str(god)):
        str_split = i[0].split("|")
        if str_split[5][:2] == str(god) and str_split[14] == f"{months:02}":
            summ += float(str_split[23])
    return round(summ)


def order_work(order: str, god: str = year) -> list:
    for i in order_year(god):
        if i[0][:4] == order:
            return [j.replace("||", "|", 1).replace("/", "|").split("|")[:9] for j in i[2:]]
    return []


def str_all(order: str, god: str = year) -> list:
    for i in order_year(god):
        if i[0][:4] == order:
            return [j.split("|") for j in i[:2]]
    return []


def str_one(order: str, god: str = year) -> list:
    for i in order_year(god):
        if i[0][:4] == order:
            return i[0].split("|")
    return []


def str_two(order: str, god: str = year) -> list:
    for i in order_year(god):
        if i[0][:4] == order:
            return i[1].split("|")
    return []


if __name__ == "__main__":
    print([metraj_year(god=24, months=i) for i in range(1, 13)])
    # metraj_year(year=25,month=2)
    # for i in order_work("0002"):
    #     print(i)
    # for i in order_two_year():
    #     print(i)
    # print(order_two_year())
    # my_data: list = str_all("0002")
    # my_data_1: list = str_all("0002", year_1)
    # # my_data_two: int = len(order_two_year())

    # print(my_data[0][1], my_data[1][25])
    # print(my_data_1[0][1], my_data[1][25])
    # print(str_one("0004")[1], str_two("0004")[25])
    # print(str_one("0004", year_1)[1], str_two("0004", year_1)[25])
