from .check_phrase import check_phrase


def recommend_score_negative(es, client, bot):
    bot.phrase = bot.vocabulary.get('recommend_score_negative')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event


def recommend_score_neutral(es, client, bot):
    bot.phrase = bot.vocabulary.get('recommend_score_neutral')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event


def recommend_score_positive(es, client, bot):
    bot.phrase = bot.vocabulary.get('recommend_score_positive')
    client.phrase = input(bot.phrase)

    event = check_phrase(es, client, bot, __name__)

    return event

