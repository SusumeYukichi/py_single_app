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


# 指標値の入力
def get_index(index):
    print("小数点入力不可")
    try:
        print(index + " " + "<当日の値を入力してください>")
        t_d = input()
        print(index + " " + "<前日分の値を入力してください>")
        y_d = input()
        # アンパック代入
        t_d, y_d = int(t_d), int(y_d)

    # 例外処理
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()

    return t_d, y_d


# 前日比 (当日/前日)
def get_ratio(index, t_d, y_d):
    print(line_obj)
    print(index + " " + "前日比計算開始")
    try:
        ratio_obj = t_d / y_d
        # 小数第2位まで表示
        result = round(ratio_obj, 2)
    # 例外処理 <ゼロ除算>
    except ZeroDivisionError:
        print("<エラー!><ゼロ除算>")
        print("プログラムを終了します")
        sys.exit()

    return result


# 差分 (当日-前日)
def get_subtract(index, t_d, y_d):
    print(line_obj)
    print(index + " " + "差分値計算開始")
    subtract_obj = t_d - y_d

    if subtract_obj > 1:
        print(line_obj)
        print("差分は前日よりプラスでした.")
        print(line_obj)

    elif subtract_obj == 0:
        print(line_obj)
        print("差分は前日と同値でした.")
        print(line_obj)

    elif subtract_obj < 1:
        print(line_obj)
        print("差分は前日よりもマイナスでした.")
        print(line_obj)

    # 絶対値変換
    result = abs(subtract_obj)

    return result


# 計算の一括処理
def get_metric(index):
    t_d, y_d = get_index(index)
    ratio_obj = get_ratio(index, t_d, y_d)
    subtract_obj = get_subtract(index, t_d, y_d)
    return ratio_obj, subtract_obj


# 計算結果表示
def day_metric(index, ratio_obj, subtract_obj):
    print(line_obj)
    print(index + " " + "<前日比>")
    print(str(ratio_obj) + " " + "倍")
    print(index + " " + "<差分値>")
    print(str(subtract_obj))
    print(line_obj)


# 用語リスト取得
def get_list():
    print("<分析用語リスト>")
    print(line_obj)
    print(analysis_list)
    print(line_obj)


# 分析用語入力
def get_analysis():
    get_list()
    try:
        print("<分析用語>を入力してください")
        analysis_obj = str(input())
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()

    return analysis_obj


# 分析結果
def day_analysis(index):
    print("<計算結果分析開始>")
    print(line_obj)
    print(index)
    result = get_analysis()
    print("<結果分析>" + "\n" + result + "と考えられる.")
    print(line_obj)


# 全体の要因分析
def second_analysis():
    try:
        print(line_obj)
        print("記事関連用語リスト")
        print(item_list)
        print(line_obj)
        print("<主な要因>を入力してください")
        analysis_obj = str(input())
        print("<主な要因>" + "\n" + analysis_obj + "が考えられる.")
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()


# ========================================
# <指標> <インプレッション> (投稿記事表示回数を想定)
imp = "<インプレッション>"
ratio_obj, subtract_obj = get_metric(imp)
day_metric(imp, ratio_obj, subtract_obj)
day_analysis(imp)

# ========================================
# <指標> <ページビュー> (投稿記事クリック数を想定)
pag = "<ページビュー>"
ratio_obj, subtract_obj = get_metric(pag)
day_metric(pag, ratio_obj, subtract_obj)
day_analysis(pag)

# ========================================
# 全体の要因分析
second_analysis()


# サンプルデータ
"""
インプレッション:
当日:590
前日:763
"""

"""
ページビュー:
当日:5
前日:10
"""

# 検証用
"""
ゼロ除算
当日:100
前日:0
小数入力
当日:1.1
前日:1.1
"""
