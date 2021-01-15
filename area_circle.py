import math


def area(r):
    if r > 0:
        area = math.pi * r * r
    else:
        raise ValueError("Error: Radius should be greater than 0\n")

    return round(area, 2)


if __name__ == "__main__":
    while True:
        inputed = input(
            "Write a number as a radius or \"q\" to exit the program\n-> ")
        if inputed == "q":
            print("quiting...")
            break
        else:
            radius = float(inputed)

        try:
            area(radius)
            print(area(radius))
        except ValueError as er:
            print(er)
            continue
