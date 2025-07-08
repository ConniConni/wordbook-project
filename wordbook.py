from wordbook import logger_config
from wordbook import main


# --- プログラムの実行開始点　---
if __name__ == "__main__":
    # アプリケーションのログ設定処理を呼び出す
    logger_config.setup_logging()
    # アプリケーションを実行処理を呼び出す
    main.run_app()
