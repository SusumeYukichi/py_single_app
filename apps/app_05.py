import sqlite3
import sys
from pathlib import Path

# コマンドライン引数:
# python3 app_05.py db.sqlite db.txt

dir_path = Path(__file__).parent
db_path = dir_path / sys.argv[1]
output_path = dir_path / sys.argv[2]


# Connection_obj
conn = sqlite3.connect(
    db_path,
    isolation_level=None,
)

# テーブル定義
create_table_sql = """
    CREATE TABLE IF NOT EXISTS my_words
    (name TEXT NOT NULL UNIQUE)
    STRICT;
"""

# テーブル生成
conn.execute(create_table_sql)

print("<1>:データベース接続開始")

print("<2>:用語追加開始")


# ハッシュタグとして用語登録
try:
    print("*" * 30)
    conn.execute('INSERT INTO my_words VALUES ("#python3")')
    conn.execute('INSERT INTO my_words VALUES ("#公開")')
    conn.execute('INSERT INTO my_words VALUES ("#アプリ開発")')
    conn.execute('INSERT INTO my_words VALUES ("#Github")')
    print("<3>:用語登録完了")
    print("*" * 30)

except sqlite3.IntegrityError:
    print("*" * 30)
    print("<3>:既に用語は登録済です.")
    print("*" * 30)

# 用語の検索
my_words = """
    SELECT name FROM my_words;
"""
result = conn.execute(my_words).fetchall()

new_list = []
i = 0
if result:
    for my_data in result:
        i = i + 1
        new_list.append(my_data[0])
        print(f"No{i}.:検索完了")
else:
    print("データベースに用語が登録されていません.")


print("*" * 30)
print(f"取得結果:\n{new_list}")
print("*" * 30)

print("<4>:テキスト改行処理開始")

get_my_words = "\n".join(new_list)
print(f"<処理結果>\n{get_my_words}")

print("保存開始したい場合は1,キャンセルしたい場合は0")
task = int(input())
if task == 1:
    with open(output_path, "w", encoding="utf-8") as file:
        print("<保存開始>")
        file.write(get_my_words)
        print("<5>:ファイル保存完了")
elif task == 0:
    print("<5>:入力キャンセル")
else:
    print("入力番号を再入力してください")


print("<6>:接続終了")
conn.close()

print("<7>:プログラム終了")
sys.exit()
