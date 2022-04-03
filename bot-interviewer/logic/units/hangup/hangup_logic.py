from .hangup_negative import hangup_negative
from .hangup_positive import hangup_positive
from .hangup_null import hangup_null
from .hangup_wrong_time import hangup_wrong_time


def hangup_action():
    exit()


def hangup_logic(es, client, bot, action):
    event = es.add(
        unit='hangup_logic',
        action=None,
        next_action=action, 
        payload={'msg': 'start hangup_logic'})

    next_action = event.next_action

    match next_action:
        # TODO no need to receive the event, can be simplified 
        case 'hangup_null':
            event = hangup_null(es, client, bot)
        case 'hangup_negative':
            event = hangup_negative(es, client, bot)  
        case 'hangup_positive':
            event = hangup_positive(es, client, bot)
        case 'hangup_wrong_time':
            event = hangup_wrong_time(es, client, bot)
        case _:
            raise ValueError('Requested next_action does not exist')

    hangup_action()