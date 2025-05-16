# 数列の入力を受け取る（スペース区切りの数字を想定）
numbers = input("スペース区切りで数字を入力してください: ")

# 文字列を数値のリストに変換
number_list = [int(x) for x in numbers.split()]

# 合計を計算
total = sum(number_list)
# 答えがマイナスかどうかを判定する
if total < 0:
    print("合計はマイナスです。")
else:
    print("合計はマイナスではありません。")

# 結果を出力
print(f"入力された数列の合計: {total}")