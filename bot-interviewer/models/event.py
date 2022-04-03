from datetime import datetime

class Event:
    '''
    An event must be created and recorded after each phrase of the client 
    '''
    def __init__(self, datetime, unit, action, next_unit, next_action, payload):
        self.datetime = datetime
        self.unit = unit
        self.action = action
        self.next_unit = next_unit
        self.next_action = next_action
        self.payload = payload


class EventStorage:
    def __init__(self) -> None:
        self.data = list()


    def add(self, unit, action=None, next_unit=None, next_action=None, payload=None):
        event = Event(datetime.now(), unit, action, next_unit, next_action, payload)
        self.data.append(event)

        return event