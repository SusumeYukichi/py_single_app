import sys
from pathlib import Path

"""
<実行コマンド>
python3 app_02.py sample.txt output.txt
<詳細>
引数-2:読込先
引数-3:出力先
"""

# 区切線
line_obj = "=" * 30

print(line_obj)
print("<プログラム開始>")
print(line_obj)

# パス定義
file_obj = Path(__file__)
directory = file_obj.parent


# コマンドライン引数-2
def get_file_path():
    try:
        file_path = directory / sys.argv[1]
        assert sys.argv[1] == "sample.txt", "引数-2と異なります"
    # 例外処理
    except IndexError:
        print("コマンドラインの第2引数が未設定です")
        print("プログラム終了します")
        sys.exit()

    return file_path


# コマンドライン引数-3
def get_output_path():
    try:
        output_path = directory / sys.argv[2]
        assert sys.argv[2] == "output.txt", "引数-3と異なります"
    # 例外処理
    except IndexError:
        print("コマンドラインの第3引数が未設定です")
        print("プログラム終了します")
        sys.exit()

    return output_path


# ファイル読込
def read_file():
    file_path = get_file_path()
    with open(file_path, encoding="utf-8") as file:
        try:
            read_obj = file.read()
        # 例外処理 読込ファイル検証
        except FileNotFoundError:
            print("読込ファイルが存在しません")
            print("プログラム終了します")
            sys.exit()

    return read_obj


# 読込ファイル加工処理
def get_read_obj(read_obj):
    new_list = []
    list_obj = read_obj.split()

    # 加工処理 "･"記号追加
    for my_obj in list_obj:
        new_list.append(f"･{my_obj}")

    join_obj = "\n".join(new_list)

    return join_obj


# ファイル出力
def get_write(save_obj):
    output_path = get_output_path()
    with open(output_path, "w", encoding="utf-8") as file:
        # 文字型検証
        assert type(save_obj) == str, "ファイル出力エラー!"

        # 開始位置検証
        assert save_obj.startswith("･")

        # 改行処理検証
        assert "\n" in save_obj

        # 終了位置検証
        assert save_obj.endswith("。")

        file.write(save_obj)


# ======================================
# ファイル読込
read_obj = read_file()
print(line_obj)
print("ファイル読込完了")
print(line_obj)
# ======================================
# 文字加工処理
join_obj = get_read_obj(read_obj)
print(line_obj)
print("<ファイル加工処理完了>")
print(line_obj)
# ======================================
# ファイル出力
get_write(join_obj)
# ======================================
print(line_obj)
print("<ファイル出力処理完了>")
print(line_obj)
