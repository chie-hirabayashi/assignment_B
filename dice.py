dice_nums = input("サイコロの面の数は？: ")
dice_times = input("何回振りますか？: ")

l_saikoro = list(range(1, int(dice_nums) + 1))

import random


def dice():
    return random.choice(l_saikoro)


random_nums = [random.randint(1, int(dice_nums)) for i in range(int(dice_times))]
print(random_nums)
