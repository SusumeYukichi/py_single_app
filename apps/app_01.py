import sys

import pyperclip

# 区切線
line_obj = "=" * 30

print(line_obj)
print("<プログラム開始>")
print(line_obj)


# クリップボードの選択値保存
def get_paste_obj():
    p_obj = pyperclip.paste()

    if len(p_obj) == 0:
        print("テキストが未選択です.")
        sys.exit("プログラムを終了します.")
    else:
        print(line_obj)
        print("<テキストの選択完了>")
        print(line_obj)

    return p_obj


# 選択範囲把握
def get_count(p_obj):
    if len(p_obj) > 400:
        print(line_obj)
        print("選択範囲は<400文字>より大きい.")
        print(line_obj)
    elif len(p_obj) > 200:
        print(line_obj)
        print("選択範囲は<200文字>より大きい.")
        print(line_obj)
    elif len(p_obj) > 100:
        print(line_obj)
        print("選択範囲は<100文字>より大きい.")
        print(line_obj)
    elif len(p_obj) > 50:
        print(line_obj)
        print("選択範囲は<50文字>より大きい.")
        print(line_obj)
    elif len(p_obj) > 20:
        print(line_obj)
        print("選択範囲は<20文字>より大きい.")
        print(line_obj)
    elif len(p_obj) > 10:
        print(line_obj)
        print("選択範囲は<10文字>より大きい.")
        print(line_obj)


# クリップボードのリスト化
def get_list(p_obj):
    list_obj = p_obj.split("\n")
    return list_obj


# 記号追加処理
def get_new_list(list_obj):
    new_list = []
    head_item = "･"
    for i in range(len(list_obj)):
        if not list_obj[i].startswith("･"):
            lines = head_item + list_obj[i]
            print(f"{i + 1}行目")
            assert lines.startswith("･")
            new_list.append(lines)
        else:
            lines = list_obj[i]
            new_list.append(lines)

    print("<行頭追加処理完了>")
    return new_list


# リストの文字型処理
def get_text_obj(new_list):
    text_obj = "\n".join(new_list)
    print(line_obj)
    print("<文字合計数>" + "\n" + str(len(text_obj)))
    print(line_obj)

    return text_obj


def main():
    p_obj = get_paste_obj()
    get_count(p_obj)
    list_obj = get_list(p_obj)
    new_list = get_new_list(list_obj)
    text_obj = get_text_obj(new_list)
    pyperclip.copy(text_obj)
    print("<下記のテキスト貼付可能>")
    print(line_obj)
    print(text_obj)


# プログラム実行
main()

# ======================================
# テキストサンプル-1
# ======================================
"""
テキスト選択
コピー
Python起動
貼付
出力結果確認
"""
# ======================================
# テキストサンプル-2
# ======================================
"""
テキスト選択
･コピー
Python起動
･貼付
出力結果確認
"""
