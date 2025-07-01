def main():
    """単語帳アプリケーションのメイン関数"""
    word_dict = {}

    while True:
        print("実行したい操作の番号を入力してください")
        print("1: 単語登録")
        print("2: クイズ")
        print("3: 終了")

        try:
            choice_mode = int(input(">>>"))

        except ValueError:
            print("エラー: 半角数字で入力してください")
            continue

        if choice_mode == 1:
            register_word(word_dict)
        elif choice_mode == 2:
            start_quiz(word_dict)
        elif choice_mode == 3:
            print("終了します")
            break
        else:
            print("有効な数字を入力してください")


def register_word(word):
    print("単語登録を行います")


def start_quiz(word):
    print("クイズを行います")


# --- プログラムの実行開始点　---
if __name__ == "__main__":
    main()
