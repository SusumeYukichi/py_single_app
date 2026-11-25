import sqlite3
import sys
from pathlib import Path

"""
<実行コマンド>
python3 app_05.py db.sqlite db.txt
<詳細>
引数-2:データベース読込先
引数-3:出力先
"""


# 区切線
line_obj = "=" * 30

# ファイルパス定義
dir_path = Path(__file__).parent
db_path = dir_path / sys.argv[1]
output_path = dir_path / sys.argv[2]


# Connection_objの取得
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

# 列検索(#タグ)
tag_obj = """
    SELECT name FROM my_words;
"""


# テーブル生成
def db_create():
    conn.execute(create_table_sql)


# ハッシュタグとして用語登録
def db_insert():
    try:
        conn.execute('INSERT INTO my_words VALUES ("#python3")')
        conn.execute('INSERT INTO my_words VALUES ("#公開")')
        conn.execute('INSERT INTO my_words VALUES ("#アプリ開発")')
        conn.execute('INSERT INTO my_words VALUES ("#Github")')
    except sqlite3.IntegrityError:
        print(line_obj)
        print("<3>:既に用語は登録済です.")
        print(line_obj)


# 用語検索開始
def db_search():
    search_obj = conn.execute(tag_obj).fetchall()
    return search_obj


# 検索用語リスト格納と改行処理
def get_list_obj(search_obj):
    new_list = []
    i = 0
    if search_obj:
        for data_obj in search_obj:
            i = i + 1
            new_list.append(data_obj[0])
            print(f"No{i}.:検索完了")
            list_obj = "\n".join(new_list)
    else:
        print("データベースに用語が登録されていません.")

    return list_obj


# データベース操作
def get_db_obj():
    db_create()
    print("<1>:データベース接続完了")
    db_insert()
    print("<2>:用語登録完了")
    search_obj = db_search()
    print("<3>:用語検索完了")
    return search_obj


# 改行処理結果取得
def get_save_obj(search_obj):
    save_obj = get_list_obj(search_obj)
    print("<4>:用語改行処理完了")
    return save_obj


# 数値入力
def get_user_task(save_obj):
    print("保存開始したい場合は1,キャンセルしたい場合は0")
    task = int(input(">"))
    get_write(task, save_obj)


# 保存処理の選択
def get_write(task, save_obj):
    if task == 1:
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(save_obj)
            print("<5>:ファイル保存完了")
    elif task == 0:
        print("<5>:入力キャンセル")
    else:
        print("入力番号を再入力してください")


# 全機能の関数化
def main():
    search_obj = get_db_obj()
    save_obj = get_save_obj(search_obj)
    get_user_task(save_obj)
    conn.close()
    print("<6>:データベース接続終了")
    sys.exit("<7>:プログラム終了")


# ========================================
# プログラム実行
main()

# ========================================
# データベース実装目的
"""
1.ブラウザや動画サイトから正確な検索結果を得たい.
2.用語を参照しながら文脈に合った正確な文章を書きたい.
3.関心のある書籍・解説動画の用語も整理したい.
"""
