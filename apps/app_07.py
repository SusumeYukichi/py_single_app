import sys

# 区切線
line_obj = "=" * 30

# 分析用語リスト
analysis_list = [
    "倍増",
    "増加",
    "微増",
    "同値",
    "横ばい",
    "減少",
    "半減",
    "急落",
]

# 記事関連用語リスト
item_list = [
    "統一された見出し・サムネイル・#タグ設定",
    "投稿日・投稿時間・投稿頻度の見直し",
    "人気・急上昇などアルゴリズムの表示・非表示",
]

# <指標> <インプレッション> (投稿記事表示回数を想定)
imp = "<インプレッション>"
# <指標> <ページビュー> (投稿記事クリック数を想定)
pag = "<ページビュー>"


# 指標値の入力
def get_input_obj():
    try:
        print("<当日値>を入力してください>")
        t_d = input(">")
        if not t_d.isdecimal():
            raise ValueError("入力値は自然数でなければならない")

        print("<前日値>を入力してください>")
        y_d = input(">")
        if not y_d.isdecimal():
            raise ValueError("入力値は自然数でなければならない")

        # アンパック代入
        t_d, y_d = int(t_d), int(y_d)

    # 例外処理
    except KeyboardInterrupt as e:
        print(f"エラー:{e}")
        sys.exit("プログラムを終了します")

    except ValueError as e:
        print(f"エラー:{e}")
        sys.exit("プログラムを終了します")

    return t_d, y_d


# 前日比 (当日/前日)
def get_ratio(index, t_d, y_d):
    try:
        ratio_obj = t_d / y_d
        # 小数第2位まで表示
        result = round(ratio_obj, 2)
        print(f"{line_obj}\n{index} <前日比> {result} 倍")
    # 例外処理 <ゼロ除算>
    except ZeroDivisionError as e:
        print(f"エラー:{e}")
        sys.exit("プログラムを終了します")


# 差分 (当日-前日)
def get_subtract(index, t_d, y_d):
    result = t_d - y_d

    if result >= 1:
        print("<差分はプラス.>")
    elif result == 0:
        print("<差分は同値で変化なし>")
    elif result <= -1:
        print("<差分はマイナス>")

    print(f"{index} <前日差分値> {abs(result)} 回")


# インプレッション集計
def get_first_index():
    print(f"{line_obj}\n{imp} 実行開始\n{line_obj}")
    t_d, y_d = get_input_obj()
    get_ratio(imp, t_d, y_d)
    get_subtract(imp, t_d, y_d)


# ページビュー集計
def get_second_index():
    print(f"{line_obj}\n{pag} 実行開始\n{line_obj}")
    t_d, y_d = get_input_obj()
    get_ratio(pag, t_d, y_d)
    get_subtract(pag, t_d, y_d)


# 指標集計の関数集約
def get_index_obj():
    get_first_index()
    get_second_index()


# ========================================
# 分析用語入出力に関するコード
# ========================================


# 分析用語入力
def get_analysis(index):
    try:
        print(f"{line_obj}\n{index} <分析開始>")
        print("当てはまる<分析用語>を選択してください")
        analysis_obj = str(input(">"))

        print(f"{line_obj}\n{index} <主な要因分析開始>")
        print("当てはまる<主な要因>を自由に記載してください")
        item_obj = str(input(">"))

    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        sys.exit("プログラムを終了します")

    print(f"{line_obj}\n{index} <結果分析>\n{analysis_obj}と考えられる.")
    print(f"{line_obj}\n{index} <主な要因>\n{item_obj}が考えられる.")


# 分析用語入出力の関数集約
def get_index_analysis():
    get_analysis(imp)
    get_analysis(pag)


def main():
    print(f"{line_obj}\n<分析用語リスト>")
    print(analysis_list)
    print(f"{line_obj}\n<用語リスト>")
    print(item_list)
    get_index_obj()
    get_index_analysis()
    print(f"{line_obj}\n<すべて実行完了>\n{line_obj}")


# ========================================
# プログラム実行
main()
