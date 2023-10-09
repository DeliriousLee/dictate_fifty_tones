import random

# 平假名和片假名的字典
hiragana_dict = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'hu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'だ': 'da', 'ぢ': 'ji', 'づ': 'zu', 'で': 'de', 'ど': 'do',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
}

katakana_dict = {
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'hu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n',
    'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',
    'ザ': 'za', 'ジ': 'ji', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',
    'ダ': 'da', 'ヂ': 'ji', 'ヅ': 'zu', 'デ': 'de', 'ド': 'do',
    'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
    'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po',
}

# 答对多少题目提示
correct_tips_num = 20
# 答错多少题目提示
wrong_tips_num = 5


# return (假名，假名类型，罗马音)
def random_kana() -> tuple:
    # 随机选择平假名或片假名
    kana_type = random.choice(['平假名', '片假名'])

    if kana_type == 'hiragana':
        kana = random.choice(list(hiragana_dict.keys()))
        kana_roman = hiragana_dict[kana]
    else:
        kana = random.choice(list(katakana_dict.keys()))
        kana_roman = katakana_dict[kana]
    return kana, kana_type, kana_roman


# 抽取 假名，输入给出罗马音
def pick_name_card() -> (bool, str):
    kana, kana_type = random_kana()
    print(f'随机选择的{kana_type}字符是：{kana}')

    user_input = input('请输入注音（音）：')

    if kana_type == 'hiragana':
        correct_reading = hiragana_dict[kana]
    else:
        correct_reading = katakana_dict[kana]
    return (user_input == correct_reading), correct_reading


# 给出 罗马音，等待y/n之后给出字符
def pick_roman_card() -> bool:
    kana, kana_type, roman = random_kana()
    print(f'随机选择的{kana_type} 罗马音是：{roman}')
    user_input = input('请输入是否要给出答案(y/n)')

    if user_input == 'y':
        print(f'答案是{kana}')
        result_input = input('请输入是否和答案相一致(y/n)')
        if result_input == 'y':
            return True
        else:
            return False


# 开始 抽取假名游戏
def start_random_kana_game():
    correct_num = 0
    wrong_num = 0
    while True:
        result, correct_read = pick_name_card()
        if result:
            correct_num += 1
            print('回答正确！')
        else:
            wrong_num += 1
            print(f'回答错误，正确的注音是：{correct_read}')
        if correct_num > 0 and correct_num % correct_tips_num == 0:
            print(f'已经答对{correct_num}道题目咯，再接再厉')
        if wrong_num > 0 and wrong_num % wrong_tips_num == 0:
            print(f'已经答错{wrong_num}道题目，仔细读题认真复习')


def start_random_roman_game():
    correct_num = 0
    wrong_num = 0
    while True:
        result = pick_roman_card()
        if not result:
            wrong_num += 1
            print(f'回答错误')
        else:
            correct_num += 1
            print('回答正确！')
        if correct_num > 0 and correct_num % correct_tips_num == 0:
            print(f'已经答对{correct_num}道题目咯，再接再厉')
        if wrong_num > 0 and wrong_num % wrong_tips_num == 0:
            print(f'已经答错{wrong_num}道题目，仔细读题认真复习')


def main():
    game_mode = input('请输入游戏模式：(1:给罗马音写假名 /2：给假名写罗马音)')
    if game_mode == 1 or game_mode == '1':
        start_random_roman_game()
    else:
        start_random_kana_game()


if __name__ == "__main__":
    main()
