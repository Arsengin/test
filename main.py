lst = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]
count = 0
leng = 0
# col_count =
for row in range(len(lst)):
    for col in range(len(lst[row])):
        for row_dx in [-1, 0, 1]:
            for col_dx in [-1, 0, 1]:
                neighbour = lst[row + row_dx][col + col_dx]
                # if row == 0 and leng != 0:
                #     count += 1
                #     leng = 0
                # elif row == 0:
                #     leng = 0
                # elif row == 1:
                #     leng += 1
print(count)