import sys
from pathlib import Path

print("*" * 30)
print("<プログラム開始>")
print("<パス移動>:cd apps")
print("<実行コマンド>:python3 app_02.py sample.txt output.txt")
print("*" * 30)

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

"""
コマンド詳細:
<実行プログラム>:app_02.py
<読込ファイル>:sample.txt
<出力ファイル名指定>:output.txt
"""

try:
    file_obj = Path(__file__)
    directory = file_obj.parent

    file_path = directory / sys.argv[1]
    output_path = directory / sys.argv[2]

    path_dict = {
        "name": output_path.stem,
        "suffix": output_path.suffix,
    }

    # 引数検証
    assert path_dict["name"] == "output", "引数のファイル名が異なります"
    assert path_dict["suffix"] == ".txt", "引数の拡張子が異なります"
    print("<実行コマンド指定完了>")

# 例外処理
except IndexError:
    print("コマンドライン引数が未設定です")
    print("プログラム終了します")
    sys.exit()


# ファイル読込
def read_file():
    with open(file_path, encoding="utf-8") as file:
        read_obj = file.read()
    return read_obj


try:
    read_obj = read_file()

# 例外処理
except FileNotFoundError:
    print("読込ファイルが存在しません")
    sys.exit()


# list型変換
def get_split_list(read_obj):
    split_obj = read_obj.split()
    return split_obj


# 加工処理 "･"記号追加
def get_new_list(get_split):
    new_list = []

    for my_obj in get_split:
        new_list.append(f"･{my_obj}")

    if new_list:
        join_data = "\n".join(new_list)
        print("<ファイル加工処理完了>")
        return join_data

    else:
        print("リストが空です")


# ファイル出力
def get_write(save_obj):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(save_obj)

    return save_obj


split_obj = get_split_list(read_obj)
join_data = get_new_list(split_obj)
result = get_write(join_data)


print("<出力結果検証>")

# 文字型検証
assert type(result) == str, "ファイル出力エラー!"

# 開始位置検証
assert result.startswith("･")

# 改行処理検証
assert "\n" in result

# 末尾改行検証
assert result[-1] != "\n", "末尾に改行が含まれています"

# 終了位置検証
assert result.endswith("。")

print("<検証終了>")

print("*" * 30)
print("<ファイル出力処理完了>")
print("*" * 30)
