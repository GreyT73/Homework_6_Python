"""Проверяет дату на возможность ее существования в Григорианском календаре.
На вход принимает текст в формате 'ДД.ММ.ГГГГ'"""

from sys import argv


def _is_leap_year(y: int) -> bool:
    return False if y % 400 != 0 and y % 100 == 0 or y % 4 != 0 else True


def data_check(date: str) -> bool:
    d, m, y = [int(i) for i in date.split('.')]
    match m:
        case 1 | 3 | 5 | 6 | 8 | 10 | 12:
            max_day = 31
        case 4 | 6 | 9 | 11:
            max_day = 30
        case 2:
            max_day = 29 if _is_leap_year(y) else 28
        case _:
            return False
    if not (1 <= y <= 9999 and 1 <= d <= max_day):
        return False
    else:
        return True


if __name__ == "__main__":
    print(data_check(argv[1]))
