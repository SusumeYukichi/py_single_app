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


# ファイルパス 取得 (読込先・出力先)
def get_file_path():
    dir_path = Path(__file__).parent
    if sys.argv[1] == "sample.txt":
        file_path = dir_path / sys.argv[1]
    else:
        print("読込先の引数を設定してください")
        sys.exit("プログラムを終了します")
    if sys.argv[2] == "output.txt":
        save_path = dir_path / sys.argv[2]
    else:
        print("出力先の引数を設定してください")
        sys.exit("プログラムを終了します")

    return file_path, save_path


# ファイル読込
def read_file(file_path, name):
    try:
        with open(file_path, encoding="utf-8") as file:
            read_obj = file.read()
            print(read_obj)

    # 例外処理 読込ファイル検証
    except FileNotFoundError:
        print("読込ファイルが存在しません")
        sys.exit("プログラムを終了します.")

    print(f"{line_obj}\n{name} 完了>\n{line_obj}")

    return read_obj


# オブジェクトのlist型変換
def get_list_obj(read_obj):
    list_obj = read_obj.split("\n")

    return list_obj


# 記号追加処理
def get_new_list(list_obj, name):
    new_list = []
    for i, obj in enumerate(list_obj):
        lines = obj.replace("：", ":\n").replace("。", ".")
        print(f"<行数:{i + 1}>\n{name} 実行")
        new_list.append(lines)
    print(f"{line_obj}\n{name} <すべて実行完了>\n{line_obj}")

    return new_list


# new_listのstr型変換
def get_new_obj(new_list):
    new_obj = "\n".join(new_list)

    return new_obj


# ファイル出力
def get_write(save_obj, save_path, name):
    with open(save_path, "w", encoding="utf-8") as file:
        file.write(save_obj)
        print(save_obj)
        print(f"{line_obj}\n{name} <完了>\n{line_obj}")


# 機能の集約
def get_save_obj():
    file_path, save_path = get_file_path()
    read_obj = read_file(file_path, "<ファイル読込>")
    list_obj = get_list_obj(read_obj)
    new_list = get_new_list(list_obj, "<改行 記号整形処理>")
    save_obj = get_new_obj(new_list)
    get_write(save_obj, save_path, "<ファイル出力処理>")


def main():
    get_save_obj()


# ========================================
# プログラム実行
main()

# ======================================
# コマンドサンプル-1
# ======================================
"""
python3 app_02.py sample
python3 app_02.py sample.txt output
"""
