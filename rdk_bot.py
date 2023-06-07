import telebot
import os
from dotenv import load_dotenv
from telebot import types
import datetime

load_dotenv("resources/.env")
recruit_bot = telebot.TeleBot(os.getenv("TOKEN"))


def go_to_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    key_rus = types.KeyboardButton(text="Рус")
    markup.add(key_rus)
    key_eng = types.KeyboardButton(text="Eng")
    markup.add(key_eng)
    recruit_bot.send_message(message.from_user.id, "Выберите язык/Select the language", reply_markup=markup)


@recruit_bot.message_handler(commands=['start'])
def start(message):
    go_to_start(message)

@recruit_bot.message_handler(content_types=['text'])
def choice_handler(message):
    if message.text == "Рус" or message.text == "Назад":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Как вступить?")
        # btn_2 = types.KeyboardButton("Как помочь?")
        btn_3 = types.KeyboardButton("Как оказать финансовую помощь?")
        btn_4 = types.KeyboardButton("Пресс-служба РДК")
        markup.add(btn_1, btn_3, btn_4)
        recruit_bot.send_message(message.from_user.id, "Приветствуем, в нашем боте вы можете прочесть ответы на самые популярные вопросы. Если вы не нашли вашего вопроса или ответ вас не устроил - пишите в нашу обратную связь \n@rusvolcorps", reply_markup=markup)
    elif message.text == "Как вступить?":
        recruit_bot.send_message(message.from_user.id, "<b>Русский Добровольческий Корпус</b> - это национальное подразделение и принимает этнических русских вне зависимости от гражданства.\n\n"
                                                       "В данный момент, мы можем принять:\n"
                                                       "- Граждан РФ/РБ, которые находятся в Украине либо в странах ЕС.\n"
                                                       "- Граждан других стран, имеющих возможность въехать в страны ЕС/Украину самостоятельно.\n\n"
                                                       "Если вы попадаете под одну из категорий заполните анкету - (<a href='https://forms.gle/Q5FwRzoubyf86QUu9'>линк</a>)\n\n"
                                                       "Желающим вступить в наши ряды, которые в данный момент находятся непосредственно в Российской Федерации/Республике Беларусь, необходимо сначала самостоятельно покинуть территорию РФ/РБ.\n\n"
                                                       "Мы не оказываем никакого организационного содействия вам до момента вашего прибытия в страны ЕС.\n\n"
                                                       "Если вы не нашли ответа на свой вопрос - пишите в нашу обратную связь @rusvolcorps", parse_mode="html")
    # elif message.text == "Как помочь?":
    #     recruit_bot.send_message(message.from_user.id, "алгоритм помощи")
    elif message.text == "Как оказать финансовую помощь?" or message.text == "Назад к меню донатов":
        financical_markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Перевод на Банку")
        btn_2 = types.KeyboardButton("Перевод SWIFT")
        btn_3 = types.KeyboardButton("Прямой перевод на карту")
        btn_4 = types.KeyboardButton("Криптовалюты")
        btn_5 = types.KeyboardButton("Назад")
        financical_markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
        recruit_bot.send_photo(message.from_user.id, open('resources/finance.png', 'rb'), caption="Благодарим вас за помощь! Помните - рубль, доллар или гривна, переведённые на благое дело сегодня - петля, накинутая на шею Путина и его сатрапов завтра!", reply_markup=financical_markup)
    elif message.text == "Перевод на Банку":
        markup = types.InlineKeyboardMarkup()
        btn_donation_form = types.InlineKeyboardButton("Ссылка на банку", url="https://send.monobank.ua/jar/3vHg25YeUn")
        markup.add(btn_donation_form)
        recruit_bot.send_message(message.from_user.id, text="Переходи по ссылке!", reply_markup=markup)
    elif message.text == "Прямой перевод на карту":
        recruit_bot.send_message(message.from_user.id, "<b>Приватбанк (Карта)</b> - <pre>4731185613960753</pre>"
                                                       "\n<b>Monobank (Карта)</b> - <pre>5375411507022700</pre>", parse_mode="html")
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
        recruit_bot.send_message(message.from_user.id, "<b>Bitcoin</b>\n<pre>bc1qpyaw5a4xpgrmvhvwtelx6xd3z5cxkapcdn7tty</pre>\n"
                                                       "\n<b>Solana</b>\n<pre>FhyVtG9Q8agfV9pX5LheUNBzycFUTcVzcheynW4hTije</pre>\n"
                                                       "\n<b>Ethereum</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                                       "\n<b>USDT (BNB Smart Chain)</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                                       "\n<b>BNB</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                                       "\n<b>BUSD (BNB Smart Chain)</b>\n<pre>0x0204C039DE6d13ACe6F873484D0D9A71BFBACA06</pre>\n"
                                                       "\n<b>Cardano</b>\n<pre>addr1q9zpwctvhalyz0wtmvc73j97p2q2daksek5hndeuxstkadjyzaske0m7gy7uhke3arytuz5q5mmdpndf0xmncdqhd6mqyw04k2</pre>\n"
                                                       "\n<b>Monero</b>\n<pre>45HrLZN7sX5W4uAUFhasJhUKaPTV9ymXi4L3wEf7NqmM7eCsYaEti39QMdPDGZcacChWJRiMYapfQj6wjtsCa3r47JzGV7u</pre>\n"

                                 , parse_mode="html")
    elif message.text == "Пресс-служба РДК":
        recruit_bot.send_message(message.from_user.id, "Пресс-служба\n\n"
                                                       "Для общения с Пресс-службой у нас создан отдельный аккаунт \n"
                                                       "@rdksupport \n\n"
                                                       "При обращении необходимо сообщить и предоставить: \n"
                                                       "1) Название СМИ или иного медиаресурса; \n"
                                                       "2) Формат предлагаемого интервью: видео под запись/текст/прямой эфир и т.д. \n"
                                                       "3) Пул вопросов в текстовом виде. \n"
                                                       "4) Удостоверение журналиста и аккредитация. \n\n"
                                                       "По иным вопросам: \n"
                                                       "@rusvolcorps")
    elif message.text == "Eng" or message.text == "Back":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("How to join?")
        # btn_2 = types.KeyboardButton("How to help?")
        btn_3 = types.KeyboardButton("Donations")
        btn_4 = types.KeyboardButton("Press service RVC")
        markup.add(btn_1, btn_3, btn_4)
        recruit_bot.send_message(message.from_user.id, "Welcome, in our bot you can read the answers to the most popular questions. If you did not find your question or the answer did not suit you - write to our feedback chat \n@rusvolcorps", reply_markup=markup)
    elif message.text == "How to join?":
        recruit_bot.send_message(message.from_user.id,
                                 "<b>The Russian Volunteer Corps</b> is a national unit and accepts ethnic Russians regardless of citizenship.\n\n"
                                 "At the moment we can accept:\n"
                                 "- Citizens of the Russian Federation/Belarus who are in Ukraine or in the EU countries.\n"
                                 "- Citizens of other countries who have the opportunity to enter the EU/Ukraine on their own.\n\n"
                                 "If you fall under one of the categories fill out the questionnaire - (<a href='https://forms.gle/Q5FwRzoubyf86QUu9'>link</a>)\n\n"
                                 "Those wishing to join our ranks, which are located in the Russian Federation/Republic of Belarus, need to travel to the EU countries, and then fill out the form (<a href='https://forms.gle/Q5FwRzoubyf86QUu9'>link</a>).\n\n"
                                 "We are not able to provide any assistance in leaving the Russian Federation / Belarus.\n\n"
                                 "If you did not find the answer to your question - write to our feedback @rusvolcorps",
                                 parse_mode="html")
    elif message.text == "Donations" or message.text == "Back to donations":
        financical_markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Transfer to the jar (Monobank)")
        btn_2 = types.KeyboardButton("SWIFT transfer")
        btn_3 = types.KeyboardButton("Credit card transfer")
        btn_4 = types.KeyboardButton("Cryptocurrency")
        btn_5 = types.KeyboardButton("Back")
        financical_markup.add(btn_1, btn_2, btn_3, btn_4, btn_5)
        recruit_bot.send_photo(message.from_user.id, open('resources/finance.png', 'rb'),
                               caption="Remember - the ruble, dollar or hryvnia, transferred to a good cause today - a noose thrown around the neck of Putin and his satraps tomorrow!",
                               reply_markup=financical_markup)
    elif message.text == "Transfer to the jar (Monobank)":
        markup = types.InlineKeyboardMarkup()
        btn_donation_form = types.InlineKeyboardButton("Jar link", url="https://send.monobank.ua/jar/3vHg25YeUn")
        markup.add(btn_donation_form)
        recruit_bot.send_message(message.from_user.id, text="Follow the link!", reply_markup=markup)
    elif message.text == "SWIFT transfer":
        markup = types.ReplyKeyboardMarkup(row_width=1)
        btn_1 = types.KeyboardButton("Euro")
        btn_2 = types.KeyboardButton("Dollar")
        btn_3 = types.KeyboardButton("Back to donations")
        markup.add(btn_1, btn_2, btn_3)
        recruit_bot.send_message(message.from_user.id, "Select currency", reply_markup=markup)
    elif message.text == "Euro":
        recruit_bot.send_message(message.from_user.id, "<b>BENEFICIARY</b>\n"
                                                       "Recipient\n"
                                                       "To find out the recipient, write to us in feedback at @rusvolcorps\n"
                                                       "IBAN\n"
                                                       "<pre>UA453052990262086400931944870</pre>\n"
                                                       "Account\n"
                                                       "<pre>5168752014069077</pre>\n\n"
                                                       "<b>BANK OF BENEFICIARY</b>\n"
                                                       "Bank\n"
                                                       "<pre>JSC CB PRIVATBANK, 1D HRUSHEVSKOHO STR., KYIV, 01001, UKRAINE</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>PBANUA2X</pre>\n\n"
                                                       "<b>CORRESPONDENT BANK</b>\n"
                                                       "Bank\n"
                                                       "<pre>J.P.MORGAN AG, FRANKFURT AM MAIN, GERMANY</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>CHASDEFX</pre>\n"
                                                       "Correspondent account\n"
                                                       "<pre>623-160-5145</pre>\n", parse_mode="html")
    elif message.text == "Dollar":
        recruit_bot.send_message(message.from_user.id, "<b>BENEFICIARY</b>\n"
                                                       "Recipient\n"
                                                       "To find out the recipient, write to us in feedback at @rusvolcorps\n"
                                                       "IBAN\n"
                                                       "<pre>UA453052990262086400931944870</pre>\n"
                                                       "Account\n"
                                                       "<pre>5168752014069077</pre>\n\n"
                                                       "<b>BANK OF BENEFICIARY</b>\n"
                                                       "Bank\n"
                                                       "<pre>JSC CB PRIVATBANK, 1D HRUSHEVSKOHO STR., KYIV, 01001, UKRAINE</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>PBANUA2X</pre>\n\n"
                                                       "<b>CORRESPONDENT BANK</b>\n"
                                                       "Bank\n"
                                                       "<pre>Citibank N.A., NEW YORK, USA</pre>\n"
                                                       "SWIFT CODE/BIC\n"
                                                       "<pre>CITIUS33</pre>\n"
                                                       "Correspondent account\n"
                                                       "<pre>36445343</pre>\n", parse_mode="html")
    elif message.text == "Credit card transfer":
        recruit_bot.send_message(message.from_user.id, "<b>Privatbank</b> - <pre>4731185613960753</pre>"
                                                       "\n<b>Monobank</b> - <pre>5375411507022700</pre>",
                                 parse_mode="html")
    elif message.text == "Press service RVC":
        recruit_bot.send_message(message.from_user.id, "Press service\n\n"
                                                       "To communicate with the Press Service, we have created a separate account \n"
                                                       "@rdksupport \n\n"
                                                       "When applying, you must report and provide: \n"
                                                       "1) The name of the mass media or other media resource; \n"
                                                       "2) The format of the proposed interview: video for recording / text / live broadcast, etc. \n"
                                                       "3) A pool of questions in text form. \n"
                                                       "4) Journalist's license and accreditation. \n\n"
                                                       "For other questions: \n"
                                                       "@rusvolcorps")







while True:
    try:
        print("Bot is running")
        recruit_bot.polling(none_stop=True)
    except:
        continue
    recruit_bot.polling(none_stop=True)