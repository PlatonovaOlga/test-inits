from .forward import forward

def bridge_action():
    exit()


def forward_logic(es, client, bot, action='forward'):
    event = es.add(
        unit='forward_logic',
        action=None,
        next_action=action, 
        payload={'msg': 'start forward_logic'})

    next_action = event.next_action

    match next_action:
        case 'forward':
            event = forward(es, client, bot)

    bridge_action()

