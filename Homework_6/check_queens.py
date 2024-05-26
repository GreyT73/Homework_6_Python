"""Делает проверку, бьют ли восемь ферзей друг друга на стандартной шахматой доске. На вход необходимо подать список из восьми координат,
каждая из которых задана в следующем формате: [1, 1] """


def check_figures(queens: list):
    flag = True
    hor, ver = [], []
    for i in queens:
        hor.append(i[0])
        ver.append(i[1])
    if not (len(hor) == len(set(hor)) and len(ver) == len(set(ver))):
        flag = False
    else:
        for i in queens:
            for j in range(-7, 8):
                if j == 0:
                    continue
                else:
                    try:
                        if (
                                [i[0] + j, i[1] + j] in queens or [i[0] + j, i[1] - j] in queens or
                                [i[0] - j, i[1] + j] in queens or [i[0] - j, i[1] - j] in queens
                        ):
                            flag = False
                            break
                    except:
                        continue
    return "Ферзи не бьют друг друга при такой расстановке" if flag else "Минимум два ферзя бьют друг друга"


if __name__ == "__main__":
    sample = [[2, 1], [4, 2], [6, 3], [8, 4], [3, 5], [1, 6], [7, 7], [5, 8]]
    print(check_figures(sample))
