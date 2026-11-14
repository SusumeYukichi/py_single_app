import sys
from datetime import date
from pathlib import Path

"""
<パス移動>:
cd apps
<実行コマンド>:
python3 app_06.py day_task.txt
"""


print("*" * 30)
print("<プログラム開始>")
print("実行ファイル:" + str(sys.argv[0]))
print("保存ファイルパス指定:" + str(sys.argv[1]))
print("*" * 30)

# 出力先パス
file_obj = Path(__file__)
directory = file_obj.parent
output_path = directory / sys.argv[1]

# 共通タスク
task_list = [
    "[タスクの優先順位設定]",
    "[アプリ製作のアイデア言語化]",
    "[要件定義]",
    "[動作検証]",
    "[Github 公開]",
    "[Note 外部発信]",
]

# 件数カウント
print("共通タスク:" + str(len(task_list)) + "件")

# 追加のタスク候補
sub_task_list = [
    "[ローカル環境のフォルダ整理]",
    "[既存アプリのリファクタリング]",
    "[AIに関するニュースの検索]",
    "[Noteのアクセス状況分析]",
]

# テキスト操作
text_lib = (
    "[クリップボード操作:pyperclip]",
    "[検索・置換:re]",
)

# コマンド・ファイル操作
cmd_lib = (
    "[フォルダ操作:pathlib]",
    "[フォルダ操作:os]",
    "[コマンド操作:sys]",
)

# 業務ファイル操作
file_lib = (
    "[Excelファイル操作:openpyxl]",
    "[PDF管理:pypdf]",
)

# その他のライブラリ
other_lib = (
    "[URL操作:webbrowser]",
    "[データベース操作:sqlite3]",
    "[日時取得:datetime]",
)


# タスク追加時の参照情報
def input_info():
    print(f"追加のタスク候補:\n{sub_task_list}")
    print(f"Pythonのライブラリ:\n{text_lib}\n{cmd_lib}\n{file_lib}\n{other_lib}")


# タスク追加
def get_add_task():
    input_info()
    print("*" * 30)
    print("<追加タスク>があれば5行入力してください")
    print("入力例-1:情報整理効率化の実施")
    print("入力例-2:フォルダ操作:osの検証")
    print("入力例-3:アプリのコードリファクタリング.")
    print("入力例-4:ローカル環境のフォルダ整理.")
    print("入力例-5:Noteの投稿記事表記揺れチェック.")
    print("*" * 30)
    print("<追加タスク>が無ければEnterを押してください")
    try:
        add_01 = input()
        print("<1行目入力完了>")
        add_02 = input()
        print("<2行目入力完了>")
        add_03 = input()
        print("<3行目入力完了>")
        add_04 = input()
        print("<4行目入力完了>")
        add_05 = input()
        print("<5行目入力完了>")
        add_task = (
            add_01 + "\n" + add_02 + "\n" + add_03 + "\n" + add_04 + "\n" + add_05
        )

        return add_task
    except KeyboardInterrupt:
        print("入力をやり直してください")
        print("プログラムを終了します")
        sys.exit()


# 共通タスク取得
def get_task(task_list):
    get_my_task = "\n".join(task_list)
    return get_my_task


# タスク設定日取得
def get_date_info():
    today = "作成日:" + str(date.today())
    return today


# 日次タスク設定 (日付＋共通タスク＋追加分)
def task_create():
    today = get_date_info()
    get_my_task = get_task(task_list)
    add_task = get_add_task()
    today_task = (
        today
        + "\n"
        + "<共通タスク>"
        + "\n"
        + get_my_task
        + "\n"
        + "<追加タスク>"
        + "\n"
        + add_task
    )
    print(today_task)
    return today_task


# ファイル出力
def save_file(day_task):
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(day_task)


print("*" * 30)
day_task = task_create()
print("<タスク設定完了>")
print("*" * 30)

print("*" * 30)
save_file(day_task)
print("ファイル出力完了")
print("*" * 30)
