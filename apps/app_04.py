import sys
import webbrowser

# 区切線
line_obj = "=" * 30

# new_list
new_list = []

# ========================================
# 記事見出し取得に関するコード
# ========================================


# 投稿日の入力
def get_input_obj(sample):
    try:
        while True:
            print(f"投稿日を入力をしてください.\n{sample}")
            print("入力をキャンセルする場合はEnterを入力してください")
            input_obj = input(">")
            if input_obj == "":
                sys.exit("プログラムを終了します")

            if len(input_obj) != 4 or not input_obj.isdecimal():
                print("4桁の数値を入力してください.")
                continue
            else:
                print("入力成功!")
                break

    # 例外処理
    except KeyboardInterrupt:
        print("入力をやり直してください.")
        sys.exit("プログラムを終了します")

    return input_obj


# 投稿日の見出し取得
def get_first_head(input_obj, year):
    first_head = f"[{year}{input_obj}]"

    # 文字数検証　"[YYYYMMDD]"
    assert len(first_head) == 10

    # 記事の見出しリスト
    head_list = [
        "公開",
        "Python3",
        "アプリ-Number",
        "コード整理",
    ]

    return first_head, head_list


# new_list 取得
def get_new_list(first_head, head_list):
    if not new_list:
        new_list.append(first_head)
        for obj in head_list:
            obj = f"[{obj}]"
            new_list.append(obj)

    # 投稿日見出しの開始位置検証
    assert new_list[0] == first_head

    return new_list


# new_listのstr型変換
def get_new_obj(new_list):
    new_obj = " ".join(new_list)
    # 文字検証 [西暦8桁]　半角スペース
    assert new_obj[10] == " "
    # 次の見出しの開始位置検証
    assert new_obj[11] == "["

    return new_obj


# 記事見出し取得の関数集約
def get_head_obj(name):
    input_obj = get_input_obj("1月1日 例:0101")
    first_head, head_list = get_first_head(input_obj, "2026")
    new_list = get_new_list(first_head, head_list)
    head_obj = get_new_obj(new_list)
    print(f"{line_obj}\n{name}\n{head_obj}")


# ========================================
# 本文取得に関するコード
# ========================================

# 本文を想定
tmp_content = {
    "<結論>": "[Python3]の[Github公開]を行いました.",
    "<目的>": "[効率化できた主な作業や機能名を記載する]の効率化・自動化の実現のため.",
    "<内容>": "下記がアプリのリポジトリです.\nもし良ければ見ていただけると幸いです.",
    "<URL>": "[検証済のURLを記事に埋め込む]",
    "<今後>": "効率化や自動化に繋がるアプリが完了出来次第\n順次公開を続けていきます.",
}


# テンプレートの本文取得 (辞書型)
def get_tmp_content(name):
    print(f"{line_obj}\n{name}")
    for k, v in tmp_content.items():
        print(f"{k}:\n{v}")


# ========================================
# 該当URL起動確認に関するコード
# ========================================


# 該当URL起動確認
def get_my_url(name):
    my_url = {
        "1": "https://github.com/SusumeYukichi/py_single_app",
    }

    webbrowser.open(my_url["1"], new=0, autoraise=True)
    print(f"{line_obj}\n{name}\n{my_url['1']}\n{line_obj}")


# ========================================
# #タグ形式として取得に関するコード
# ========================================


# #タグ形式として取得
def get_tag_list(name):
    print(f"{name}")
    tag_list = [
        "python3",
        "プログラミング学習記録",
        "Github",
        "自動化ツール",
        "リファクタリング",
    ]

    for tag in tag_list:
        tag = f"#{tag}"
        print(tag)


# すべての関数を集約
def main():
    get_head_obj("<記事見出し>")
    get_tmp_content("<本文のテンプレート>")
    get_my_url("<起動確認済URL>")
    get_tag_list("<#タグ一覧>")
    print(f"{line_obj}\n<記事見出し・本文・URL・#タグ> すべて取得完了\n{line_obj}")


# ========================================
# プログラム実行
main()
