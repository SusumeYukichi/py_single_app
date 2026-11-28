import re
import sys

# 区切線
line_obj = "=" * 30

print(line_obj)
print("<プログラム開始>")
print(line_obj)


# オブジェクト
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


# オブジェクトのlist型変換
def get_list_obj(name):
    print(f"{line_obj}\n{name} 取得開始\n{text_obj}\n{line_obj}")
    list_obj = text_obj.split("\n")
    return list_obj


# オブジェクト取得・データ整形
def get_new_list(name, list_obj):
    new_list = []
    for i, obj in enumerate(list_obj):
        lines = obj.replace("･", "").replace("：", ":").replace("。", ".")
        print(f"<行数:{i + 1}> {name} 完了")
        new_list.append(lines)
    return new_list


# new_listのstr型変換
def get_new_obj(new_list):
    new_obj = "\n".join(new_list)
    return new_obj


# オブジェクトの正規表現検索
def get_match_obj(name, search_obj):

    # 正規表現
    pattern_obj = re.compile(
        r"""
        (\w+:) # 1文字以上の文字
        (.*)  # 1文字以上の全ての文字
        """,
        re.VERBOSE,
    )

    match_obj = pattern_obj.findall(search_obj)

    if match_obj:
        print(f"{line_obj}\n{name} {len(match_obj)} 件\n{line_obj}")
    else:
        print(f"{line_obj}\n{name} 無し\n{line_obj}")
        sys.exit("プログラムを終了します")

    return match_obj


# 検索結果のIT用語化
def get_it_obj(name, match_obj):
    i = 0
    for key, obj in match_obj:
        key, obj = key.strip(":"), obj.strip(".")
        i = i + 1
        print(f"{i}.[{key}] [{obj}]")
    print(f"{line_obj}\n{name} {len(match_obj)} 件\nすべて完了\n{line_obj}")


# 機能の集約
def get_re_obj():
    list_obj = get_list_obj("<対象テキスト>")
    new_list = get_new_list("<記号整形処理>", list_obj)
    search_obj = get_new_obj(new_list)
    match_obj = get_match_obj("<検索該当>", search_obj)
    get_it_obj("<IT用語化>", match_obj)


def main():
    get_re_obj()


# ========================================
# プログラム実行
main()
