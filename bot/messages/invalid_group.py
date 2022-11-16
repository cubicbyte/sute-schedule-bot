from telebot import types

def create_message(message: types.Message) -> dict:
    message_text = message.lang['command.group_incorrect']
    markup = message.KeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton(text=message.lang['button.select_group'], callback_data='open.select_group'),
        types.InlineKeyboardButton(text=message.lang['button.menu'], callback_data='open.menu')
    )

    msg = {
        'chat_id': message.chat.id,
        'text': message_text,
        'reply_markup': markup,
        'parse_mode': 'Markdown'
    }

    return msg
