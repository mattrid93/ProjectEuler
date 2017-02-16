"""Problem 19: Counting Sundays.

Directly count."""

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def count_sundays():
    y = 1
    m = 1
    d = 1
    count = 0
    while y < 100:
        d += months[m]
        if not y%4 and m == 2:
            d += 1
        if not (d%7):
            count += 1
        m += 1
        if m > 12:
            m = 1
            y += 1
    return count

if __name__ == "__main__":
    print(count_sundays())
