def sockMerchant(n, ar):
    socks_dict = {}
    for i in ar:
        if i not in socks_dict:
            socks_dict[i] = 1
        else:
            socks_dict[i] += 1
    total_pairs = 0
    for val in socks_dict.values():
        total_pairs += val//2