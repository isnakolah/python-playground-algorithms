def drinking(age):
    if age >= 18:
        return True

    return False


def driving(age):
    if age >= 16:
        return True

    return False


def drinking_and_driving(age):
    if drinking(age) and driving(age):
        return True

    return False


mitchelle = 17
ngugi = 20

print(drinking_and_driving(mitchelle))
