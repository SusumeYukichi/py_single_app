import re

# 区切線
line_obj = "=" * 30

print(line_obj)
print("<プログラム開始>")
print(line_obj)


# テキスト取得・データ整形
def get_text_obj():
    text_obj = """･API：ソフトウェア同士が機能やデータをやり取りする仕組み。
･HTTP：Webブラウザとサーバー間で通信するためのプロトコル。
･HTTPS：HTTP通信をTLSによって暗号化する仕組み。
･DNS：ドメイン名をIPアドレスなどの情報に対応付ける仕組み。
･IPアドレス：ネットワーク上の機器を識別するためのアドレス。
･SQL：データベースのデータを検索・追加・更新・削除するための言語。
･DBMS：データベースを管理・操作するためのソフトウェア。
･Git：ソースコードなどの変更履歴を管理する分散型バージョン管理システム。
･Docker：アプリケーションをコンテナとして実行・管理するための技術。
･Flask：PythonでWebアプリケーションを構築するための軽量フレームワーク。"""

    print(line_obj)
    print(f"<データ整形開始>\n{text_obj}")
    print(line_obj)

    # データ整形(検索処理前)・削除 空白削除(先頭と末尾)
    search_obj = text_obj.replace("･", "").strip()

    print(line_obj)
    print(f"<データ整形完了>\n{search_obj}")
    print(line_obj)

    return search_obj


# IT用語検索
def get_match_obj(search_obj):

    # 正規表現
    pattern_obj = re.compile(
        r"""
        (\w+) # 1文字以上の数字，英文字，下線(アンダースコア)
        (.*) # (\n)以外の全ての文字列
        """,
        re.VERBOSE,
    )

    match_obj = pattern_obj.findall(search_obj)

    print(line_obj)
    print("<検索該当>" + " " + str(len(match_obj)) + " " + "件です.")
    print(line_obj)

    return match_obj


# データ整形(検索処理後)
def get_it_obj(match_obj):
    i = 0
    for key, name in match_obj:
        i = i + 1
        name = name.replace("：", "").replace("。", "")
        print(f"{i}.{key}\n{name}")
    print(line_obj)
    print("<加工処理完了>")
    print(line_obj)


def main():
    search_obj = get_text_obj()
    match_obj = get_match_obj(search_obj)
    get_it_obj(match_obj)


# プログラム実行
main()
