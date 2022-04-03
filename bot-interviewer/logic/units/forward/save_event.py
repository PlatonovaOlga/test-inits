def save_event(es, bot, action):
    event = es.add(
        unit='forward_logic',
        action=action,
        payload={
            'msg': 'stop forward_logic and script',
            'bot_phrase': bot.phrase,
            'done_unit': True,
            'done_script': True})
            
    return event