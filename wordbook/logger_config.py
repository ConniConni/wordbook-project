import logging


def setup_logging():
    """コマンドライン単語帳のログ設定を行う関数"""

    # ルートロガーを生成
    logger = logging.getLogger()
    # ルートロガーにログレベルを設定
    logger.setLevel(logging.WARNING)
    # フォーマッタを設定
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        "%Y-%m-%d %H:%M:%S",  # タイムスタンプの書式
    )
    # ハンドラでフォーマットと書き出し先を設定
    file_handler = logging.FileHandler("wordbook_log.txt", encoding="utf-8")
    file_handler.setFormatter(formatter)

    # ロガーに登録するハンドラが１つになるようにする
    if not logger.handlers:
        logger.addHandler(file_handler)
