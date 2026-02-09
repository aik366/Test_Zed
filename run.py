def main(zakaz):
    with open(r"DATA\22.txt", "r") as file:
        data = [i.strip().split("\n") for i in file.read().split("#@#\n")[1:]]
        for i in data:
            if i[0][:4] == zakaz:
                return [
                    j.replace("||", "|", 1).replace("/", "|").split("|")[:9]
                    for j in i[2:]
                ]


def main_2(zakaz):
    with open(r"DATA\22.txt", "r") as file:
        data = [i.strip().split("\n") for i in file.read().split("#@#\n")[1:]]
        for i in data:
            if i[0][:4] == zakaz:
                return [j.split("|") for j in i[:2]]


if __name__ == "__main__":
    print(main_2("0002")[0])
