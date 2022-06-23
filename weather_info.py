weather_information = [
    {"prefecture": "東京都", "station": "渋谷", "temperature": 6.5},
    {"prefecture": "東京都", "station": "池袋", "temperature": 7.0},
    {"prefecture": "東京都", "station": "新橋", "temperature": 7.5},
    {"prefecture": "大阪府", "station": "梅田", "temperature": 8.2},
    {"prefecture": "大阪府", "station": "大阪", "temperature": 9.3},
    {"prefecture": "大阪府", "station": "堺", "temperature": 9.5},
    {"prefecture": "福岡県", "station": "博多", "temperature": 13.0},
    {"prefecture": "福岡県", "station": "太宰府", "temperature": 15.0},
]

# Q1. 全国の平均気温を計算してください(9.5となればOK)
print("<Q1_全国の平均気温>")
l_temp = [d.get("temperature") for d in weather_information]
print(sum(l_temp) / len(l_temp))  # typeがおかしいみたい・・・あとで確認

print(sep="")

# Q2. 大阪府のすべての駅名をカンマ区切りで出力してください( '梅田,大阪,堺' となればOK)
# step1:大阪府の辞書を取り出す
l_osaka = [item for item in weather_information if item["prefecture"] == "大阪府"]

# step2:stationをgetする
l_osaka_station = [d.get("station") for d in l_osaka]

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
