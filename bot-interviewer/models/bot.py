from collections import namedtuple
from datetime import datetime


class Bot:
    '''
    The Bot instance is the bot interviewer.
    Can start and end a conversation.
    name - name of the bot.
    unit - a string with the name of the logical block being executed.
    action - a string with the name of the action to be performed inside the logical block.
    phrase - the phrase to be spoken after the call to say()
    '''
    def __init__(self, name, company_name, vocabulary, unit=None, action=None, phrase=None):
        self.name = name
        self.unit = unit
        self.company_name = company_name
        self.action = action
        self.phrase = phrase
        self.vocabulary = vocabulary
        self.exit_point = dict()

        self.sessions = list()


    def start_call(self, es, client, unit=None):
        '''
        Takes a reference to the current client and event store object.
        Adds a session to the list of its sessions and specifies a starting point (logical block).
        unit - the name of the logical unit that is the start of the job.  
        '''
        Session = namedtuple('Session', 'datetime, es, client')

        self.sessions.append(
            Session(datetime.now(), es, client))

        self.unit = unit

    def end_call(self, unit, action):
        self.exit_point['unit'] = unit
        self.exit_point['action'] = action




