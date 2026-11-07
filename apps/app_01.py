import pyperclip

print("*" * 30)
print("<プログラム開始>")
print("*" * 30)

text = pyperclip.paste()

# 追加記号 (半角文字)
head_item = "･"

get_list = text.split("\n")

print("*" * 30)
print("<選択完了>")
print(text)
print("*" * 30)

print("*" * 30)
print(f"<記号>|{head_item}|<追加処理開始>")
print("*" * 30)

new_list = []
for i in range(len(get_list)):
    if not get_list[i].startswith("･"):
        print(f"{i + 1}行目:処理開始")
        lines = head_item + get_list[i]
        new_list.append(lines)
    else:
        lines = get_list[i]
        new_list.append(lines)

print("*" * 30)
print("<すべての処理完了>")
print("*" * 30)

my_text = "\n".join(new_list)

pyperclip.copy(my_text)


print("*" * 30)
print("<処理結果> <貼付処理可能>")
print(my_text)
print("*" * 30)


# テキストサンプル
"""
テキスト選択
コピー
Python起動
貼付
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
