import re
import random
import csv

CSV_FILE = "data_dict.csv"


def main():
    """単語帳アプリケーションのメイン関数"""
    word_dict = {}
    # CSVファイルを読み込みword_dictに値を代入
    load_csv_file(word_dict)

    while True:
        print("=== 実行したい操作の番号を入力してください ===")
        print("1: 単語登録")
        print("2: クイズ")
        print("3: 終了")

        try:
            choice_mode = int(input(">>> "))

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
    print("=== 単語登録を行います ===")

    while True:
        print("英単語を入力してください")
        input_eg_word = input(">>> ")

        if is_half_width_alpha_only(input_eg_word):
            break
        else:
            print("エラー: 英単語は半角英字で入力してください")

    while True:
        print("入力した英単語の日本語訳を入力してください")
        translation_jp_word = input(">>> ")
        if is_japanese_char_only(translation_jp_word):
            break
        else:
            print("エラー: 日本語訳は 漢字・ひらがな・カタカナで入力してください")

    word[input_eg_word] = translation_jp_word

    print("以下の英単語と日本語訳を保存しました")
    print(f"英単語: {input_eg_word}")
    print(f"日本語訳: {translation_jp_word}")


def start_quiz(word):
    print("=== クイズを行います ===")
    if not word:
        print("登録された英単語がありません。英単語を登録してください")
        return

    # word_dictのキーをリストで保持し、ランダムに１つ抽出
    all_keys = list(word.keys())
    choice_key = random.choice(all_keys)

    # キーに対応する日本語訳をプロンプトに表示し、ユーザーに英単語の入力を求める
    # 入力は半角英字のみを許可する
    while True:
        print(f"'{word[choice_key]}'を英訳して入力してください")
        answer_eg_word = input(">>> ")
        if is_half_width_alpha_only(answer_eg_word):
            break
        else:
            print("エラー: 英訳は半角英字のみで入力してください")

    # ユーザーの回答とword_dictのキーを比較し、正誤判定を行う
    if answer_eg_word == choice_key:
        print("正解です！")
    else:
        print("不正解です")
        print(f"正解は{choice_key}です")


def load_csv_file(dict):
    """
    CSVファイルの内容を読み取る
    データがある場合はdictに代入する
    データがない場合はヘッダーのみを持つCSVファイルを新規作成する
    """

    try:
        # utf-8で読み込みモードでファイルを開く
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            # readerオブジェクト（CSVのルールを理解して１行ずつリスト化したもの）を生成する
            reader = csv.reader(f)
            # ヘッダーはスキップする（next()を使ってイテレータを1行進めることで実現）
            header = next(reader)
            # CSVのレコードからdict_wordのキー・バリューを取得する
            for row in reader:
                dict[row[0]] = row[1]
            print("データをCSVファイルから読み込みました")
    # open()しようとしたCSV_FILEが存在しない場合
    except FileNotFoundError:
        print("CSVファイルが見つかりません 新しいCSVファイルを作成します")
        with open(CSV_FILE, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["英単語", "日本語訳"])
    # open()しようとしたCSV_FILEは存在するがヘッダーのみの場合
    except StopIteration:
        print("CSVファイルは空です")


def is_half_width_alpha_only(text):
    """
    文字列が半角アルファベット（a-z, A-Z）のみで構成されているかを判定します。
    """

    # 文字列が空の場合はFalseとする
    if not text:
        return False

    # 正規表現パターン
    # ^: 文字列の先頭
    # $: 文字列の末尾
    # [a-zA-Z]+: aからz、AからZのいずれかの文字が1回以上続く
    alpha_pattern = r"^[a-zA-Z]+$"

    if re.fullmatch(alpha_pattern, text):
        return True
    else:
        return False


def is_japanese_char_only(text):
    """
    文字列が漢字、ひらがな、カタカナ（全角）のみで構成されているかを判定します。
    長音符「ー」や、繰り返し記号「々」も含みます。
    """

    # 文字列が空の場合はFalseとする
    if not text:
        return False

    # 正規表現パターン
    # ^: 文字列の先頭
    # $: 文字列の末尾
    # [...]+: [...]内のいずれかの文字が1回以上続く
    # \u4E00-\u9FFF: CJK統合漢字（一般的な漢字）
    # \u3040-\u309F: ひらがな
    # \u30A0-\u30FF: カタカナ（全角）
    # ー: 長音符
    # 々: 繰り返し記号
    japanese_pattern = r"^[一-龠ぁ-んァ-ヶー々]+$"
    if re.fullmatch(japanese_pattern, text):
        return True
    else:
        return False


# --- プログラムの実行開始点　---
if __name__ == "__main__":
    main()
