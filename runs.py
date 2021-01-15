def achieved(run, target):
    distance = 0

    for i in range(len(run)):
        if run[i] == "R":
            distance += 100
        else:
            continue
    if distance >= target:
        return True

    return False


run1 = "RRWRRRRWWWRRW"

print(achieved(run1, 700))
