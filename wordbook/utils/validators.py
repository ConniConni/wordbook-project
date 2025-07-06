import re


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
