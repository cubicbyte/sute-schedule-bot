import telebot.types
import logging
from ..settings import bot, chat_configs
from ..messages import create_select_course_message

logger = logging.getLogger(__name__)

@bot.callback_query_handler(func=lambda call: call.query == 'select.schedule.faculty')
def handler(call: telebot.types.CallbackQuery):
    logger.debug('Handling callback query')
    faculty_id = int(call.args['facultyId'])
    struct_id = int(call.args['structureId'])
    chat_configs.set_chat_config(call.message.chat.id, call.message.config)
    bot.edit_message_text(**create_select_course_message(call.message, struct_id, faculty_id), message_id=call.message.id)