import webbrowser

print("<投稿日の入力必須> 例:MMDD")
input_day = input()
head_day = "2026" + input_day

head_list = (
    head_day,
    "[公開]",
    "[Python3]",
    "[アプリ-4]",
)

head_result = " ".join(head_list)

print("*" * 30)
print("<記事タイトル取得完了>")
print(head_result)
print("*" * 30)

# 半角空白文字検証
assert head_result[8] == " "
assert head_result[-1] == "]"


temp_text = """
【Github公開】を行いました.
目的:アプリ製作進捗の外部発信効率化のため
下記がアプリのリポジトリです.
該当URL:
もし良ければ見ていただけると幸いです.
今後:
効率化や自動化に繋がるアプリが完了出来次第,順次公開を続けていきます.
"""

print("<本文>")
print(temp_text)


my_url = {
    "1": "https://github.com/SusumeYukichi/py_single_app",
}

print(f"<URL>:\n{my_url['1']}")

# 該当URL起動確認
webbrowser.open(my_url["1"], new=0, autoraise=True)

print("*" * 30)
print("<URL検証完了>")


my_tag = (
    "#python3",
    "#公開",
    "#アプリ開発",
    "#Github",
)


print("*" * 30)
print("<投稿時の設定情報取得>")
print("*" * 30)

print("<#タグ取得開始>")
print("*" * 30)

i = 0
for one_tag in my_tag:
    i = i + 1
    print(f"{one_tag}")

print("*" * 30)
print("<#タグ取得完了>")
print("*" * 30)


print("""
ログ出力後,文体チェックや追記等の調整実行
ログ出力コマンド:python3 app_04.py > output.log
コマンド実施時に投稿日の入力必要 例:MMDD
""")
