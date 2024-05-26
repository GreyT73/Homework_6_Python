"""Предлагает четыре расстановки на шахматной доске, при которых восемь ладей не будут бить друг друга"""


from random import randint


def find_solution():
    flag = False
    count = 0
    while not flag or count < 4:
        queens = [[randint(1, 8), randint(1, 8)] for i in range(8)]
        flag = True
        hor, ver = [], []
        for i in queens:
            hor.append(i[0])
            ver.append(i[1])
        if not (len(hor) == len(set(hor)) and len(ver) == len(set(ver))):
            flag = False
        else:
            count += 1
            print(f'В такой расстановке ладьи не будут бить друг друга: {queens}')


if __name__ == "__main__":
    find_solution()
