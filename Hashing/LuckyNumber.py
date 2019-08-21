n = int(input())
for _ in range(n):
    num = input()
    total_numbers_list = []
    digits_product_list = []
    for i in range(len(num)):
        for j in range(len(num)-i):
            total_numbers_list.append(int(num[j:j+i+1]))
            temp = total_numbers_list[-1]
            is_zero = temp
            products = 1
            while temp != 0:
                products *= temp % 10
                temp //= 10
            if is_zero == 0:
                digits_product_list.append(0)
            else:
                digits_product_list.append(products)
    print(total_numbers_list)
    print(digits_product_list)
    temp1 = set(digits_product_list)
    if len(temp1) == len(digits_product_list):
        print(1)
    else:
        print(0)
