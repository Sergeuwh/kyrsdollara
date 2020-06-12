import telebot
import requests
from bs4 import BeautifulSoup
import time

chet = []

banki_i_kursi_USD_buy = []
banki_i_kursi_USD_sell = []
headers = {"User-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}
full_page = requests.get("https://myfin.by/currency/usd/novopolotsk?sort=bank_name.desc", headers=headers)
soup = BeautifulSoup(full_page.content, 'html.parser')
bestt = soup.findAll("td")
all_banks = ['Абсолютбанк', 'Альфа-Банк', 'Банк БелВЭБ', 'Банк ВТБ', 'Белагропромбанк', 'Беларусбанк', 'Белгазпромбанк', 'Белинвестбанк', 'БПС-Сбербанк', 'Идея Банк', 'Паритетбанк', 'Приорбанк']


for i in range(len(bestt)):
    item = bestt[i]
    item = str(item).replace("<td>", "")
    item = str(item).replace("</td>", "")
    if len(list(item.split())) != 1:
        item = str(item).replace("<td ", "")
        item = str(item).replace('class="best">', "")
    if i == 35:
        banki_i_kursi_USD_buy.append({"Абсолютбанк": item})
    elif i == 36:
        banki_i_kursi_USD_sell.append({"Абсолютбанк": item})
    elif i == 50:
        banki_i_kursi_USD_buy.append({"Альфа-Банк": item})
    elif i == 51:
        banki_i_kursi_USD_sell.append({"Альфа-Банк": item})
    elif i == 72:
        banki_i_kursi_USD_buy.append({"Банк БелВЭБ": item})
    elif i == 73:
        banki_i_kursi_USD_sell.append({"Банк БелВЭБ": item})
    elif i == 87:
        banki_i_kursi_USD_buy.append({"Банк ВТБ": item})
    elif i == 88:
        banki_i_kursi_USD_sell.append({"Банк ВТБ": item})
    elif i == 102:
        banki_i_kursi_USD_buy.append({"Белагропромбанк": item})
    elif i == 103:
        banki_i_kursi_USD_sell.append({"Белагропромбанк": item})
    elif i == 124:
        banki_i_kursi_USD_buy.append({"Беларусбанк": item})
    elif i == 125:
        banki_i_kursi_USD_sell.append({"Беларусбанк": item})
    elif i == 195:
        banki_i_kursi_USD_buy.append({"Белгазпромбанк": item})
    elif i == 196:
        banki_i_kursi_USD_sell.append({"Белгазпромбанк": item})
    elif i == 210:
        banki_i_kursi_USD_buy.append({"Белинвестбанк": item})
    elif i == 211:
        banki_i_kursi_USD_sell.append({"Белинвестбанк": item})
    elif i == 225:
        banki_i_kursi_USD_buy.append({"БПС-Сбербанк": item})
    elif i == 226:
        banki_i_kursi_USD_sell.append({"БПС-Сбербанк": item})
    elif i == 254:
        banki_i_kursi_USD_buy.append({"Идея Банк": item})
    elif i == 255:
        banki_i_kursi_USD_sell.append({"Идея Банк": item})
    elif i == 269:
        banki_i_kursi_USD_buy.append({"Паритетбанк": item})
    elif i == 270:
        banki_i_kursi_USD_sell.append({"Паритетбанк": item})
    elif i == 284:
        banki_i_kursi_USD_buy.append({"Приорбанк": item})
    elif i == 285:
        banki_i_kursi_USD_sell.append({"Приорбанк": item})
def get_max():
    max_buy = 0.0
    max_buy_bank = ""
    for i in range(len(banki_i_kursi_USD_buy)):
        item = banki_i_kursi_USD_buy[i]
        bank = all_banks[i]
        if float(item[bank]) > float(max_buy):
            max_buy = item[bank]
            max_buy_bank = bank
    return max_buy_bank + "  " + max_buy
def get_for_ma_or_pa_sell():
    first_buy = 100.0
    second_buy = 110.0
    third_buy = 120.0
    first_buy_bank = ""
    second_buy_bank = ""
    third_buy_bank = ""
    for i in range(len(banki_i_kursi_USD_buy)):
        item = banki_i_kursi_USD_buy[i]
        bank = all_banks[i]
        if float(item[bank]) < float(first_buy) and float(item[bank]) < float(second_buy) and float(item[bank]) < float(
                third_buy):
            first_buy = item[bank]
            first_buy_bank = bank
        elif float(item[bank]) > float(first_buy) and float(item[bank]) < float(second_buy) and float(item[bank]) < float(third_buy):
            second_buy = item[bank]
            second_buy_bank = bank
        elif float(item[bank]) > float(first_buy) and float(item[bank]) > float(second_buy) and float(item[bank]) < float(third_buy):
            third_buy = item[bank]
            third_buy_bank = bank
    all = [first_buy, first_buy_bank, second_buy, second_buy_bank, third_buy, third_buy_bank]
    return all

def get_for_ma_or_pa():
    first_buy = 0.0
    second_buy = 0.0
    third_buy = 0.0
    first_buy_bank = ""
    second_buy_bank = ""
    third_buy_bank = ""
    for i in range(len(banki_i_kursi_USD_buy)):
        item = banki_i_kursi_USD_buy[i]
        bank = all_banks[i]
        if float(item[bank]) > float(first_buy) and float(item[bank]) > float(second_buy) and float(item[bank]) > float(third_buy):
            first_buy = item[bank]
            first_buy_bank = bank
        elif float(item[bank]) < float(first_buy) and float(item[bank]) > float(second_buy) and float(item[bank]) > float(third_buy):
            second_buy = item[bank]
            second_buy_bank = bank
        elif float(item[bank]) < float(first_buy) and float(item[bank]) < float(second_buy) and float(item[bank]) > float(third_buy):
            third_buy = item[bank]
            third_buy_bank = bank
    all = [first_buy, first_buy_bank, second_buy, second_buy_bank, third_buy, third_buy_bank]
    return all

def get_min():
    min_sell = 0.0
    min_sell_bank = ""
    for i in range(len(banki_i_kursi_USD_sell)):
        item = banki_i_kursi_USD_sell[i]
        bank = all_banks[i]
        if float(item[bank]) < float(min_sell) and min_sell != 0.0:
            min_sell = item[bank]
            min_sell_bank = bank
        elif min_sell == 0.0:
            min_sell = item[bank]
            min_sell_bank = bank
    return min_sell_bank + "  " + min_sell
def get_min_adres():
    min_sell = 0.0
    min_sell_bank = ""
    for i in range(len(banki_i_kursi_USD_sell)):
        item = banki_i_kursi_USD_sell[i]
        bank = all_banks[i]
        if float(item[bank]) < float(min_sell) and min_sell != 0.0:
            min_sell = item[bank]
            min_sell_bank = bank
        elif min_sell == 0.0:
            min_sell = item[bank]
            min_sell_bank = bank
    min_sell_bank = min_sell_bank
    if min_sell_bank == "Абсолютбанк":
        return "г. Новополоцк, ул. Молодежная, 7"
    elif min_sell_bank == "Альфа-банка":
        return "г. Новополоцк, ул. Калинина, 3; г. Новополоцк, ул. Молодёжная, 166"
    elif min_sell_bank == "Банк БелВЭБ":
        return "г. Новополоцк, ул. Молодежная, 169, а"
    elif min_sell_bank == "Банк ВТБ":
        return "г. Новополоцк, ул. Молодежная, 92а"
    elif min_sell_bank == "Белагропромбанк":
        return "г. Новополоцк, ул.Молодежная, 166; г. Новополоцк, ул. Кирова, 3"
    elif min_sell_bank == "Беларусбанк":
        return "г. Новополоцк, ул. Дружбы, 4; г. Новополоцк, ул. Кирова, 1; г. Новополоцк, ул. Молодежная, 144; г. Новополоцк, ул. Молодежная, 169; г. Новополоцк, ул. Молодежная, 16; г. Новополоцк, ул. Молодежная, 177а; г. Новополоцк, ул. Молодежная, 104а; г. Новополоцк, ул. Молодежная, 217; г. Новополоцк, ул. Молодежная, 162"
    elif min_sell_bank == "Белгазпромбанк":
        return "г. Новополоцк, ул. Молодежная, д. 11а"
    elif min_sell_bank == "Белинвестбанк":
        return "г. Новополоцк, ул. Молодежная, 167"
    elif min_sell_bank == "БПС-Сбербанк":
        return "г. Новополоцк, ул. Олимпийская, 11; г. Новополоцк, Центральная проходная ОАО 'Нафтан' завод 'Полимир'; г. Новополоцк, ул. Молодежная, 137; г. Новополоцк, ул. Молодежная, 137"
    elif min_sell_bank == "Идея Банк":
        return "г. Новополоцк, ул. Молодежная, 148"
    elif min_sell_bank == "Паритетбанк":
        return "г. Новополоцк, ул. Молодежная, 166А"
    elif min_sell_bank == "Приорбанк":
        return "г. Новополоцк, ул. Молодежная, 213"
def get_max_adres():
    max_buy = 0.0
    max_buy_bank = ""
    for i in range(len(banki_i_kursi_USD_buy)):
        item = banki_i_kursi_USD_buy[i]
        bank = all_banks[i]
        if float(item[bank]) > float(max_buy):
            max_buy = item[bank]
            max_buy_bank = bank
    max_buy_bank = max_buy_bank
    if max_buy_bank == "Абсолютбанк":
        return "г. Новополоцк, ул. Молодежная, 7"
    elif max_buy_bank == "Альфа-банка":
        return "г. Новополоцк, ул. Калинина, 3; г. Новополоцк, ул. Молодёжная, 166"
    elif max_buy_bank == "Банк БелВЭБ":
        return "г. Новополоцк, ул. Молодежная, 169, а"
    elif max_buy_bank == "Банк ВТБ":
        return "г. Новополоцк, ул. Молодежная, 92а"
    elif max_buy_bank == "Белагропромбанк":
        return "г. Новополоцк, ул.Молодежная, 166; г. Новополоцк, ул. Кирова, 3"
    elif max_buy_bank == "Беларусбанк":
        return "г. Новополоцк, ул. Дружбы, 4; г. Новополоцк, ул. Кирова, 1; г. Новополоцк, ул. Молодежная, 144; г. Новополоцк, ул. Молодежная, 169; г. Новополоцк, ул. Молодежная, 16; г. Новополоцк, ул. Молодежная, 177а; г. Новополоцк, ул. Молодежная, 104а; г. Новополоцк, ул. Молодежная, 217; г. Новополоцк, ул. Молодежная, 162"
    elif max_buy_bank == "Белгазпромбанк":
        return "г. Новополоцк, ул. Молодежная, д. 11а"
    elif max_buy_bank == "Белинвестбанк":
        return "г. Новополоцк, ул. Молодежная, 167"
    elif max_buy_bank == "БПС-Сбербанк":
        return "г. Новополоцк, ул. Олимпийская, 11; г. Новополоцк, Центральная проходная ОАО 'Нафтан' завод 'Полимир'; г. Новополоцк, ул. Молодежная, 137; г. Новополоцк, ул. Молодежная, 137"
    elif max_buy_bank == "Идея Банк":
        return "г. Новополоцк, ул. Молодежная, 148"
    elif max_buy_bank == "Паритетбанк":
        return "г. Новополоцк, ул. Молодежная, 166А"
    elif max_buy_bank == "Приорбанк":
        return "г. Новополоцк, ул. Молодежная, 213"

bot = telebot.TeleBot(token= token)
keyboard_main = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_main.row('Главное меню')

keyboard_vopr = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_vopr.row('Покупка доллара', 'Продажа доллара')

keyboard_yes_or_no2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_yes_or_no2.row('Интересует ', 'Главное меню')

keyboard_vopr_for_mapa = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard_vopr_for_mapa.row('Покупка доллара!', 'Продажа доллара!')
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '/start':

        bot.send_message(message.chat.id, 'Привет!')
        time.sleep(0.6)
        bot.send_message(message.chat.id, 'Я могу отправлять лучшие курсы валют в Новополоцке', reply_markup = keyboard_main)
    if message.text == 'Главное меню':
        chet.append("1")
        bot.send_message(message.chat.id, "Что вас интересует?", reply_markup = keyboard_vopr)
    if message.text == 'Покупка доллара':
        bot.send_message(message.chat.id, 'Лучший курс доллара на сегодня')
        time.sleep(0.6)
        bot.send_message(message.chat.id, get_max())
        time.sleep(0.6)
        bot.send_message(message.chat.id, "Адреса отделений- " + get_max_adres(), reply_markup = keyboard_main)
    if message.text == 'Продажа доллара':
        bot.send_message(message.chat.id, 'Лучший курс доллара на сегодня')
        time.sleep(0.6)
        bot.send_message(message.chat.id, get_min())
        time.sleep(0.6)
        bot.send_message(message.chat.id, "Адреса отделений- " + get_min_adres(), reply_markup = keyboard_main)
    if message.text == 'Мама' or message.text == 'Папа' or message.text == 'мама' or message.text == 'папа':
        bot.send_message(message.chat.id, "Выбери пожалуста то, что тебя интересует)))", reply_markup = keyboard_vopr_for_mapa)
    if message.text == 'Продажа доллара!':
        all = get_for_ma_or_pa()
        for i in range(len(all)):
            bot.send_message(message.chat.id, all[i])
            if i % 2 != 0:
                bot.send_message(message.chat.id, "###########")
        bot.send_message(message.chat.id, "В главное меню?)", reply_markup=keyboard_main)
    if message.text == 'Покупка доллара!':
        all = get_for_ma_or_pa_sell()
        for i in range(len(all)):
            bot.send_message(message.chat.id, all[i])
            if i % 2 != 0:
                bot.send_message(message.chat.id, "###########")
        bot.send_message(message.chat.id, "В главное меню?)", reply_markup = keyboard_main)
    if message.text == 'счёт':
        bot.send_message(message.chat.id, len(chet))

bot.polling(none_stop=True, interval=0)
