def order_list() -> list:
    with open(r"DATA\22.txt", "r") as file:
        return [i.strip().split("\n") for i in file.read().split("#@#\n")[1:]]


def order_work(order: str) -> list:
    for i in order_list():
        if i[0][:4] == order:
            return [
                j.replace("||", "|", 1).replace("/", "|").split("|")[:9] for j in i[2:]
            ]
    return []


def str_all(order: str) -> list:
    for i in order_list():
        if i[0][:4] == order:
            return [j.split("|") for j in i[:2]]
    return []


def str_one(order: str) -> list:
    for i in order_list():
        if i[0][:4] == order:
            return i[0].split("|")
    return []


def str_two(order: str) -> list:
    for i in order_list():
        if i[0][:4] == order:
            return i[1].split("|")
    return []


if __name__ == "__main__":
    for i in order_work("0002"):
        print(i)
    my_data: list = str_all("0002")
    print(my_data[0][1])
    print(my_data[1][25])
    print(str_one("0004")[1])
    print(str_two("0004")[25])
