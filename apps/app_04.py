import sys
import webbrowser

# 区切線
line_obj = "=" * 30


# 記事の見出しを想定
head_list = (
    "公開",
    "Python3",
    "アプリ-Number",
)

# 本文を想定
tmp_content = {
    "<結論>": "[Python3]の[Github公開]を行いました.",
    "<目的>": "[効率化できた主な作業や機能名を記載する]の効率化・自動化の実現のため.",
    "<内容>": "下記がアプリのリポジトリです.\nもし良ければ見ていただけると幸いです.",
    "<URL>": "[検証済のURLを記事に埋め込む]",
    "<今後>": "効率化や自動化に繋がるアプリが完了出来次第\n順次公開を続けていきます.",
}


# URLリスト
my_url = {
    "1": "https://github.com/SusumeYukichi/py_single_app",
}


# ハッシュタグを想定
tag_list = [
    "python3",
    "公開",
    "アプリ開発",
    "Github",
]


# 投稿日の入力
def get_input_obj():
    try:
        while True:
            print("投稿日を入力をしてください. 例:MMDD")
            input_obj = input(">")
            if len(input_obj) != 4 or not input_obj.isdecimal():
                print("4桁の数値を入力してください.")
                continue
            else:
                print(f"{line_obj}\n投稿日の入力成功しました!")
                break
    # 例外処理
    except KeyboardInterrupt:
        print("入力をやり直してください.")
        sys.exit("プログラムを終了します")

    return input_obj


# 投稿日の見出し化
def get_first_head(input_obj, year):
    first_head = "[" + year + input_obj + "]"
    return first_head


# リストの見出し化
def get_second_head():
    new_list = []
    for obj in head_list:
        obj = "[" + obj + "]"
        new_list.append(obj)
    second_obj = " ".join(new_list)
    return second_obj


# 記事見出し取得の関数集約
def get_head_obj():
    input_obj = get_input_obj()
    first_head = get_first_head(input_obj, "2026")
    second_obj = get_second_head()
    head_obj = first_head + " " + second_obj

    # 文字検証 [西暦8桁]　半角スペース
    assert head_obj[0] == "["
    assert head_obj[9] == "]"
    assert head_obj[10] == " "

    # 次の見出しの開始位置検証
    assert head_obj[11] == "["

    return head_obj


# テンプレートの本文取得 (辞書型)
def get_tmp_content(name):
    print(f"{line_obj}\n{name}")
    for k, v in tmp_content.items():
        print(f"{k}:\n{v}")


# 該当URL起動確認
def get_my_url(name):
    print(f"{line_obj}\n{name}\n{my_url['1']}\n{line_obj}")
    webbrowser.open(my_url["1"], new=0, autoraise=True)


# #タグ形式として取得
def get_tag_list(name):
    print(f"{name}")
    for tag in tag_list:
        tag = "#" + tag
        print(tag)


def main():
    head_obj = get_head_obj()
    print(f"{line_obj}\n<記事見出し>\n{head_obj}")
    get_tmp_content("<本文>")
    get_my_url("<URL>")
    get_tag_list("<#タグ>")
    print(f"{line_obj}\n<記事見出し・本文・URL・#タグ> すべて取得完了\n{line_obj}")


# ========================================
# プログラム実行
main()
