import sys
from datetime import date
from pathlib import Path
from pprint import pprint

"""
<実行コマンド>
python3 app_06.py day_task.txt
<詳細>
<実行プログラム>:app_06.py
<出力ファイル名指定>:day_task.txt
"""

# 区切線
line_obj = "=" * 30


print(line_obj)
print("<プログラム開始>")
print(line_obj)


# タスク一覧
task_list = [
    "アプリ製作:アイデア言語化・要件定義・コーディング・動作検証",
    "公開作業:Github・Note・Youtube",
    "コード整理:関数化・データ構造化",
    "分析作業:Noteのダッシュボード確認・前日比・差分集計",
]


# Pythonライブラリ一覧
lib_list = [
    "クリップボード:pyperclip",
    "検索・置換:re",
    "フォルダ:pathlib・os",
    "コマンド:sys",
    "Excel:openpyxl",
    "PDF:pypdf",
    "URL:webbrowser",
    "データベース:sqlite3",
    "日時:datetime",
]

# 例外処理 コマンドライン引数
try:
    if sys.argv[1] != "day_task.txt":
        raise IndexError("出力先の引数が正しくありません.")
except IndexError as e:
    print(f"<実行コマンド>\nエラー:{e}")
    sys.exit("プログラムを終了します.")


# 出力先パス取得
def get_path_obj():
    file_obj = Path(__file__)
    directory = file_obj.parent
    output_path = directory / sys.argv[1]

    return output_path


# 共通タスク　保存オブジェクト取得
def save_common_list():
    new_list = []
    i = 0
    for i in range(len(task_list)):
        lines = task_list[i]
        new_list.append(lines)
        save_obj = "\n".join(new_list)
    save_path = get_path_obj()
    return save_obj, save_path


# 共通タスク保存 (上書きモード)
def write_common_task(save_obj, today_obj, save_path):
    with open(save_path, "w", encoding="utf-8") as file:
        file.write("設定日:" + today_obj + "\n")
        file.write("共通タスク一覧:" + "\n" + save_obj + "\n")


# 共通タスク取得　関数集約
def get_common_task():
    save_obj, save_path = save_common_list()
    today_obj = str(date.today())
    write_common_task(save_obj, today_obj, save_path)
    print(f"{line_obj}\n<ファイル出力処理完了>\n{line_obj}")


# ========================================
# タスク追加に関するコード
# ========================================


# タスク追加のオブジェクト取得
def get_create_list():
    create_list = []
    print("共通タスク一覧")
    pprint(task_list)
    print("Pythonのライブラリ一覧")
    pprint(lib_list)
    print("<新しいタスクが有れば5行追加可能です>")
    try:
        for num in range(1, 6):
            add_task = str(num) + "件目:" + input(">")
            print(f"{num} 件目 入力完了")
            create_list.append(add_task)

    except KeyboardInterrupt:
        print("入力をやり直してください")
        sys.exit("プログラムを終了します")

    print("<追加タスク> <すべて入力完了>")
    return create_list


# create_listのstr型変換
def save_create_list(create_list):
    new_obj = "\n".join(create_list)
    save_obj = new_obj
    return save_obj


# 新規タスク保存 (共通タスクに追記する処理)
def write_create_task(save_obj, save_path):
    with open(save_path, "a", encoding="utf-8") as file:
        file.write(line_obj + "\n" + "追加タスク:" + "\n" + save_obj)
        print(f"{line_obj}\n<ファイル追記処理完了>\n{line_obj}")


# 新規タスク追加処理　関数集約
def get_create_task():
    create_list = get_create_list()
    save_obj = save_create_list(create_list)
    save_path = get_path_obj()
    write_create_task(save_obj, save_path)


def main():
    get_common_task()
    get_create_task()


# ========================================
# プログラム実行
main()

# ======================================
# テキストサンプル-1
# ======================================
"""
ローカル環境のフォルダ整理.
新規のライブラリについて情報整理.
Noteの投稿記事表記揺れチェック.
AIのプロンプト情報整理.
技術書の再読.
"""
