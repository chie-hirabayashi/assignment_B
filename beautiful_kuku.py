step_number = int(input("行数を入力してください: "))
time_number = int(input("列数を入力してください: "))


for num1 in range(1, int(step_number) + 1):
    for num2 in range(1, int(time_number) + 1):
        print(
            "%03s" % num1,
            "×" "%03s" % num2,
            "=" "%03s" % (int(num1) * int(num2)),
            "|",
            end=" ",
        )
        if num2 == int(time_number):
            print(sep="")
