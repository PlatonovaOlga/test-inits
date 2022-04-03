from .check_phrase import check_phrase


def recommend_null(es, client, bot):
    '''
    Просит повторить и сохраняет фразу клиента в client.phrase
    '''
    bot.phrase = bot.vocabulary.get('recommend_null')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event

