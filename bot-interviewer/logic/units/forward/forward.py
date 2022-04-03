from .save_event import save_event


def forward(es, client, bot):
    bot.phrase = bot.vocabulary.get('forward')
    print(bot.phrase)

    event = save_event(es, bot, __name__)

    return event
