import sys

# 区切線
line_obj = "=" * 30

# 分析用語リスト
analysis_list = [
    [
        "倍増",
        "増加",
        "微増",
    ],
    [
        "同値",
        "横ばい",
    ],
    [
        "減少",
        "急落",
    ],
]

# 記事関連用語リスト
item_list = [
    [
        "見出し・サムネイル・タグ設定",
    ],
    [
        "投稿日・投稿時間・投稿頻度増減",
    ],
    [
        "人気・急上昇の表示・非表示",
    ],
]

# <指標> <インプレッション> (投稿記事表示回数を想定)
imp = "<インプレッション>"
# <指標> <ページビュー> (投稿記事クリック数を想定)
pag = "<ページビュー>"


# 昨日値
y_d = ""
# 当日値
t_d = ""


# 指標値の入力
def get_input_obj():
    try:
        print("<当日値>を入力してください>\n小数点入力不可")
        t_d = input(">")
        if not t_d.isdecimal():
            raise ValueError("入力値は自然数でなければならない")

        print("<前日値>を入力してください>\n小数点入力不可")
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
        print(f"{index} <前日比> {result} 倍")
    # 例外処理 <ゼロ除算>
    except ZeroDivisionError as e:
        print(f"エラー:{e}")
        sys.exit("プログラムを終了します")


# 差分 (当日-前日)
def get_subtract(index, t_d, y_d):
    result = t_d - y_d

    if result >= 1:
        print("<差分増加>")
    elif result == 0:
        print("<差分同値>")
    elif result <= -1:
        print("<差分減少>")

    print(f"{index} <前日差> {abs(result)} 回")


def list_info(first_list, second_list):
    print(line_obj)
    print(f"<名称>:{first_list}")
    print(analysis_list)
    print(line_obj)
    print(f"<名称>:{second_list}")
    print(item_list)
    print(line_obj)


# 分析用語入力
def get_analysis(index):
    try:
        list_info("<分析用語リスト>", "<記事関連用語リスト")
        print("<分析開始> 当てはまる<分析用語>を選択してください")
        analysis_obj = str(input(">"))
        print("<分析開始> 当てはまる<主な要因>を記載してください")
        item_obj = str(input(">"))
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        sys.exit("プログラムを終了します")

    print(f"{index} <結果分析>\n{analysis_obj}と考えられる.")
    print(f"{index} <主な要因>\n{item_obj}が考えられる.")

    return analysis_obj, item_obj


def get_first_index():
    print(f"{imp} 実行開始")
    t_d, y_d = get_input_obj()
    get_ratio(imp, t_d, y_d)
    get_subtract(imp, t_d, y_d)


def get_second_index():
    print(f"{pag} 実行開始")
    t_d, y_d = get_input_obj()
    get_ratio(pag, t_d, y_d)
    get_subtract(pag, t_d, y_d)


def main():
    get_first_index()
    print(line_obj)
    get_analysis(imp)
    get_second_index()
    print(line_obj)
    get_analysis(pag)
    print("<すべて実行完了>")


# ========================================
# プログラム実行
main()
