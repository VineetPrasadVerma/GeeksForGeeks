def countingValleys(n, s):
    v = 0
    m = 0
    total_valeys_cover = 0
    for step in s:
        if step == "D":
            v += 1
        if step == "U":
            m += 1
        if v == m and v != 0:
            if step == "U":
                total_valeys_cover += 1
                m = 0
                v = 0
            else:
                m = 0
                v = 0
    return total_valeys_cover