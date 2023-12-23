import time

import telebot
import os
from dotenv import load_dotenv
from telebot import types

import datetime
from functools import wraps

load_dotenv("resources/.env")
recruit_bot = telebot.TeleBot(os.getenv("TOKEN"))


@recruit_bot.message_handler(commands=['start'])
def start(message):
    handle_rus_menu(message)


@recruit_bot.message_handler(func=lambda message: message.text in ["Я хочу вступить",
                                                                   "Как оказать финансовую помощь?",
                                                                   "Пресс-служба РДК",
                                                                   "Назад",
                                                                   "Рус"])
def handle_rus_menu(message):
    if message.text == "Я хочу вступить":
        handle_join_information(message)
    elif message.text == "Как оказать финансовую помощь?":
        handle_financial_information(message)
    elif message.text == "Пресс-служба РДК":
        handle_press_service_information(message)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Я хочу вступить")
        btn_3 = types.KeyboardButton("Как оказать финансовую помощь?")
        btn_4 = types.KeyboardButton("Пресс-служба РДК")
        markup.add(btn_1, btn_3, btn_4)
        recruit_bot.send_message(message.from_user.id,
                                 "Приветствуем, в нашем боте вы можете прочесть ответы на самые популярные вопросы. Если вы не нашли вашего вопроса или ответ вас не устроил - пишите в нашу обратную связь \n@rusvolcorps",
                                 reply_markup=markup)


@recruit_bot.message_handler(
    func=lambda message: message.text in ["Я ознакомлен и готов вступить", "Оставить заявку / требования к кандидату"])
def handle_join_information(message):
    final_text = (
        "Если вы физически подготовлены (выполняете  порог вхождения), сделали все необходимые дела, собрали документы - подавайте заявку по ссылке (https://docs.google.com/forms/d/e/1FAIpQLSfLXuDOvZvlU2RZO9cuD7MSWl7l2NwMJnZNn2JdZGhze2ge3Q/viewform). "
        "С вами свяжутся с нашего официального Telegram Аккаунта - @rusvolcorps, указанный в описании Официального Telegram-канала (https://t.me/russvolcorps), как будет формироваться новый заезд. "
        "И помните- не обсуждайте ваш отъезд в РДК с кем-либо, особенно в интернете. Обратного пути в РФ грозит вам лишением свободы, здоровья и жизни. "
        "При раскрытии вашей личности к вашим близким и родственникам будет проявлено пристальное внимание спецслужб РФ.")
    if message.text == "Оставить заявку / требования к кандидату":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Я ознакомлен и готов вступить")
        btn_2 = types.KeyboardButton("Назад")
        markup.add(btn_1, btn_2)
        recruit_bot.send_message(message.from_user.id, "Требования к кандидатам\n"
                                                       "Возраст от 18 до 45 лет, стрессоустойчивость, отсутствие вредных привычек в виде алкогольной или наркотической зависимостей."
                                                       "Приоритет отдается тем, кто осуществлял партизанскую деятельность в России, имеет опыт ведения боевых действия или службы в армии.\n\n"

                                                       "Оптимальные физические показатели\n"
                                                       "Отжимания — 60 раз за 2 минуты\n"
                                                       "Пресс — 60 раз за 2 минуты\n Подтягивания — 10 раз\n"
                                                       "Бег — 3,5 км за 15 минут.\n\n"

                                                       "Более подробно можно ознакомиться - здесь (https://rusvolcorps.notion.site/rusvolcorps/737526a604f04ab295ebbb090476a05b)",
                                 parse_mode="html", reply_markup=markup)
    elif message.text == "Я ознакомлен и готов вступить":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Назад")
        markup.add(btn_1)
        recruit_bot.send_message(message.from_user.id, final_text, reply_markup=markup)

    else:
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Оставить заявку / требования к кандидату")
        btn_2 = types.KeyboardButton("Что необходимо сделать до отъезда, необходимые документы")
        markup.add(btn_1, btn_2)
        recruit_bot.send_message(message.from_user.id, "Суть обращения:", parse_mode="html",
                                 reply_markup=markup)


@recruit_bot.message_handler(func=lambda message: message.text in ["Что необходимо сделать до отъезда, необходимые документы"])
def handle_documents_information(message):
    if message.text == "Что необходимо сделать до отъезда, необходимые документы":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Назад")
        markup.add(btn_1)
        recruit_bot.send_message(message.from_user.id,
                                 "<b>Для того, чтобы вступить в наше подразделение, вам необходимо будет выехать в любые третьи страны, иметь при себе пакет документов в виде.</b>\n\n"
                                 "- Внутренний российский паспорт (желательно)\n"
                                 "- Заграничный российский паспорт\n"
                                 "- Свидетельство о рождении (желательно)\n"
                                 "- Документы об образовании (желательно)\n"
                                 "- Военный билет \ приписное (желательно)\n"
                                 "- Водительские права (желательно, если есть)\n\n"
                                 "<b>Если у вас есть время, то рекомендуем вам сделать:</b>\n\n"
                                 "- Генеральную доверенность на близкого человека, которому вы доверяете."
                                 "Подробно, как оформить генеральную доверенность - здесь (https://relocation.guide/c5f2e7c0f970422298638ab209cec7a7)\n"
                                 "- Либо же оформить имущественную доверенность с правом передачи.\n"
                                 "- Если у вас есть основания для репатриации - узнайте какие документы нужны.\n"
                                 "- Сделать второй загранпаспорт - на случай утери и прочих непредвиденных обстоятельств. Любой гражданин РФ может одновременно иметь два заграничных паспорта.",
                                 parse_mode="html", reply_markup=markup)


@recruit_bot.message_handler()
def handle_financial_information(message):
    if message.text == "Как оказать финансовую помощь?" or message.text == "Назад к меню донатов":
        financical_markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Назад")
        financical_markup.add(btn_1)
        recruit_bot.send_photo(message.from_user.id, open('resources/finance.png', 'rb'),
                               caption="<b>Финансовая помощь</b>\n"
                                       "Все официальные реквизиты для помощь Русскому Добровольческому Корпусу вы найдете ниже <a href='https://rusvolcorps.notion.site/ea0c14c7f92841c68887ac64d8d4bd80?pvs=4'><b>по ссылке</b></a>.\n\n"
                                       "Если вы хотите совершить перевод по IBAN — напишите нам в аккаунт @rusvolcorps, чтобы мы выдали вам все актуальные  данные.",
                               reply_markup=financical_markup, parse_mode="HTML")




@recruit_bot.message_handler(func=lambda message: message.text in ["Пресс-служба РДК"])
def handle_press_service_information(message):
    markup = types.ReplyKeyboardMarkup(row_width=1)
    btn_1 = types.KeyboardButton("Назад")
    markup.add(btn_1)
    recruit_bot.send_message(message.from_user.id, "Пресс-служба\n\n"
                                                   "Для общения с Пресс-службой у нас создан отдельный аккаунт \n"
                                                   "@rdkpress \n\n"
                                                   "При обращении необходимо сообщить и предоставить: \n"
                                                   "1) Название СМИ или иного медиаресурса; \n"
                                                   "2) Формат предлагаемого интервью: видео под запись/текст/прямой эфир и т.д. \n"
                                                   "3) Пул вопросов в текстовом виде. \n"
                                                   "4) Удостоверение журналиста и аккредитация. \n\n"
                                                   "По иным вопросам: \n"
                                                   "@rusvolcorps", reply_markup=markup)


while True:
    try:
        print("Bot is running")
        recruit_bot.polling(none_stop=True)
    except:
        continue
    recruit_bot.polling(none_stop=True)
