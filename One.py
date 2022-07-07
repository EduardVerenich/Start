from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


# -698326696     Vxod         -1001705438794
#   -757001906   отгрузка     -1001680322912
#   -604455394   остальное    -1001761735220
#   -789695658   выкинутое    -1001636807619

bot = Bot(token='5476160874:AAHFAmQ27xto5_4Q94nNM1qfckGlD5iDkC4')
dp = Dispatcher(bot)
INPUT_MSG_CHAT_ID = '-1001705438794'
OZER_MSG_CHAT_ID = '-1001636807619'

CHATS = {
    "Отгрузка": {
        "chat_id": '-1001680322912',
        'message_paterns': [
            'загрузка',
            'погрузка',
            'выгрузка',
            'отгрузка'
        ],
        'to_print': '<b>Заявка для отгрузки</b>\n\n'
    },
    'Остольное': {
        "chat_id": '-1001761735220',
        'message_paterns': [
            'доставить',
            'перевозка',
            'перевозить',
            'отвести'
        ],
        'to_print': '<b>Заявка для остольное</b>\n\n'
    }

}


@dp.message_handler(chat_type=[types.ChatType.GROUP, types.ChatType.PRIVATE, types.ChatType.SUPERGROUP])
async def process_lead(message):
    is_send = False
    if message.chat.id != -1001761735220 and message.chat.id != -1001680322912 and message.chat.id != -1001636807619:      # отсикает сообщения в ненужных чатах
        for chat_name, content in CHATS.items():
            chat_id = content['chat_id']
            for allowed_word in content['message_paterns']:
                if allowed_word in message.text.lower():                                                                   # введенный текст становится маленьким и сверяется с базай
                    await bot.send_message(chat_id, content['to_print'] + message.text, parse_mode='html')                 # отправляет в оприделенную группу
                    await message.reply('<b>заявка ушла в %s:</b>\n\n' % chat_name, parse_mode='html')                     # отвичает, куда ушла заявка
                    is_send = True
                    break

    if not is_send:
        if message.chat.id != -1001761735220 and message.chat.id != -1001680322912 and message.chat.id != -1001636807619:
            await bot.send_message(OZER_MSG_CHAT_ID, '<b>Неразборчево:</b>\n\n' + message.text, parse_mode='html')
            await message.reply('<b>заявка ушла в Выкинутое</b>\n\n' , parse_mode='html')
    #     print(message.text)


# @dp.message_handler(con)
# async def procces_lead(message):
# print(message.text)


executor.start_polling(dp)
