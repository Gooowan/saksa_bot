import random
import telebot

TOKEN = '6577957091:AAER5wegM_OpVGfqYSOc6NkdZtFpRSeSE2Q'
bot = telebot.TeleBot(TOKEN)

values = ['Ваня @igotblessed'
    , 'Міша @seheda'
    , 'Назар @galuknazar'
    , 'Діма @javaSendman'
    , 'Варгес @anzr0'
    , 'Артем @artemgaluk'
    , 'Влад @@Vlad_Shch_05'
    , 'Yevgen @godmodeonn'
    , 'Остап @ospapi'
    , 'Стас @stasmarii'
    , 'Нікіта @sviridov1401']
last_picked_index = -1

fields = {
    "Поверхні": 2,
    "Сосунка": 2,
    "Підлога": 2,
    "Кухня": 2,
    "Великий": 2,
    "Маленький": 1
}


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global last_picked_index
    if "/bot musor" in message.text:
        last_picked_index += 1
        if last_picked_index >= len(values):
            last_picked_index = 0
        bot.reply_to(message, values[last_picked_index])
    if "/bot pidorasim" in message.text:
        random.shuffle(values)
        response = ""
        start_index = 0
        for field, count in fields.items():
            selected_people = values[start_index:start_index + count]
            start_index += count
            response += f"{field}: {', '.join(selected_people)}\n"
        bot.reply_to(message, response)


bot.polling()
