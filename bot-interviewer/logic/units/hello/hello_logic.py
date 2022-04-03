from .hello import hello
from .hello_repeat import hello_repeat
from .hello_null import hello_null


def hello_logic(es, client, bot, action='hello'):
    '''
    Accepts objects: client, robot, event store
    The first step is to get consent.
    Returns an event with payload next_unit and next_action 
    '''
    event = es.add(
        unit='hello_logic',
        action=None,
        next_unit='hello_logic', 
        next_action=action, 
        payload={'msg': 'start hello'})

    done = False
    while not done:
        next_action = event.next_action

        match next_action:
            case 'hello':
                event = hello(es, client, bot)
            case 'hello_repeat':
                event = hello_repeat(es, client, bot)
            case 'hello_null':
                event = hello_null(es, client, bot)
            case _:
                raise ValueError('Requested next_action does not exist')
        
        done = event.payload.get("done_unit")

    return event



    



