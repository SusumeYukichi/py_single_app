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
        "横ばい",
    ],
    [
        "減少",
        "急落",
    ],
]


def get_ratio():
    print("小数点入力不可")
    try:
        print("<当日>")
        t_d = input()
        print("<前日分>")
        y_d = input()
        # アンパック代入
        t_d, y_d = int(t_d), int(y_d)
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()

    try:
        # 前日比 = 当日/前日
        ratio_obj = t_d / y_d
        # 小数第2位まで表示
        result = round(ratio_obj, 2)

    # 例外処理 <ゼロ除算>
    except ZeroDivisionError:
        print("<エラー!><ゼロ除算>")
        print("プログラムを終了します")
        sys.exit()

    return result


def get_metric(index):
    result = get_ratio()
    print(line_obj)
    print(index + " " + "<前日比>" + " " + str(result) + " " + "倍")
    print(line_obj)


def get_list():
    print("<分析用語リスト>")
    print(line_obj)
    print(analysis_list)
    print(line_obj)


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


def get_result(index):
    print("<計算結果分析開始>")
    result = get_analysis()
    print(line_obj)
    print(index + "\n" + result + "と考えられる.")
    print(line_obj)


# ========================================
# <インプレッション> (投稿記事表示回数を想定)
get_metric("<インプレッション>")
# 計算結果分析実行
get_result("<インプレッション>")
# ========================================
# <ページビュー> (投稿記事クリック数を想定)
get_metric("<ページビュー>")
# 計算結果分析実行
get_result("<ページビュー>")
# ========================================

# サンプルデータ
"""
当日:590
前日:763
当日:10
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
