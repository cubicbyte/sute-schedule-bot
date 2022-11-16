import logging
import telebot.types
from datetime import date, timedelta
from ..settings import bot, langs
from .. import messages

logger = logging.getLogger(__name__)

buttons = {}
for lang_code, lang in langs.items():
    for key, value in lang.items():
        if key.startswith('button'):
            buttons[value] = key


@bot.message_handler()
def handle_command(message: telebot.types.Message):
    logger.info(f'Handling keyboard command {message.text} from chat {message.chat.id}')

    if not message.text in buttons:
        return
    
    action = buttons[message.text]

    if action == 'button.admin_panel':
        if message.config['admin'] is not True:
            bot.send_message(**messages.create_access_denied_message(message))
            return 

        bot.send_message(**messages.create_admin_panel_message(message))

    elif action == 'button.calls':
        bot.send_message(**messages.create_calls_message(message))

    elif action == 'button.menu':
        bot.send_message(**messages.create_menu_message(message))

    elif action == 'button.schedule.today':
        time = date.today()
        bot.send_message(**messages.create_schedule_message(message, time))

    elif action == 'button.schedule.tomorrow':
        time = date.today() + timedelta(days=1)
        bot.send_message(**messages.create_schedule_message(message, time))

    elif action == 'button.':
        bot.send_message(**messages.create__message(message))

    elif action == 'button.':
        bot.send_message(**messages.create__message(message))

    

    print(action)