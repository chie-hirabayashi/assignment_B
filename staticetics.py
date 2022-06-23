from __future__ import annotations
import staticetics
from audioop import maxpp
import statistics

input_numbers = input("データを入力してください(スペース区切り) > ")


l_si_numbers = f"{input_numbers}".split(" ")
l_in_numbers = [int(s) for s in l_si_numbers]
print("組み込み関数")
print(f"合計値: {sum(l_in_numbers)}")
print(f"最大値: {max(l_in_numbers)}")
print(f"最小値: {min(l_in_numbers)}")
print(f"平均値: {statistics.mean(l_in_numbers)}")

# 組み込み関数つかっちゃダメよー
print(sep="")
print("基本統計量の計算")

sum = 0
for num in l_in_numbers:
    sum += num

print(f"合計値: {sum}")

max = l_in_numbers[0]
for num in range(0, len(l_in_numbers)):
    if l_in_numbers[num] > max:
        max = l_in_numbers[num]

print(f"最大値: {max}")

min = l_in_numbers[0]
for num in range(0, len(l_in_numbers)):
    if l_in_numbers[num] < min:
        min = l_in_numbers[num]

print(f"最小値: {min}")


mean = int(sum / len(l_in_numbers))

print(f"平均値: {mean}")
