import sys

import pyperclip

print("*" * 30)
print("<プログラム開始>")
print("*" * 30)

text = pyperclip.paste()

# コピー選択範囲把握(1文字~400文字以上)
if len(text) >= 400:
    print("選択範囲は<400文字>以上です")
elif len(text) >= 200:
    print("選択範囲は<200文字>以上です")
elif len(text) >= 100:
    print("選択範囲は<100文字>以上です")
elif len(text) >= 50:
    print("選択範囲は<50文字>以上です")
elif len(text) >= 20:
    print("選択範囲は<20文字>以上です")
# 未入力状態のターミナル画面を選択したケース
elif text == "":
    print("文字が正しく選択されていません.")
    print("プログラムを終了します.")
    sys.exit()
elif len(text) >= 1:
    print("選択範囲は<1文字>以上です")

# 0文字以上の文字選択検証
assert len(text) >= 0

print("*" * 30)
print(f"<選択完了>\n{text}")
print("*" * 30)


# リスト化
get_list = text.split("\n")
print(f"対象のリスト化完了:\n{get_list}")

print("*" * 30)
# 追加記号 (半角文字)
head_item = "･"
print(f"<記号>|{head_item}|<追加処理開始>")
print("*" * 30)

new_list = []
for i in range(len(get_list)):
    if not get_list[i].startswith("･"):
        print(f"{i + 1}行目:処理開始")
        lines = head_item + get_list[i]
        assert lines.startswith("･")
        new_list.append(lines)
    else:
        lines = get_list[i]
        new_list.append(lines)

my_text = "\n".join(new_list)

print("*" * 30)
print("<処理結果>")
print("<文字合計数>" + "\n" + "(" + str(len(my_text)) + ")")
print("*" * 30)
print("<貼付処理可能>")
print("*" * 30)
print(my_text)


pyperclip.copy(my_text)

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
