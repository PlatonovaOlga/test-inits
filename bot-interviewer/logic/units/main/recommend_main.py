from .check_phrase import check_phrase


def recommend_main(es, client, bot):
    '''
    Спрашивает оценку и сохраняет фразу клиента в client.phrase
    '''
    bot.phrase = bot.vocabulary.get('recommend_main')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event
