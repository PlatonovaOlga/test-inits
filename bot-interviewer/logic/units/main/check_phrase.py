def check_phrase(es, client, bot, action):
    '''
    Checks the client's phrase and, based on it, 
    returns an event to transfer control to another action or another module 
    '''
    negative_score = [str(i) for i in range(0, 9)]
    positive_score = [str(i) for i in range(9, 11)]

    match client.phrase:
        # TODO if repeat call switch to hangup_logic: hangup_null
        case '':
            next_unit = 'hangup_logic' if client.was_silent else 'main_logic'
            next_action= 'hangup_null' if client.was_silent else 'recommend_null'
            done_unit = True if client.was_silent else None

            client.was_silent = True
            event = es.add(
                unit='main_logic',
                action=action,
                next_unit=next_unit,
                next_action=next_action,
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'done_unit': done_unit})
            return event

        case client.phrase if client.phrase in negative_score:
            event = es.add( 
                unit='main_logic',
                action=action,
                next_unit='hangup_logic',
                next_action='hangup_negative',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'recommendation_score': client.phrase,
                    'done_unit': True})
            return event

        case client.phrase if client.phrase in positive_score:
            event = es.add( 
                unit='main_logic',
                action=action,
                next_unit='hangup_logic',
                next_action='hangup_positive',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'recommendation_score': client.phrase,
                    'done_unit': True})
            return event

        case 'нет':
            event = es.add(
                unit='main_logic',
                action=action,
                next_action='recommend_score_negative',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'recommendation': 'negative'})
            return event

        case 'возможно':
            event = es.add(
                unit='main_logic',
                action=action,
                next_action='recommend_score_neutral',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'recommendation': 'neutral'})
            return event

        case 'да':
            event = es.add(
                unit='main_logic',
                action=action,
                next_action='recommend_score_neutral',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'recommendation': 'neutral'})
            return event

        case 'ещё раз':
            event = es.add( 
                unit='main_logic',
                action=action,
                next_action='recommend_repeat',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'repeat': True})
            return event

        case 'не знаю':
            event = es.add( 
                unit='main_logic',
                action=action,
                next_action='recommend_repeat_2',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'recommendation': 'dont_know'})
            return event

        case 'занят':
            event = es.add(
                unit='main_logic',
                action=action,
                next_unit='hangup_logic',
                next_action='hangup_wrong_time',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'wrong_time': True,
                    'done_unit': True})
            return event

        case 'вопрос':
            event = es.add(
                unit='main_logic',
                action=action,
                next_unit='forward_logic',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'done_unit': True})
            return event

        case _:
            # TODO при повторе hangup_null
            event = es.add(
                unit='main_logic',
                action=action,
                next_unit='main_logic',
                next_action='recommend_default',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase})
            return event