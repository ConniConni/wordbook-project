import logging
import random

from .utils.file_handler import save_data_to_csv_file
from .utils.validators import is_half_width_alpha_only
from .utils.validators import is_japanese_char_only


# ロガーを生成する
logger = logging.getLogger(__name__)


def register_word(word_dict):
    print("=== 単語登録を行います ===")

    while True:
        print("英単語を入力してください")
        input_eg_word = input(">>> ")

        if is_half_width_alpha_only(input_eg_word):
            break
        else:
            logger.warning("無効な入力です: 英単語登録に半角英字以外が入力されました。")
            print("エラー: 英単語は半角英字で入力してください")

    while True:
        print("入力した英単語の日本語訳を入力してください")
        translation_jp_word = input(">>> ")
        if is_japanese_char_only(translation_jp_word):
            break
        else:
            logger.warning(
                "無効な入力です: 日本語訳登録に漢字・ひらがな・カタカナ以外が入力されました。"
            )
            print("エラー: 日本語訳は 漢字・ひらがな・カタカナで入力してください")

    word_dict[input_eg_word] = translation_jp_word

    save_data_to_csv_file(word_dict)

    logger.info(
        f"英単語: '{input_eg_word}', 日本語訳: '{translation_jp_word}' を登録しました。"
    )
    print("以下の英単語と日本語訳を保存しました")
    print(f"英単語: {input_eg_word}")
    print(f"日本語訳: {translation_jp_word}")


def start_quiz(word_dict):
    print("=== クイズを行います ===")
    if not word_dict:
        logger.warning("CSVが不正です: 登録された英単語がありません。")
        print("登録された英単語がありません。英単語を登録してください")
        return

    # word_dictのキーをリストで保持し、ランダムに１つ抽出
    all_keys = list(word_dict.keys())
    choice_key = random.choice(all_keys)

    # キーに対応する日本語訳をプロンプトに表示し、ユーザーに英単語の入力を求める
    # 入力は半角英字のみを許可する
    while True:
        print(f"'{word_dict[choice_key]}'を英訳して入力してください")
        answer_eg_word = input(">>> ")
        if is_half_width_alpha_only(answer_eg_word):
            break
        else:
            logger.warning("無効な入力です: 回答に半角英字以外が入力されました")
            print("エラー: 英訳は半角英字のみで入力してください")

    # ユーザーの回答とword_dictのキーを比較し、正誤判定を行う
    if answer_eg_word == choice_key:
        logger.info(f"正解です: 回答 '{answer_eg_word}'")
        print("正解です！")
    else:
        logger.info(f"不正解です: 回答 '{answer_eg_word}'")
        print("不正解です")
        print(f"正解は{choice_key}です")
