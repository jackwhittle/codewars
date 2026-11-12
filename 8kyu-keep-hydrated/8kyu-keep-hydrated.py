"""Codewars 8 kyu: Keep Hydrated!

https://www.codewars.com/kata/582cb0224e56e068d800003c

Nathan drinks 0.5 litres of water per hour of cycling. Given the time in
hours, return the litres he drinks, rounded down to a whole number.
"""


def litres(time):
    return int(time * 0.5)


if __name__ == "__main__":
    for t in (3, 6.7, 11.8):
        print(t, "->", litres(t))
