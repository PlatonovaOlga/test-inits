from .check_phrase import check_phrase


def recommend_repeat_2(es, client, bot):
    '''
    Повторяет вопрос об оценке и сохраняет фразу клиента в client.phrase
    '''
    bot.phrase = bot.vocabulary.get('recommend_repeat_2')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event

