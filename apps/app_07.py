import sys

# 区切線
line_obj = "=" * 30

# 分析用語リスト
my_list = [
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


# インプレッション (投稿記事表示回数を想定)
def get_imp():
    print("小数点入力不可")
    try:
        print("<当日>")
        t_d = input()
        print("<前日分>")
        y_d = input()
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()

    # アンパック代入
    t_d, y_d = int(t_d), int(y_d)

    # 前日比 = 当日/前日
    try:
        imp_obj = t_d / y_d

    # 例外処理 <ゼロ除算>
    except ZeroDivisionError:
        print("<エラー!><ゼロ除算>")
        print("プログラムを終了します")
        sys.exit()

    # 小数第2位まで表示
    result = round(imp_obj, 2)
    print(line_obj)
    print("<インプレッション>" + "\n" + "<前日比>" + " " + str(result) + " " + "倍")
    print(line_obj)

    return result


# ページビュー (投稿記事クリック数を想定)
def get_pag():
    print("小数点入力不可")
    try:
        print("<当日>")
        t_d = input()
        print("<前日分>")
        y_d = input()
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()

    # アンパック代入
    t_d, y_d = int(t_d), int(y_d)

    # 前日比 = 当日/前日
    try:
        pag_obj = t_d / y_d

    # 例外処理 <ゼロ除算>
    except ZeroDivisionError:
        print("<エラー!><ゼロ除算>")
        print("プログラムを終了します")
        sys.exit()

    # 小数第2位まで表示
    result = round(pag_obj, 2)
    print(line_obj)
    print("<ページビュー>" + "\n" + "<前日比>" + " " + str(result) + " " + "倍")
    print(line_obj)

    return result


# 前日比計算
def main():
    print("<インプレッション>")
    get_imp()
    print("<ページビュー>")
    get_pag()


# 計算結果分析
def sub():
    try:
        print("<インプレッション>分析開始")
        print("<分析用語>を入力してください")
        first = str(input())
        print("<ページビュー>分析開始")
        print("<分析用語>を入力してください")
        second = str(input())
    except KeyboardInterrupt:
        print("入力がキャンセルされました")
        print("プログラムを終了します")
        sys.exit()

    text_obj = "<インプレッション>:" + first + "\n" + "<ページビュー>:" + second
    return text_obj


# ==============================================
# 1.前日比計算実行
main()
# ==============================================
# 2.計算結果分析実行
print(line_obj)
print("<計算結果分析開始>")
print("<分析用語リスト>")
print(my_list)
print(line_obj)
text_obj = sub()
# ==============================================
# 3.実行結果
print(line_obj)
print("<結論>" + "\n" + text_obj)
print(line_obj)
# ==============================================

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
