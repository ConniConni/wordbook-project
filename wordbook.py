choice_mode = 0

while choice_mode != 3:
    print("実行したい操作の番号を入力してください")
    print("1: 単語登録")
    print("2: クイズ")
    print("3: 終了")

    try:
        choice_mode = int(input(">>>"))

    except ValueError:
        print("エラー: 半角英数字で入力してください")
        continue

    if choice_mode == 1:
        print("単語登録を行います")
    elif choice_mode == 2:
        print("クイズを行います")
    elif choice_mode == 3:
        print("終了します")
    else:
        print("有効な数字を入力してください")
