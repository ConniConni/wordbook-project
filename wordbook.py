print("実行したい操作の番号を入力してください" "1: 単語登録" "2: クイズ" "3: 終了")
choice_mode = 0

while choice_mode != 3:
    choice_mode = int(input())

    if choice_mode == 1:
        print("単語登録を行います")
    elif choice_mode == 2:
        print("クイズを行います")
    elif choice_mode == 3:
        print("終了します")
    else:
        print("有効な数字を入力してください")
