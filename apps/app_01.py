import sys

import pyperclip

print("*" * 30)
print("<プログラム開始>")
print("*" * 30)


# テキストの選択
def get_paste_obj():
    p_obj = pyperclip.paste()
    print(f"<選択完了>\n{p_obj}")
    print("*" * 30)
    return p_obj


# 選択範囲把握(1文字~400文字以上)
def paste_check(p_obj):
    if len(p_obj) >= 400:
        print("選択範囲は<400文字>以上です")
    elif len(p_obj) >= 200:
        print("選択範囲は<200文字>以上です")
    elif len(p_obj) >= 100:
        print("選択範囲は<100文字>以上です")
    elif len(p_obj) >= 50:
        print("選択範囲は<50文字>以上です")
    elif len(p_obj) >= 20:
        print("選択範囲は<20文字>以上です")
    # 未入力状態のターミナル画面を選択したケース
    elif p_obj == "":
        print("文字が正しく選択されていません.")
        print("プログラムを終了します.")
        sys.exit()
    elif len(p_obj) >= 1:
        print("選択範囲は<1文字>以上です")
    # 0文字以上の文字選択検証
    assert len(p_obj) >= 0
    print("選択範囲検証完了")
    print("*" * 30)
    return p_obj


# リスト化
def get_list_obj(return_obj):
    list_obj = return_obj.split("\n")
    print(f"対象のリスト化完了:\n{list_obj}")
    print("*" * 30)
    return list_obj


# 記号追加処理
def add_item(list_obj):
    new_list = []
    # 追加記号 (半角文字)
    head_item = "･"
    for i in range(len(list_obj)):
        if not list_obj[i].startswith("･"):
            print(f"<記号>|{head_item}|<追加処理開始>")
            print(f"{i + 1}行目:処理開始")
            lines = head_item + list_obj[i]
            assert lines.startswith("･")
            new_list.append(lines)
        else:
            lines = list_obj[i]
            new_list.append(lines)
    text_obj = "\n".join(new_list)
    print("*" * 30)
    print("<記号処理完了>")
    return text_obj


# 文字数・処理結果取得
def get_result(text_obj):
    print("*" * 30)
    print("<文字合計数>" + "\n" + "(" + str(len(text_obj)) + ")")
    print("*" * 30)
    print("<処理結果取得完了>")
    print("<<<クリップボード貼付可能>>>")
    print("*" * 30)
    print(text_obj)
    return text_obj


def main():
    p_obj = get_paste_obj()
    return_obj = paste_check(p_obj)
    list_obj = get_list_obj(return_obj)
    text_obj = add_item(list_obj)
    result = get_result(text_obj)
    pyperclip.copy(result)


# プログラム実行
try:
    print("テキスト選択済の場合は<1>を入力してください")
    number = input()
    if number == "1":
        main()
    elif number != "1":
        print("数字が正しく選択されていません.")
        print("プログラムを終了します.")
        sys.exit()
except KeyboardInterrupt:
    print("入力操作がキャンセルされました.")
    print("プログラムを終了します.")
    sys.exit()


# テキストサンプル-1
"""
テキスト選択
コピー
Python起動
貼付
出力結果確認
"""

# テキストサンプル-2
"""
テキスト選択
･コピー
Python起動
･貼付
出力結果確認
"""

# 処理結果 (記号追加済)
"""
･テキスト選択
･コピー
･Python起動
･貼付
･出力結果確認
"""
