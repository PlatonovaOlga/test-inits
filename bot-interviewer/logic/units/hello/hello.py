from .check_phrase import check_phrase


def hello(es, client, bot):
    '''
    Greet and save answer in client.phrase
    '''
    bot.phrase = bot.vocabulary.get('hello').format(
        client_name=client.name, 
        company_name=bot.company_name,
        bot_name=bot.name)
        
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event