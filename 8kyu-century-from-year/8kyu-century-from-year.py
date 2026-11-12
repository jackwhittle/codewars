"""Codewars 8 kyu: Century From Year.

https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

The first century spans years 1-100, the second 101-200, and so on.
"""


def century(year):
    return (year + 99) // 100


if __name__ == "__main__":
    for y in (1705, 1900, 1601, 2000, 2742):
        print(y, "->", century(y))
