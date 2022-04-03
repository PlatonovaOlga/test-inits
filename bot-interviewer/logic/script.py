from .units import hello_logic, main_logic, hangup_logic, forward_logic


def script(bot, client, es):
    '''
    Robot-interviewer logic switching
    '''
    # start work
    bot.start_call(es, client)

    event = es.add(
        unit=None,
        action=None,
        next_unit='hello_logic', 
        next_action='hello', 
        payload={'msg': 'start robot'})
 
    # switch between logical blocks
    # the loop will run until any of the logic blocks says {'done': True} in event.payload 
    done = False
    while not done:
        next_action = event.next_action

        match event.next_unit:
            case 'hello_logic':
                event = hello_logic(es, client, bot) 
            case 'main_logic':
                # checking for repeated silence depends on the client attribute
                # executed in check_phrase
                # TODO should consider another solution 
                client.was_silent = False
                event = main_logic(es, client, bot,  next_action)
            case 'hangup_logic':
                event = hangup_logic(es, client, bot,  next_action)
            case 'forward_logic':
                event = forward_logic(es, client, bot)
            case _:
                raise ValueError('Requested next_unit does not exist')
        
        done = event.payload.get('done_script')

    bot.end_call(event.unit, event.action)

    exit()