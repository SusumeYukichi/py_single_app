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


# 例外処理 コマンドライン引数
try:
    if sys.argv[1] != "sample.txt":
        raise IndexError("読込先の引数が正しくありません.")
    if sys.argv[2] != "output.txt":
        raise IndexError("出力先の引数が正しくありません.")
except IndexError as e:
    print(f"<実行コマンド>\nエラー:{e}")
    sys.exit("プログラムを終了します.")


# パス取得
def get_path_obj():
    file_path = Path(__file__)
    dir_path = file_path.parent
    file_path = dir_path / sys.argv[1]
    output_path = dir_path / sys.argv[2]
    return file_path, output_path


# ファイル読込
def read_file(file_path):
    try:
        with open(file_path, encoding="utf-8") as file:
            read_obj = file.read()
            print(f"{line_obj}\n<ファイル読込完了>\n{line_obj}")

    # 例外処理 読込ファイル検証
    except FileNotFoundError:
        print("読込ファイルが存在しません")
        sys.exit("プログラムを終了します.")

    return read_obj


# オブジェクトのlist型変換
def get_list_obj(read_obj):
    list_obj = read_obj.split("\n")
    return list_obj


# 記号追加処理
def get_new_list(list_obj):
    new_list = []
    for i in range(len(list_obj)):
        lines = list_obj[i].replace("：", ":\n").replace("。", ".")
        # 記号検証開始
        assert "。" not in lines
        assert "：" not in lines

        print(f"<行数:{i + 1}>\n<改行・整形処理> 実行")
        new_list.append(lines)
    print(f"{line_obj}\n<データ整形処理 すべて実行完了>\n{line_obj}")
    return new_list


# new_listのstr型変換
def get_new_obj(new_list):
    new_obj = "\n".join(new_list)
    return new_obj


# 機能の集約
def get_save_obj(file_path, output_path):
    read_obj = read_file(file_path)
    list_obj = get_list_obj(read_obj)
    new_list = get_new_list(list_obj)
    new_obj = get_new_obj(new_list)

    # アンパック代入
    save_obj, save_path = new_obj, output_path

    return save_obj, save_path


# ファイル出力
def get_write(save_obj, save_path):
    with open(save_path, "w", encoding="utf-8") as file:
        file.write(save_obj)
        print(f"{line_obj}\n<ファイル出力処理完了>\n{line_obj}")


def main():
    file_path, output_path = get_path_obj()
    save_obj, save_path = get_save_obj(file_path, output_path)
    get_write(save_obj, save_path)


# ========================================
# プログラム実行
main()
