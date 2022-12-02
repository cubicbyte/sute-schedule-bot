import telebot.types
import logging
from ..settings import bot
from ..pages import create_left_message

logger = logging.getLogger(__name__)

@bot.callback_query_handler(func=lambda call: call.query == 'open.left')
def handler(call: telebot.types.CallbackQuery):
    logger.debug('Handling callback query')
    bot.edit_message_text(**create_left_message(call.message), message_id=call.message.message_id)
