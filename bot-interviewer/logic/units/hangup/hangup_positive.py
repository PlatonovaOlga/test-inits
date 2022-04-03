from .save_event import save_event


def hangup_positive(es, client, bot):
    bot.phrase = bot.vocabulary.get('hangup_positive')
    print(bot.phrase)

    event = save_event(es, client, bot, __name__)

    return event