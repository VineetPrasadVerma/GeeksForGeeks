lists = list(map(int, input().split()))

ans_list = []
for i in range(len(lists)):
    for j in range(i+1, len(lists)+1):
        ans_list.append(lists[i:j])

print(ans_list)
        