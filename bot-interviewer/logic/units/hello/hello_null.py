from .check_phrase import check_phrase


def hello_null(es, client, bot):
    '''
    Repeat phrase and save answer in client.phrase
    '''
    bot.phrase = bot.vocabulary.get('hello_null').format(
        client.name, 
        bot.company_name)

    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event