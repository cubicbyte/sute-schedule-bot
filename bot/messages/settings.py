from telebot import types

def create_message(message: types.Message) -> dict:
    group = message.config['schedule']['group_id'] or message.lang['text.not_selected']
    markup = message.KeyboardMarkup()
    message_text = message.lang['command.settings'].format(group_id=group)

    markup.add(
        types.InlineKeyboardButton(text=message.lang['button.select_group'], callback_data='open.select_group'),
        types.InlineKeyboardButton(text=message.lang['button.select_lang'], callback_data='open.select_lang')
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
