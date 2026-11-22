import sys
from datetime import date
from pathlib import Path

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

# 出力先パス
file_obj = Path(__file__)
directory = file_obj.parent
output_path = directory / sys.argv[1]


# タスク一覧
task_list = [
    [
        "[タスクの優先順位設定]",
        "[アプリ製作のアイデア言語化]",
        "[要件定義]",
        "[動作検証]",
        "[Github 公開]",
        "[Note 外部発信]",
    ],
    [
        "[ローカル環境のフォルダ整理]",
        "[既存アプリのリファクタリング]",
        "[AIに関するニュースの検索]",
        "[Noteのアクセス状況分析]",
    ],
]

# Pythonのライブラリ一覧
py_lib = [
    [
        "[クリップボード操作:pyperclip]",
        "[検索・置換:re]",
    ],
    [
        "[フォルダ操作:pathlib]",
        "[フォルダ操作:os]",
        "[コマンド操作:sys]",
    ],
    [
        "[Excelファイル操作:openpyxl]",
        "[PDF管理:pypdf]",
    ],
    [
        "[URL操作:webbrowser]",
        "[データベース操作:sqlite3]",
        "[日時取得:datetime]",
    ],
]


# タスク全体の参照情報
def task_info():
    print("<共通タスク一覧>")
    print(task_list[0])
    print(line_obj)
    print("<追加のタスク候補>")
    print(task_list[-1])
    print("<Pythonライブラリ>")
    print(py_lib[0])
    print(py_lib[1])
    print(py_lib[-1])
    print("ライブラリ取得完了")


# 追加タスク入力時参照例
def input_info():
    print(line_obj)
    print("<追加タスク>があれば5行入力してください")
    print("入力例-1:情報整理効率化の実施")
    print("入力例-2:フォルダ操作:osの検証")
    print("入力例-3:アプリのコードリファクタリング.")
    print("入力例-4:ローカル環境のフォルダ整理.")
    print("入力例-5:Noteの投稿記事表記揺れチェック.")
    print(line_obj)
    print("<追加タスク>が無ければEnterを押してください")


# タスク設定日と共通タスク取得
def get_today_task(task_list):
    today = "作成日:" + str(date.today())
    task_join_obj = "\n".join(task_list[0])
    print("日次の共通タスク取得完了")
    return today, task_join_obj


# タスク追加入力
def get_add_task():
    input_info()
    try:
        add_01 = input(">")
        print("<1行目入力完了>")
        add_02 = input(">")
        print("<2行目入力完了>")
        add_03 = input(">")
        print("<3行目入力完了>")
        add_04 = input(">")
        print("<4行目入力完了>")
        add_05 = input(">")
        print("<5行目入力完了>")
        add_task = (
            add_01 + "\n" + add_02 + "\n" + add_03 + "\n" + add_04 + "\n" + add_05
        )

    except KeyboardInterrupt:
        print("入力をやり直してください")
        sys.exit("プログラムを終了します")

    return add_task


# 日次タスク取得 (日付＋共通タスク＋追加分)
def task_create(today, task_join_obj, add_task):
    save_obj = today + "\n" + task_join_obj + "\n" + add_task
    return save_obj


# ファイル出力
def save_file(save_obj, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(save_obj)
        print(line_obj)
        print("ファイル出力完了")
        print(line_obj)


def main():
    task_info()
    today, task_join_obj = get_today_task(task_list)
    add_task = get_add_task()
    print("<追加タスク入力完了>")
    save_obj = task_create(today, task_join_obj, add_task)
    save_file(save_obj, output_path)


# ========================================
# プログラム実行
main()
