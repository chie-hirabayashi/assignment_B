input_numbers = input("データを入力してください(スペース区切り) > ")

l_si_numbers = f"{input_numbers}".split(" ")
l_in_numbers = [int(s) for s in l_si_numbers]


def sum():
    sum_num = 0
    for num in l_in_numbers:
        sum_num += num
    return sum_num


print(f"合計値:{sum()}")


def max():
    max_num = l_in_numbers[0]
    for num in range(0, len(l_in_numbers)):
        if l_in_numbers[num] > int(max_num):
            max_num = l_in_numbers[num]
    return max_num


print(f"最大値:{max()}")


def min():
    min_num = l_in_numbers[0]
    for num in range(0, len(l_in_numbers)):
        if l_in_numbers[num] < int(min_num):
            min_num = l_in_numbers[num]
    return min_num


print(f"最小値:{min()}")


def mean():
    sum_num = 0
    for num in l_in_numbers:
        sum_num += num
    return sum_num / len(l_in_numbers)


print(f"平均値:{mean()}")
