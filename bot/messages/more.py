from telebot import types

def create_message(message: types.Message) -> dict:
    message_text = message.lang['command.more']
    markup = message.KeyboardMarkup()

    markup.add(
        types.InlineKeyboardButton(text=message.lang['button.calls'], callback_data='open.calls'),
        types.InlineKeyboardButton(text=message.lang['button.info'], callback_data='open.info')
    )

    markup.add(
        types.InlineKeyboardButton(text=message.lang['button.back'], callback_data='open.menu')
    )

    msg = {
        'chat_id': message.chat.id,
        'text': message_text,
        'reply_markup': markup,
        'parse_mode': 'Markdown'
    }

    return msg
