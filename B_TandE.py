"""
課題B-1: 日本の九九表
"""
# defはつかえないか？///NG
def kuku_number(num1, num2):
    for num1 in range(1, 10):
        for num2 in range(1, 10):
            return num1 * num2
        # print(" ".join(kuku.splitlines()))


# 1の段を計算して改行、同じ動きを2の段以降も繰り返す
for number in range(1, 10):
    print(1 * number, end=" ")

print(sep="")

for number in range(1, 10):
    print(2 * number, end=" ")

"""
課題B-2: 九九表の拡張
"""
"""
課題B-3: きれいな九九表
"""

# 使えそうな演算子？
num = 100
print("%06s" % (int(num) * 2))
print("{:0>6s}".format(str(num)))
print("zero padding: %06s" % num)

# ベース
step_number = int(input("行数を入力してください: "))
time_number = int(input("列数を入力してください: "))

for num1 in range(1, int(step_number) + 1):
    for num2 in range(1, int(time_number) + 1):
        print(num1 * num2, end=" ")
        if num2 == int(time_number):
            print(sep="")

"""
課題B-4: 天気情報の分析
3都府県のいくつかの駅名とある日の最高気温のデータを
辞書として持っています
このデータを使って3つの問を満たす実装をしてください

    # Q1. 全国の平均気温を計算してください(9.5となればOK)

    # Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

    # Q3. 福岡県の平均気温を計算してください(14.0となればOK)


def main():
    # 3都府県のいくつかの駅名とある日の最高気温(単位: ℃)のデータを辞書として持っています
"""

# 挙動確認
from locale import LC_MONETARY
from pydoc import tempfilepager

# osaka = weather_information.keys("大阪府")
# if l in weather_information.keys("大阪府"):
# print(l)

# if osaka in weather_information:
# print(f"{weather_information}")

print(weather_information[0])

# get()メソッド・・・オブジェクト専用の関数 辞書型以外には使えない
l_menbers = [{"name": "ken", "age": "10"}, {"name": "jhon", "age": "9"}]

print(next((i for i, x in enumerate(l_menbers) if x["name"] == "ken"), None))

# l_name = [d.get("name") for d in l_menbers if ["age"] == 10]
# l_age = [d.get("age") for d in l_menbers]
# print(f"{l_name}'/'{l_age}")


# sum関数
# Q1. 全国の平均気温を計算してください(9.5となればOK)
print("<Q1_全国の平均気温>")
l_temp = [d.get("temperature") for d in weather_information]
print(l_temp)
print(sum(l_temp) / len(l_temp))  # typeがおかしいみたい・・・あとで確認

print(l_temp[0])
print(type(l_temp[0]))

# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)

# l_osaka_station = [
# d.get("station")
# for d in weather_information
# if "prefecture" == "大阪府"
# ]

# prefectureが大阪府の辞書を取り出す
print(weather_information[0])

# step1:大阪府の辞書を取り出す
"""
print(
    next(
        (i for i, x in enumerate(weather_information) if x["prefecture"] == "福岡県"), None
    )
) #このコードが何を示すか不明。。。あとで確認
"""
l_osaka = [item for item in weather_information if item["prefecture"] == "大阪府"]
print(l_osaka)

# step2:stationをgetする
l_osaka_station = [d.get("station") for d in l_osaka]
print(l_osaka_station)
print(l_osaka_station[0])

print("<Q2_大阪府の駅>")
for number in range(0, 2):
    print(f"{l_osaka_station[number]}" ",", end="")
print(f"{l_osaka_station[2]}", sep="")

print(sep="")

# Q3. 福岡県の平均気温を計算してください(14.0となればOK)
# step1:福岡県の辞書を抽出する
l_hukuoka = [item for item in weather_information if item["prefecture"] == "福岡県"]

# step2:福岡県のtempuratureをgetする
l_hukuoka_temperature = [d.get("temperature") for d in l_hukuoka]

print("<Q3_福岡県の平均気温>")
print(sum(l_hukuoka_temperature) / 2)  # typeが不明

"""
課題B-5:基本統計量の計算
スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
・合計値
・最大値
・最小値
・平均値
ただし、組み込み関数やライブラリは使わないこと(sum()やnp.mean()など)
1つの統計量につき、それ専用の関数を実装すること
"""
input_numbers = input("データを入力してください(スペース区切り) > ")
print(input_numbers)

# split()メソッド
print(f"{input_numbers}".split(" "))  # ///error リストは対応していない
from audioop import maxpp
import statistics

l_si_numbers = f"{input_numbers}".split(" ")
l_in_numbers = [int(s) for s in l_si_numbers]
print(l_in_numbers)
print(f"合計値: {sum(l_in_numbers)}")
print(f"最大値: {max(l_in_numbers)}")
print(f"最小値: {min(l_in_numbers)}")
print(f"平均値: {statistics.mean(l_in_numbers)}")

# 組み込み関数つかっちゃダメよー
"""
def sum_number():
    for number in range(0, len(l_in_numbers)):
        print(l_in_numbers)
"""

min = l_in_numbers[0]
for num in range(0, len(l_in_numbers)):
    if l_in_numbers[num] < min:
        min = l_in_numbers[num]

print(f"最小値:{min}")


max = l_in_numbers[0]
for num in range(0, len(l_in_numbers)):
    if l_in_numbers[num] > max:
        max = l_in_numbers[num]

print(f"最大値:{max}")

sum = 0
for num in l_in_numbers:
    sum += num

print(f"合計値:{sum}")

mean = sum / len(l_in_numbers)

print(f"平均値:{mean}")


# n = int(f"{input_numbers}".split(" ")) ///error リストはintできない
# print(sum(input_numbers)) ///error int,str

# リストのint変換
l_si = ["1", "2", "3"]
l_si_i = [int(s) for s in l_si]
print(l_si_i)
print(type(l_si_i[0]))
# OKうまくいった！


"""
N面サイコロ
"""
ice_nums = input("サイコロの面の数は？: ")
dice_times = input("何回振りますか？: ")

# サイコロの面出力
"""
失敗
for n in range(0,int(dice_nums)):
    print(n+1)
    l_saikoro = [n+1]
    print(l_saikoro)
"""
l_saikoro = list(range(1, int(dice_nums) + 1))
print(l_saikoro)

import random


def dice():
    return random.choice(l_saikoro)


for n in range(1, int(dice_times)):
    print(f"{dice()},", end="")

print(sep="")

for n in range(1, int(dice_times) + 1):
    print(f"{random.choice(l_saikoro)} ", end="")

print(sep="")

# これだrandom.randint
random_nums = [random.randint(1, int(dice_nums)) for i in range(int(dice_times))]
print(random_nums)
"""
sai = []
    for n in range(1, int(dice_times) + 1):
        return(random.choice(l_saikoro))

print(sai)
"""

# r = list(saikoro())
# print(r)
"""
def result():
    for n in range(1, int(dice_times)):
         dice()
"""

# print(result())


# print(random.choice(l_saikoro))
