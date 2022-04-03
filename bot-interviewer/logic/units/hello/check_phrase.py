def check_phrase(es, client, bot, action):
    '''
    Checks the client's phrase and, based on it, 
    returns an event to transfer control to another action or another module 
    '''
    match client.phrase:
        case '':
            # checking for repeated silence depends on the client attribute
            # TODO consider another solution
            # reset in scripts before calling main_logic 
            next_unit = 'hangup_logic' if client.was_silent else 'hello_logic' 
            next_action = 'hangup_null' if client.was_silent else 'hello_null'
            done_unit = True if client.was_silent else None

            client.was_silent = True
            
            event = es.add( 
                unit='hello_logic',
                action=action,
                next_unit=next_unit,
                next_action=next_action,
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'done_unit': done_unit})
            return event

        case 'да':
            event = es.add(
                unit='hello_logic',
                action=action,
                next_unit='main_logic',
                next_action='recommend_main',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'confirm': True,
                    'done_unit': True})
            return event

        case 'нет':
            event = es.add(
                unit='hello_logic',
                action=action,
                next_unit='hangup_logic',
                next_action='hangup_wrong_time',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'confirm': False,
                    'done_unit': True})
            return event

        case 'занят':
            event = es.add( 
                unit='hello_logic',
                action=action,
                next_unit='hangup_logic',
                next_action='hangup_wrong_time',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'wrong_time': True,
                    'done_unit': True})
            return event

        case 'ещё раз':
            event = es.add(
                unit='hello_logic',
                action=action,
                next_action='hello_repeat',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'repeat': True})
            return event

        case _:
            event = es.add(
                unit='hello_logic',
                action=action,
                next_unit='main_logic',
                next_action='recommend_main',
                payload={
                    'bot_phrase': bot.phrase,
                    'client_phrase': client.phrase,
                    'done_unit': True})
            return event