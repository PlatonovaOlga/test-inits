from logic import script
from models import Bot, Client, EventStorage, vocabulary


client = Client('Заяц')
bot = Bot('Белка', 'ООО Волшебный лес', vocabulary)     

es = EventStorage()


if __name__ == '__main__':
    script(bot, client, es)

