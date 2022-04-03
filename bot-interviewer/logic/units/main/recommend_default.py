from .check_phrase import check_phrase


def recommend_default(es, client, bot):
    '''
    Asks to repeat and stores the client's phrase in client.phrase 
    '''
    bot.phrase = bot.vocabulary.get('recommend_null')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event
