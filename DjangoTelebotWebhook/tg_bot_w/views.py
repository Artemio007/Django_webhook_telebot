from telebot import TeleBot, types
from rest_framework.response import Response
from rest_framework.views import APIView
from DjangoTelebotWebhook.settings import BOT_TOKEN, NGROK_URL
from django.http import HttpResponse
import psycopg2
from django.conf import settings


bot = TeleBot(BOT_TOKEN)

start_count = 0


class UpdateBot(APIView):
    def post(self, request):
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return Response({'code': 200})


@bot.message_handler(commands=['start'])
def phone(message):
    global start_count
    print(start_count)
    if not start_count:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        button_phone = types.KeyboardButton(text="Отправить телефон", request_contact=True)
        keyboard.add(button_phone)
        bot.send_message(message.chat.id, f"Привет {message.chat.first_name}, а дай номер.", reply_markup=keyboard)
        start_count += 1
    elif start_count in range(1, 6):
        bot.send_message(message.chat.id, f"{message.chat.first_name}, мы уже здоровались.")
        start_count += 1
    elif start_count in range(6, 11):
        bot.send_message(message.chat.id, f"{message.chat.first_name}, перестань пожалуйста.")
        start_count += 1
    else:
        bot.send_message(message.chat.id, f"{message.chat.first_name}, если хочешь начать заново введи: /repeat")


@bot.message_handler(commands=['repeat'])
def rep(message):
    global start_count
    start_count = 0
    phone(message)


@bot.message_handler(content_types=['contact'])
def contact(message):
    if message.contact is not None:
        bot.send_message(message.chat.id, "Спасибо, я получил твой номер телефона :)",
                         reply_markup=types.ReplyKeyboardRemove())
        your_view(message.contact)


def your_view(json_response):

    conn = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )

    cursor = conn.cursor()

    try:
        print(json_response.first_name)
        cursor.execute("INSERT INTO user_db (first_name, last_name, user_id, phone_number, vcard) "
                       "VALUES (%s, %s, %s, %s, %s)", (json_response.first_name,
                                                       json_response.last_name, json_response.user_id,
                                                       json_response.phone_number, json_response.vcard))
        conn.commit()
        cursor.close()
        conn.close()
        print("Данные успешно сохранены в таблицу PostgreSQL.")
    except psycopg2.Error as err:
        print("Ошибка при выполнении запроса:", err)
    except Exception as err:
        print(err)

    return HttpResponse('Данные успешно сохранены в таблицу PostgreSQL.')


bot.set_webhook(url=NGROK_URL)

