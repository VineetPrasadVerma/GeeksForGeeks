def length(s, count):
    if s == "":
        return count
    count += 1
    return length(s[1:], count)

print(length("GEEKSFORGEEKS", 0))