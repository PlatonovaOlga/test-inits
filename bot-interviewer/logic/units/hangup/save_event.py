def save_event(es, client, bot, action):
    event = es.add(
        unit='hangup_logic',
        action=action,
        payload={
            'msg': 'stop hangup_logic and script',
            'bot_phrase': bot.phrase,
            'done_unit': True,
            'done_script': True})
            
    return event