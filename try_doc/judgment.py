""" ポジネガ判定したい記事を取得して、ポジネガスコアをつけた結果を返す

サンプル本文では、90 の判定結果となった
>>> 判定結果: 90 ポイント

"""

import datetime


def count_words(text: str, words: list) -> int:
    """ 本文から設定したワードが含まれている数を抽出 """
    count = 0
    for word in words:
        count += text.count(word)
    return count


def judgment_posi_nega(target_text: str) -> int:
    """ ポジネガ判定 """
    # TODO: 設定ファイル etc に値を持たせる: 気軽に変えられるようにする.
    negative_words = ["悪い", "嫌い", "イライラ", "鬱", "疲れ", "悲しい", "失望", "やばい", "うざい", "愚痴", "ストレス", "落ち込む", "恨み", "苦しい",
                      "くだらない", "辛い", "むかつく", "空虚", "苦手", "不安", "嫌", "暗い", "憂鬱", "泣く", "悩む", "反感", "不満", "無力", "嫉妬",
                      "恐れ", "憎しみ", "衰退", "後悔", "堪える", "仕返し", "空腹", "不幸", "恥ずかしい", "苦悩", "感傷", "怠惰", "懊悩", "無関心", "嘲笑",
                      "冷たい", "無気力", "悪夢", "退屈", "絶望", "罪悪感"]
    positive_words = ["楽しい", "幸せ", "笑顔", "やる気", "感謝", "ありがとう", "元気", "大好き", "良い", "笑う", "喜び", "ハッピー", "癒し", "安心", "期待",
                      "快適", "嬉しい", "成功", "おめでとう", "親切", "頑張る", "美味しい", "素晴らしい", "ステキ", "エネルギー", "信頼", "励ます", "努力", "勇気",
                      "賞賛", "輝く", "誇り", "有益", "勝利", "進歩", "光栄", "満足", "温かい", "忠実", "希望", "友情", "誠実", "刺激", "魅力", "情熱",
                      "共感", "誠意", "応援", "幸運", "寛大"]

    negative_count = count_words(target_text, negative_words)
    positive_count = count_words(target_text, positive_words)

    return negative_count * 10 - positive_count * 10


def save_article(target_text: str, score: int, url: str, media_type: str, posted_at: datetime):
    """ TODO: DB格納: Twitter 以外の Media も想定
     Articles TBL:
       id          : ユニークID
       text        : 投稿本文
       score       : ポジネガ判定
       url         : 投稿 URL
       media_type  : 取得元メディア名
       posted_at   : 投稿時間
       created_at  : DB 格納時間
       updated_at  : DB 更新時間
    """


def main():
    # サンプル
    target_text = "怠惰, 懊悩, 無関心, 嘲笑, 冷たい, 無気力, 悪夢, 退屈, 絶望, 罪悪感. お好み焼きは美味しい"
    score = judgment_posi_nega(target_text)

    print(f"判定結果: {score} ポイント")

    # TODO: DB 保存
    save_article(
        target_text=target_text, score=score, url='https://xxx',
        media_type='', posted_at=datetime.datetime.now()
    )


if __name__ == '__main__':
    main()
