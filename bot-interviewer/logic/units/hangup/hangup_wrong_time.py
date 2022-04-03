from .save_event import save_event


def hangup_wrong_time(es, client, bot):
    bot.phrase = bot.vocabulary.get('hangup_wrong_time')
    print(bot.phrase)

    event = save_event(es, client, bot, __name__)

    return event