import sys

import pyperclip

# 区切線
line_obj = "=" * 30

print(line_obj)
print("<プログラム開始>")
print(line_obj)


# オブジェクト取得
def get_obj():
    p_obj = pyperclip.paste()

    try:
        if p_obj is None:
            raise Exception("テキストの選択が必要です")
    # 例外処理
    except Exception as e:
        print(f"テキストが未選択です.\nエラー:{e}")
        sys.exit("プログラムを終了します")

    print(f"{line_obj}\n<テキスト選択完了>\n{line_obj}")

    return p_obj


# オブジェクトの文字数検証
def get_count_obj(p_obj, first_text, second_text):

    if len(p_obj) >= 400:
        print(f"{line_obj}\n{first_text}\n400 {second_text}です.\n{line_obj}")
    elif len(p_obj) >= 200:
        print(f"{line_obj}\n{first_text}\n200 {second_text}です.\n{line_obj}")
    elif len(p_obj) >= 100:
        print(f"{line_obj}\n{first_text}\n100 {second_text}です.\n{line_obj}")
    elif len(p_obj) >= 50:
        print(f"{line_obj}\n{first_text}\n50 {second_text}です.\n{line_obj}")
    elif len(p_obj) >= 20:
        print(f"{line_obj}\n{first_text}\n20 {second_text}です.\n{line_obj}")
    elif len(p_obj) >= 10:
        print(f"{line_obj}\n{first_text}\n10 {second_text}です.\n{line_obj}")


# オブジェクトのlist型変換
def get_list_obj(p_obj):
    list_obj = p_obj.split("\n")
    return list_obj


# 記号追加処理
def get_new_list(list_obj):
    new_list = []
    head_item = "･"
    for i in range(len(list_obj)):
        if not list_obj[i].startswith("･"):
            lines = head_item + list_obj[i]
            print(f"<行数:{i + 1}> 追加")
            assert lines.startswith("･")
            new_list.append(lines)
        else:
            lines = list_obj[i]
            print(f"<行数{i + 1}> {head_item} 該当 追加処理スキップ")
            new_list.append(lines)

    print(f"{line_obj}\n<記号処理すべて実行完了>\n{line_obj}")
    return new_list


# new_listのstr型変換
def get_new_obj(new_list):
    new_obj = "\n".join(new_list)
    return new_obj


# 機能の集約
def get_save_obj():
    p_obj = get_obj()
    get_count_obj(p_obj, "<選択範囲>", "<字以上>")
    list_obj = get_list_obj(p_obj)
    new_list = get_new_list(list_obj)
    new_obj = get_new_obj(new_list)

    return new_obj


def main():
    save_obj = get_save_obj()
    pyperclip.copy(save_obj)
    print(f"{line_obj}\n<下記のテキスト貼付可能>\n{line_obj}")
    print(save_obj)


# ========================================
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
