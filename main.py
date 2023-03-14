#### DOUBLE SHIFT #### to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    print(get_gcd(8, 50))


def get_gcd(x, y):
    while y != 0:
        t = x
        x = y
        y = t % x
    return x


if __name__ == '__main__': main()

