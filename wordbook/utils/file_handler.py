import csv


CSV_FILE = "data_dict.csv"


def load_csv_file():
    """
    CSVファイルの内容を読み取る
    データがある場合はdictに代入する
    データがない場合はヘッダーのみを持つCSVファイルを新規作成する
    """

    # 空の辞書を定義
    word_dict = {}

    try:
        # utf-8で読み込みモードでファイルを開く
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            # readerオブジェクト（CSVのルールを理解して１行ずつリスト化したもの）を生成する
            reader = csv.reader(f)
            # ヘッダーはスキップする（next()を使ってイテレータを1行進めることで実現）
            header = next(reader)
            # CSVのレコードからdict_wordのキー・バリューを取得する
            for row in reader:
                word_dict[row[0]] = row[1]
            print("データをCSVファイルから読み込みました")

    # open()しようとしたCSV_FILEが存在しない場合
    except FileNotFoundError:
        print("CSVファイルが見つかりません 新しいCSVファイルを作成します")
        # CSVファイルを新規作成（中身はヘッダーのみ）
        with open(CSV_FILE, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["英単語", "日本語訳"])

    # open()しようとしたCSV_FILEは存在するがヘッダーのみの場合
    except StopIteration:
        print("CSVファイルは空です")

    return word_dict


def save_data_to_csv_file(word_dict):
    """
    登録された単語をCSVに保存する
    関数が呼び出される度に、CSVファイルにヘッダーを書き込む
    現在の辞書全体を、CSVファイルに丸ごと上書き保存する
    """

    with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
        # writerオブジェクトを生成する（書き込み処理が可能になる）
        writer = csv.writer(f)
        # ヘッダーを挿入する
        writer.writerow(["英単語", "日本語訳"])
        # 辞書のキー・バリューを取り出し、CSVのレコードとして書き込む
        for eg_word, jp_word in word_dict.items():
            writer.writerow([eg_word, jp_word])
