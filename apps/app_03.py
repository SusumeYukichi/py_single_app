import re
import sys

# 区切線
line_obj = "=" * 30

# 正規表現の検索テキスト
text_obj = """
･API：ソフトウェア同士が機能やデータをやり取りする仕組み。
･HTTP：Webブラウザとサーバー間で通信するためのプロトコル。
･HTTPS：HTTP通信をTLSによって暗号化する仕組み。
･DNS：ドメイン名をIPアドレスなどの情報に対応付ける仕組み。
･IPアドレス：ネットワーク上の機器を識別するためのアドレス。
･SQL：データベースのデータを検索・追加・更新・削除するための言語。
･DBMS：データベースを管理・操作するためのソフトウェア。
･Git：ソースコードなどの変更履歴を管理する分散型バージョン管理システム。
･Docker：アプリケーションをコンテナとして実行・管理するための技術。
･Flask：PythonでWebアプリケーションを構築するための軽量フレームワーク。
"""

# データ整形
search_obj = text_obj.replace("･", "").strip()

# 正規表現
pattern_obj = re.compile(
    r"""
    (\w+) # 1文字以上の数字，英文字，下線(アンダースコア)
    (.*) # (\n)以外の全ての文字列
    """,
    re.VERBOSE,
)

# タプル型の検索結果取得
match_obj = pattern_obj.findall(search_obj)

# 検索結果表示
if match_obj:
    print(line_obj)
    print("<検索結果>" + str(len(match_obj)) + "件です.")
    print("<加工処理開始>")
    print(line_obj)
else:
    print("<該当なし>")
    print("<プログラム終了>")
    sys.exit()

i = 0
for key, name in match_obj:
    i = i + 1
    # データ整形
    name = name.replace("：", "")
    print(f"{i}.\n<用語>:{key}\n<意味>:{name}")

print(line_obj)
print("<加工処理完了>")
print(line_obj)
