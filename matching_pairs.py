def sockMerchant(n, ar):
    ass_socks = ar
    sort_socks = {}
    pairs = 0

    for i in range(len(ass_socks)):
        if ass_socks[i] in sort_socks:
            sort_socks[ass_socks[i]] = sort_socks[ass_socks[i]] + 1
        else:
            sort_socks[ass_socks[i]] = 1

    for amount in sort_socks.values():
        pairs += amount//2

    return pairs


if __name__ == "__main__":
    print(sockMerchant(7, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
