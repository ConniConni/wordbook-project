import logging

from .utils.file_handler import load_csv_file
from .core import register_word
from .core import start_quiz


# ロガーを生成する
logger = logging.getLogger(__name__)


def run_app():
    """単語帳アプリケーションのメイン関数"""

    logger.info("アプリケーションを開始")

    # CSVファイルを読み込み辞書型のリストword_dictを生成する
    word_dict = load_csv_file()

    while True:
        print("=== 実行したい操作の番号を入力してください ===")
        print("1: 単語登録")
        print("2: クイズ")
        print("3: 終了")

        try:
            choice_mode = int(input(">>> "))

        except ValueError:
            logger.warning("無効な入力です: 整数以外が入力されました。")
            print("エラー: 半角数字で入力してください")
            continue

        if choice_mode == 1:
            register_word(word_dict)
        elif choice_mode == 2:
            start_quiz(word_dict)
        elif choice_mode == 3:
            print("終了します")
            logger.info("アプリケーションを終了")
            break
        else:
            logger.warning("無効な入力です: 選択肢以外の整数が入力されました。")
            print("有効な数字を入力してください")
