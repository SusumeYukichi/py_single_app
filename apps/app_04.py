import webbrowser

# 区切線
line_obj = "=" * 30


# 記事の見出しを想定
head_list = (
    "2026",
    "公開",
    "Python3",
    "アプリ-Number",
)

# 本文を想定
tmp_content = {
    "<結論>": "[Python3]の[Github公開]を行いました.",
    "<目的>": "[効率化できた主な作業や機能名を記載する]の効率化・自動化の実現のため",
    "<内容>": "下記がアプリのリポジトリです.\nもし良ければ見ていただけると幸いです.",
    "<URL>": "[検証済のURLを記事に埋め込む]",
    "<今後>": "効率化や自動化に繋がるアプリが完了出来次第\n順次公開を続けていきます.",
}


# URLリスト
my_url = {
    "1": "https://github.com/SusumeYukichi/py_single_app",
}


# ハッシュタグを想定
tag_list = (
    "python3",
    "公開",
    "アプリ開発",
    "Github",
)


# 日付の入力
def get_input_obj():
    print("<投稿日の入力必須> 例:MMDD")
    day_obj = input()

    year_obj = head_list[0] + day_obj
    input_obj = "[" + year_obj + "]"

    return input_obj


# 記事等の見出し作成
def get_head_obj(input_obj):
    new_list = []
    for obj in head_list:
        obj = "[" + obj + "]"
        new_list.append(obj)
    head_obj = " ".join(new_list)

    # 検証作業
    assert head_obj[6] == " ", "見出し同士は半角空白が必須"

    # 記事見出し定義完了 [西暦] [記事見出しリスト]
    result = f"{input_obj} {head_obj}"

    return result


# テンプレートの本文取得 (辞書型)
def get_tmp_content():
    for k, v in tmp_content.items():
        print(f"{k}\n{v}")


# 該当URL起動確認
def get_my_url():
    webbrowser.open(my_url["1"], new=0, autoraise=True)
    print(f"<検証済のURL>:\n{my_url['1']}")


# #タグ形式として取得
def get_tag_list():
    for tag in tag_list:
        print(f"#{tag}")


# ==================================
# 投稿日時取得
day_obj = get_input_obj()
# 記事見出し取得
head_obj = get_head_obj(day_obj)
print(line_obj)
print("<見出し取得完了>")
print(head_obj)
print(line_obj)
# ==================================
# 該当URL起動確認
print(line_obj)
get_my_url()
print("<URL検証完了>")
print(line_obj)
# ==================================
# テンプレートの本文取得 (辞書型)
print(line_obj)
get_tmp_content()
print("<本文の取得完了>")
print(line_obj)
# ==================================
# #タグ取得
print(line_obj)
get_tag_list()
print("<#タグ取得完了>")
print(line_obj)
# ==================================
print(line_obj)
print("<記事見出し・本文・#タグ> 記事要素すべて取得完了>")
print(line_obj)
