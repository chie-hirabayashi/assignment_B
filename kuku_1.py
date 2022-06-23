# part2  九九計算(改行あり)
for num1 in range(1, 10):
    for num2 in range(1, 10):
        print(num1 * num2, end=" ")
        if num2 == 9:
            print(sep="")
