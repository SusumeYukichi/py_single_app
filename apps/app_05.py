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


# ========================================
# データベース操作に関するコード
# ========================================

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


# テーブル生成
def db_create(name):
    conn.execute(create_table_sql)
    print(f"{line_obj}\n{name}\n{line_obj}")


# 用語登録
def db_insert(name):
    try:
        conn.execute('INSERT INTO my_words VALUES ("python3")')
        conn.execute('INSERT INTO my_words VALUES ("公開")')
        conn.execute('INSERT INTO my_words VALUES ("アプリ開発")')
        conn.execute('INSERT INTO my_words VALUES ("Github")')
    except sqlite3.IntegrityError:
        print(f"{line_obj}\n既に用語は登録済です.\n{line_obj}")

    print(f"{line_obj}\n{name}\n{line_obj}")


# 用語検索開始
def db_search(name):
    my_obj = """
        SELECT name FROM my_words;
    """
    search_obj = conn.execute(my_obj).fetchall()
    print(f"{line_obj}\n{name}\n{line_obj}")

    return search_obj


# データベース操作
def get_db_obj():
    db_create("<1>:データベース接続完了")
    db_insert("<2>:用語登録完了")
    search_obj = db_search("<3>:用語検索完了")
    return search_obj


# ========================================
# 検索用語リスト格納と改行処理に関するコード
# ========================================


# 検索用語のnew_list 格納
def get_new_list(name):
    new_list = []
    print(f"{line_obj}\n{name}\n{line_obj}")
    search_obj = get_db_obj()
    for obj in search_obj:
        new_list.append(obj[0])
        print(f"{obj} 用語取得完了")

    return new_list


# ========================================
# 保存処理に関するコード
# ========================================


# 保存処理の選択 数値入力
def get_write(save_obj, name):
    print("保存開始したい場合は1を入力してください")
    task = input(">")
    if task == "1":
        with open(output_path, "w", encoding="utf-8") as file:
            file.write(save_obj)
            print(f"{line_obj}\n{name}\n{line_obj}")

    else:
        print("保存処理がキャンセルされました.")
        conn.close()


# 全機能の関数化
def main():
    new_list = get_new_list("<4>:用語取得処理開始")
    save_obj = "\n".join(new_list)
    get_write(save_obj, "<5>:ファイル保存完了")
    conn.close()
    print(f"{line_obj}\n<6>:データベース接続終了\n{line_obj}")
    sys.exit("プログラム終了")


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
