consecutive_ones_count = 0
lst_consecutive_ones_count = [0]
n = int(input())
binary_form = "{0:0b}".format(n)
for i in range(len(binary_form)):
    if i == 0:
        if binary_form[i] == "1":
            consecutive_ones_count = 1
    else:
        if binary_form[i] == "1":
            if binary_form[i-1] == "1":
                consecutive_ones_count += 1
            else:
                lst_consecutive_ones_count.append(consecutive_ones_count)
                consecutive_ones_count = 1
        else:
            lst_consecutive_ones_count.append(consecutive_ones_count)
            consecutive_ones_count = 0

print(binary_form)
print("Max_Consecutive_Ones : " + str(max(lst_consecutive_ones_count)))