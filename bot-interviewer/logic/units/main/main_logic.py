from datetime import datetime
from .recommend_default import recommend_default
from .recommend_main import recommend_main
from .recommend_null import recommend_null
from .recommend_repeat import recommend_repeat
from .recommend_repeat_2 import recommend_repeat_2
from .recommend_score import recommend_score_negative, recommend_score_neutral, recommend_score_positive


def main_logic(es, client, bot, action):
    '''
    Принимает объекты: клиент, робот, хранилище событий
    Второй этап - получение информации о вероятности рекомендации
    Возвращает событие с payload, в котором указан next_unit и next_action
    '''
    done = False

    event = es.add(
        unit='main_logic',
        action=None,
        next_unit='main_logic', 
        next_action=action, 
        payload={'msg': 'start main'})

    # выполнять переход между actions до тех пор, пока не потребуется
    # переход в следующий логический модуль
    while not done:
        next_action = event.next_action

        match next_action:
            case 'recommend_null':
                event = recommend_null(es=es, client=client, bot=bot)
            case 'recommend_main':
                event = recommend_main(es=es, client=client, bot=bot)
            case 'recommend_default':
                event = recommend_default(es=es, client=client, bot=bot)
            case 'recommend_score_negative':
                event = recommend_score_negative(es=es, client=client, bot=bot)
            case 'recommend_score_neutral':
                event = recommend_score_neutral(es=es, client=client, bot=bot)
            case 'recommend_score_positive':
                event = recommend_score_positive(es=es, client=client, bot=bot)
            case 'recommend_repeat':
                event = recommend_repeat(es=es, client=client, bot=bot)
            case 'recommend_repeat_2':
                event = recommend_repeat_2(es=es, client=client, bot=bot)
            case _:
                raise ValueError('Requested next_action does not exist')
        
        # проверка на случай если такой ключ вообще не был передан
        done = event.payload.get('done_unit')
    
    return event