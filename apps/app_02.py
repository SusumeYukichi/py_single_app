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


# コマンドライン引数
def get_file_path():
    try:
        file_path = directory / sys.argv[1]
        assert sys.argv[1] == "sample.txt", "引数-2と異なります"
        output_path = directory / sys.argv[2]
        assert sys.argv[2] == "output.txt", "引数-3と異なります"

    # 例外処理
    except IndexError:
        print("コマンドライン引数が未設定です")
        sys.exit("プログラムを終了します.")

    return file_path, output_path


# ファイル読込
def read_file(file_path):
    try:
        with open(file_path, encoding="utf-8") as file:
            read_obj = file.read()
            print(line_obj)
            print("ファイル読込完了")
            print(line_obj)

    # 例外処理 読込ファイル検証
    except FileNotFoundError:
        print("読込ファイルが存在しません")
        sys.exit("プログラムを終了します.")

    return read_obj


# 読込ファイル加工処理
def get_save_obj(read_obj):
    list_obj = read_obj.split("\n")
    new_list = []
    for obj in list_obj:
        obj = obj.replace("：", ":\n").replace("。", ".")
        new_list.append(f"{obj}")

    save_obj = "\n".join(new_list)

    # 記号検証開始
    assert "。" not in save_obj
    assert "：" not in save_obj

    # 文字型検証
    assert type(save_obj) == str, "文字型ではありません.!"

    print(line_obj)
    print("<ファイル加工処理完了>")
    print(line_obj)

    return save_obj


# ファイル出力
def get_write(save_obj, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(save_obj)
        print(line_obj)
        print("<ファイル出力処理完了>")
        print(line_obj)


def main():
    file_path, output_path = get_file_path()
    read_obj = read_file(file_path)
    save_obj = get_save_obj(read_obj)
    get_write(save_obj, output_path)


# プログラム実行
main()
