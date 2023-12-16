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


@recruit_bot.message_handler(func=lambda message: message.text in ["Хочу вступить",
                                                                   "Как оказать финансовую помощь?",
                                                                   "Пресс-служба РДК",
                                                                   "Назад",
                                                                   "Рус"])
def handle_rus_menu(message):
    if message.text == "Хочу вступить":
        handle_join_information(message)
    elif message.text == "Как оказать финансовую помощь?":
        handle_financial_information(message)
    elif message.text == "Пресс-служба РДК":
        handle_press_service_information(message)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Хочу вступить")
        btn_3 = types.KeyboardButton("Как оказать финансовую помощь?")
        btn_4 = types.KeyboardButton("Пресс-служба РДК")
        markup.add(btn_1, btn_3, btn_4)
        recruit_bot.send_message(message.from_user.id,
                                 "Приветствуем, в нашем боте вы можете прочесть ответы на самые популярные вопросы. Если вы не нашли вашего вопроса или ответ вас не устроил - пишите в нашу обратную связь \n@rusvolcorps",
                                 reply_markup=markup)


@recruit_bot.message_handler(
    func=lambda message: message.text in ["Я ознакомлен и готов вступить", "Ознакомится с требованиями"])
def handle_join_information(message):
    final_text = (
        "Если вы физически подготовлены (выполняете  порог вхождения), сделали все необходимые дела, собрали документы - подавайте заявку по ссылке (https://docs.google.com/forms/d/e/1FAIpQLSfLXuDOvZvlU2RZO9cuD7MSWl7l2NwMJnZNn2JdZGhze2ge3Q/viewform). "
        "С вами свяжутся с нашего официального Telegram Аккаунта - @rusvolcorps, указанный в описании Официального Telegram-канала (https://t.me/russvolcorps), как будет формироваться новый заезд. "
        "И помните- не обсуждайте ваш отъезд в РДК с кем-либо, особенно в интернете. Обратного пути в РФ грозит вам лишением свободы, здоровья и жизни. "
        "При раскрытии вашей личности к вашим близким и родственникам будет проявлено пристальное внимание спецслужб РФ.")
    if message.text == "Ознакомится с требованиями":
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
        btn_1 = types.KeyboardButton("Ознакомится с требованиями")
        btn_2 = types.KeyboardButton("Что происходит по приезду в Украину?")
        btn_3 = types.KeyboardButton("Каким образом осуществляется вступление?")
        markup.add(btn_1, btn_2, btn_3)
        recruit_bot.send_message(message.from_user.id, "Суть обращения:", parse_mode="html",
                                 reply_markup=markup)


@recruit_bot.message_handler(func=lambda message: message.text in ["Что происходит по приезду в Украину?"])
def handle_instructions_information(message):
    if message.text == "Что происходит по приезду в Украину?":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Назад")
        markup.add(btn_1)
        recruit_bot.send_photo(message.from_user.id, open('resources/training.jpg', 'rb'),
                                 "По прибытию в Украину, рекрут проходит КМБ, который длится 1 месяц. "
                                 "На КМБ дают все необходимые базовые знания, а так же проходит физическая подготовка. "
                                 "В конце курса все рекруты сдают аттестацию.", parse_mode="html", reply_markup=markup)
        time.sleep(1)
        recruit_bot.send_message(message.from_user.id,
                                 "После КМБ рекрут зачисляется в боевые группы, где у него появляется командир и в которых он продолжит свой боевой путь. "
                                 "То, в какую группу попадет рекрут, зависит от его навыков и возможности их максимально эффективного применения.",
                                 parse_mode="html")
        time.sleep(1)
        recruit_bot.send_photo(message.from_user.id, open('resources/brotherhood.jpg', 'rb'),
                               "Рекрут становится полноценным бойцом только после первого боевого выхода. "
                               "После этого, боец подает документы на оформление и заключение контракта. "
                               "А также начинает получать денежное довольствие.", parse_mode="html")


@recruit_bot.message_handler(func=lambda message: message.text in ["Каким образом осуществляется вступление?"])
def handle_documents_information(message):
    if message.text == "Каким образом осуществляется вступление?":
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
        btn_1 = types.KeyboardButton("Перевод на Банку")
        btn_2 = types.KeyboardButton("Перевод SWIFT")
        btn_3 = types.KeyboardButton("Прямой перевод на карту")
        btn_4 = types.KeyboardButton("Криптовалюты")
        btn_5 = types.KeyboardButton("Назад")
        financical_markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
        recruit_bot.send_photo(message.from_user.id, open('resources/finance.png', 'rb'),
                               caption="Благодарим вас за помощь! Помните - рубль, доллар или гривна, переведённые на благое дело сегодня - петля, накинутая на шею Путина и его сатрапов завтра!",
                               reply_markup=financical_markup)

    elif message.text == "Перевод на Банку":
        markup = types.InlineKeyboardMarkup()
        btn_donation_form = types.InlineKeyboardButton("Ссылка на банку", url="https://send.monobank.ua/jar/3vHg25YeUn")
        markup.add(btn_donation_form)
        recruit_bot.send_message(message.from_user.id, text="Переходи по ссылке!", reply_markup=markup)
    elif message.text == "Прямой перевод на карту":
        recruit_bot.send_message(message.from_user.id, "<b>Приватбанк (Карта)</b> - <pre>4731185613960753</pre>"
                                                       "\n<b>Monobank (Карта)</b> - <pre>5375414102070967</pre>",
                                 parse_mode="html")
    elif message.text == "Перевод SWIFT":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Евро")
        btn_2 = types.KeyboardButton("Доллары США")
        btn_3 = types.KeyboardButton("Назад к меню донатов")
        markup.add(btn_1, btn_2, btn_3)
        recruit_bot.send_message(message.from_user.id, "Выберите валюту", reply_markup=markup)
    elif message.text == "Евро":
        recruit_bot.send_message(message.from_user.id, "<b>BENEFICIARY (Получатель)</b>\n"
                                                       "Recipient\n"
                                                       "Чтобы узнать, писать нам в обратную связь на @rusvolcorps\n"
                                                       "IBAN\n"
                                                       "<pre>UA453052990262086400931944870</pre>\n"
                                                       "Account\n"
                                                       "<pre>5168752014069077</pre>\n\n"
                                                       "<b>BANK OF BENEFICIARY (Банк получателя)</b>\n"
                                                       "Bank\n"
                                                       "<pre>JSC CB PRIVATBANK, 1D HRUSHEVSKOHO STR., KYIV, 01001, UKRAINE</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>PBANUA2X</pre>\n\n"
                                                       "<b>CORRESPONDENT BANK (Банк-кореспондент)</b>\n"
                                                       "Bank\n"
                                                       "<pre>J.P.MORGAN AG, FRANKFURT AM MAIN, GERMANY</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>CHASDEFX</pre>\n"
                                                       "Correspondent account\n"
                                                       "<pre>623-160-5145</pre>\n", parse_mode="html")
    elif message.text == "Доллары США":
        recruit_bot.send_message(message.from_user.id, "<b>BENEFICIARY (Получатель)</b>\n"
                                                       "Recipient\n"
                                                       "Чтобы узнать, писать нам в обратную связь на @rusvolcorps\n"
                                                       "IBAN\n"
                                                       "<pre>UA453052990262086400931944870</pre>\n"
                                                       "Account\n"
                                                       "<pre>5168752014069077</pre>\n\n"
                                                       "<b>BANK OF BENEFICIARY (Банк получателя)</b>\n"
                                                       "Bank\n"
                                                       "<pre>JSC CB PRIVATBANK, 1D HRUSHEVSKOHO STR., KYIV, 01001, UKRAINE</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>PBANUA2X</pre>\n\n"
                                                       "<b>CORRESPONDENT BANK (Банк-кореспондент)</b>\n"
                                                       "Bank\n"
                                                       "<pre>Citibank N.A., NEW YORK, USA</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>CITIUS33</pre>\n"
                                                       "Correspondent account\n"
                                                       "<pre>36445343</pre>\n", parse_mode="html")
    elif message.text == "Криптовалюты" or message.text == "Cryptocurrency":
        recruit_bot.send_message(message.from_user.id,
                                 "<b>Bitcoin</b>\n<pre>bc1qpyaw5a4xpgrmvhvwtelx6xd3z5cxkapcdn7tty</pre>\n"
                                 "\n<b>Solana</b>\n<pre>FhyVtG9Q8agfV9pX5LheUNBzycFUTcVzcheynW4hTije</pre>\n"
                                 "\n<b>Ethereum</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                 "\n<b>USDT (BNB Smart Chain)</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                 "\n<b>BNB</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                 "\n<b>BUSD (BNB Smart Chain)</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                 "\n<b>Cardano</b>\n<pre>addr1q9zpwctvhalyz0wtmvc73j97p2q2daksek5hndeuxstkadjyzaske0m7gy7uhke3arytuz5q5mmdpndf0xmncdqhd6mqyw04k2</pre>\n"
                                 "\n<b>Monero</b>\n<pre>45HrLZN7sX5W4uAUFhasJhUKaPTV9ymXi4L3wEf7NqmM7eCsYaEti39QMdPDGZcacChWJRiMYapfQj6wjtsCa3r47JzGV7u</pre>\n"

                                 , parse_mode="html")


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
