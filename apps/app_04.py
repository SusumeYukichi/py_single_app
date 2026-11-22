import sys
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


# 投稿日の入力
def get_input_obj():
    input_obj = ""
    try:
        while len(input_obj) != 4:
            print("投稿日の入力値は4桁.<入力必須> 例:MMDD")
            input_obj = input(">")
    except KeyboardInterrupt:
        print("入力をやり直してください")
        sys.exit("プログラムを終了します")

    print("投稿日の入力成功しました!")
    return input_obj


# 投稿日の見出し化
def get_day_obj(input_obj):
    day_obj = input_obj

    year_obj = head_list[0] + day_obj
    first_head = "[" + year_obj + "]"

    return first_head


# 見出しの文字結合
def get_head_join(first_head):
    new_list = []
    for obj in head_list:
        obj = "[" + obj + "]"
        new_list.append(obj)
    other_obj = " ".join(new_list)

    # 検証作業
    assert other_obj[6] == " ", "見出し同士は半角空白が必須"

    # 記事見出し定義完了 [西暦] [記事見出しリスト]
    head_obj = f"{first_head} {other_obj}"

    return head_obj


# 記事の見出し処理完成
def get_head_obj():
    input_obj = get_input_obj()
    first_head = get_day_obj(input_obj)
    join_obj = get_head_join(first_head)
    print("<見出し取得完了>")
    print(join_obj)


# テンプレートの本文取得 (辞書型)
def get_tmp_content():
    for k, v in tmp_content.items():
        print(f"{k}\n{v}")
    print("<本文の取得完了>")


# 該当URL起動確認
def get_my_url():
    webbrowser.open(my_url["1"], new=0, autoraise=True)
    print(f"<検証済のURL>:\n{my_url['1']}")
    print("<URL検証完了>")


# #タグ形式として取得
def get_tag_list():
    for tag in tag_list:
        print(f"#{tag}")
    print("<#タグ取得完了>")


def main():
    get_head_obj()
    get_tmp_content()
    get_my_url()
    get_tag_list()
    print(line_obj)
    print("<記事見出し・本文・URL・#タグ> <記事要素すべて取得完了>")
    print(line_obj)


# プログラム実行
main()
