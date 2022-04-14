import importlib
from importlib import reload

import id
import json

from AvengersModule import get_user_id, create_cache, edit_cache, get_cache, del_cache, create_cache1, edit_cache1, \
    get_cache1, del_cache1, create_model, edit_model, edit_model_sell, get_model, del_model, create_dict, edit_dict, \
    get_dict, del_dict
from FunctionsModule import backup, genlist, geninfo, gensell, search, deepsearch, getvalue, create, edit, add, delite
from bot_password import bot

global st
global d
importlib.reload(id)

"""СЛОВАРЬ СТОРЕДЖ И ДИКТ"""


def json_save_d():
    with open('dict.json', 'w') as fp:
        json.dump(d, fp)


def json_load_d():
    global d
    with open('dict.json', 'r') as fp:
        d = json.load(fp)


def json_save_st():
    with open('storage.json', 'w') as fp:
        json.dump(st, fp)


def json_load_st():
    global st
    with open('storage.json', 'r') as fp:
        st = json.load(fp)


json_load_d()
json_load_st()

"""Команды!!!!"""


@bot.message_handler(commands=["start"])
def start_cm(m, ):
    user_id = str(m.from_user.id)
    line = 'id_' + user_id
    change = ' = ' + user_id + '\n'
    f = open('id.py', 'a+')
    if search(line) == 0:
        f.write(line + change)
        bot.send_message(m.chat.id, 'Отлично, добро пожаловать!')
    else:
        bot.send_message(m.chat.id, 'Вы уже являетесь пользователем бота')
    f.close()


@bot.message_handler(commands=["kiwi"])
def kiwi_cm(m, ):
    kiwi_str = '/info - выведет вашу личную статистику \n/take - взять одноразки на руки \n/sell - если продали ' \
               'одноразку \n/stats - обшая статистика \n '
    bot.send_message(m.chat.id, kiwi_str)


@bot.message_handler(commands=["info"])
def info_cm(m, ):
    user_id = get_user_id(m)
    word = 'hands_' + user_id
    inventory = geninfo(deepsearch(word))
    count = 0
    for i in range(len(deepsearch(word))):
        count += getvalue(deepsearch(word)[i])
    bot.send_message(m.chat.id, 'Все, что у вас на руках: \n' + inventory + '\nВсего на руках: ' + str(count))


@bot.message_handler(commands=["stats"])
def stats_cm(m, ):
    user_id = get_user_id(m)
    word = 'hands_' + user_id
    bot.send_message(m.chat.id, geninfo(deepsearch(word)))


@bot.message_handler(commands=["storage"])
def storage_cb(m, ):
    del_model(m)

    line = d.get('Model')
    msg = bot.reply_to(m, 'Введите название модели \n' + genlist(line))
    bot.register_next_step_handler(msg, storage_model)


def storage_model(m, ):
    global d
    create_cache(m)
    edit_cache(m, m.text)
    if (get_cache(m).isdigit() is False) or (int(get_cache(m)) > len(d.get('Model'))) or (int(get_cache(m)) == 0):
        bot.reply_to(m, 'Неправильный номер модели')
        del_cache(m)
        del_cache1(m)
        return

    st[d.get('Model')[int(get_cache(m)) - 1]] = {}
    json_save_st()
    line = d.get('Flavours')

    msg = bot.reply_to(m, 'введите номер вкуса\n' + genlist(line))
    bot.register_next_step_handler(msg, storage_flavours)


def storage_flavours(m, ):
    global d
    create_cache1(m)
    edit_cache1(m, m.text)
    if (get_cache1(m).isdigit() is False) or (int(get_cache1(m)) > len(d.get('Flavours'))) or (int(get_cache1(m)) == 0):
        bot.reply_to(m, 'Неправильный номер вкуса')
        del_cache(m)
        del_cache1(m)
        return

    st[d.get('Model')[int(get_cache(m)) - 1]][d.get('Flavours')[int(get_cache1(m)) - 1]] = 0
    json_save_st()

    msg = bot.reply_to(m, 'Введите колличество взятых одноразок:')
    bot.register_next_step_handler(msg, storage_amount)


def storage_amount(m, ):
    model_st = d.get('Model')[int(get_cache(m)) - 1]
    edit_cache(m, m.text)

    if get_cache(m).isdigit() is False:
        bot.reply_to(m, 'Неправильное число:')
        del_cache(m)
        del_cache1(m)
        return
    if int(get_cache(m)) == 0:
        del st[model_st]
        json_save_st()
    else:
        st[model_st][d.get('Flavours')[int(get_cache1(m)) - 1]] = int(get_cache(m))
    json_save_st()
    bot.reply_to(m, 'Количество одноразок этой модели изменено на  ' + get_cache(m) + 'шт.')

    del_model(m)


@bot.message_handler(commands=["take"])
def take_cb(m, ):
    del_model(m)
    line = list(st.keys())
    print(line)
    msg = bot.reply_to(m, 'Введите название модели \n' + genlist(line))
    bot.register_next_step_handler(msg, model)


def model(m, ):
    create_cache(m)
    edit_cache(m, m.text)
    create_model(m)
    line = list(st.keys())
    if (get_cache(m).isdigit() is False) or (int(get_cache(m)) > len(line)) or (int(get_cache(m)) == 0):
        bot.reply_to(m, 'Неправильный номер модели')
        del_cache(m)
        del_model(m)
        return

    edit_model(m, line[int(get_cache(m)) - 1])
    edit_cache(m, line[int(get_cache(m)) - 1])
    line = list(st[get_cache(m)].keys())
    msg = bot.reply_to(m, 'введите номер вкуса\n' + genlist(line))

    bot.register_next_step_handler(msg, flavours)


def flavours(m, ):
    create_cache1(m)
    edit_cache1(m, m.text)
    line = list(st[get_cache(m)].keys())
    print(line)
    if (get_cache1(m).isdigit() is False) or (int(get_cache1(m)) > len(line)) or (int(get_cache1(m)) == 0):
        bot.reply_to(m, 'Неправильный номер вкуса')
        del_cache(m)
        del_cache1(m)
        del_model(m)
        return

    edit_model(m, line[int(get_cache1(m)) - 1])
    edit_cache1(m, line[int(get_cache1(m)) - 1])

    msg = bot.reply_to(m, 'Введите колличество взятых одноразок:')
    bot.register_next_step_handler(msg, amount)


def amount(m, ):
    print(get_cache(m), get_cache1(m), get_model(m))
    Model = get_cache(m)
    Flavour = get_cache1(m)
    edit_cache(m, m.text)
    if get_cache(m).isdigit() is False or (int(get_cache(m)) == 0):
        bot.reply_to(m, 'Неправильное число:')
        del_cache(m)
        del_cache1(m)
        del_model(m)
        return

    if st[Model][Flavour] == int(get_cache(m)):
        del st[Model]
        json_save_st()
    elif st[Model][Flavour] < int(get_cache(m)):
        bot.reply_to(m, 'Вы просите больше, чем есть на складе!')
        del_cache(m)
        del_cache1(m)
        del_model(m)
        return
    else:
        st[Model][Flavour] -= int(get_cache(m))
        json_save_st()

    user_id_ = 'hands_' + get_user_id(m) + '_'
    user_id_model = user_id_ + get_model(m)
    if search(user_id_model) == 1:
        add(user_id_model, get_cache(m))
    else:
        create(user_id_model)
        edit(user_id_model, get_cache(m))

    bot.reply_to(m, 'вы взяли ' + get_cache(m) + ' одноразок на руки!')


@bot.message_handler(commands=["sell"])
def sell_cb(m, ):
    del_model(m)
    del_dict(m)
    create_dict(m)

    user_id = get_user_id(m)
    hands = 'hands_' + user_id
    info = deepsearch(hands)
    s = []

    for i in range(len(info)):
        c = info[i].split(sep='_')
        for j in range(2, len(c) - 1):
            s.append(c[j])
    s = list(set(s))
    for i in range(len(s)):
        if s[i] in str(d.get('Model')):
            edit_dict(m, s[i], 'Model')
        if s[i] in str(d.get('Flavours')):
            edit_dict(m, s[i], 'Flavours')

    s_brand(m)


def s_brand(m, ):
    line = get_dict(m).get('Model')
    msg = bot.reply_to(m, 'Введите название модели: \n' + gensell(line))

    create_model(m)
    del_cache(m)
    bot.register_next_step_handler(msg, s_model)


def s_model(m, ):
    create_cache(m)
    edit_cache(m, m.text)

    if (get_cache(m).isdigit() is False) or int(get_cache(m)) > len(get_dict(m).get('Model')) or int(get_cache(m)) == 0:
        bot.reply_to(m, 'Неправильный номер модели')
        del_cache(m)
        del_model(m)
        return

    edit_model_sell(m, int(get_cache(m)) - 1, 'Model')
    del_cache(m)

    line = get_dict(m).get('Flavours')
    msg = bot.reply_to(m, 'Введите номер вкуса:\n' + gensell(line))
    bot.register_next_step_handler(msg, s_flavours)


def s_flavours(m, ):
    global d
    create_cache(m)
    edit_cache(m, m.text)

    if (get_cache(m).isdigit() is False) or (int(get_cache(m)) > len(get_dict(m).get('Flavours'))):
        bot.reply_to(m, 'Неправильный номер вкуса')
        del_cache(m)
        del_model(m)
        return

    edit_model_sell(m, int(get_cache(m)) - 1, 'Flavours')

    del_cache(m)
    msg = bot.reply_to(m, 'Введите колличество проданных одноразок:')
    bot.register_next_step_handler(msg, s_amount)


def s_amount(m, ):
    create_cache(m)
    edit_cache(m, m.text)
    del_dict(m)
    if get_cache(m).isdigit() is False:
        bot.reply_to(m, 'Неправильное число:')
        del_cache(m)
        del_model(m)
        return

    user_id_ = 'hands_' + get_user_id(m) + '_'
    user_id_model = user_id_ + get_model(m)
    importlib.reload(id)
    if search(user_id_model) == 0:
        bot.reply_to(m, 'У вас нет этой модели с таким вкусом')
        return

    if int(getattr(id, user_id_model)) == int(get_cache(m)):
        msg = bot.reply_to(m, 'Вы  продали все одноразки этой модели с рук! Сколько вы получили?')
        delite(user_id_model)
        reload(id)
    elif int(getattr(id, user_id_model)) < int(get_cache(m)):
        bot.reply_to(m, 'У вас нет столько одноразок этой модели')
        return
    else:
        add(user_id_model, -int(get_cache(m)))
    msg = bot.reply_to(m, 'Сколько вы получили с ' + get_cache(m) + ' одноразок этой модели?')

    user_id_sell = 'sell_' + get_user_id(m) + '_'
    user_id_sell_model = user_id_sell + get_model(m)

    if search(user_id_sell_model) == 1:
        add(user_id_sell_model, get_cache(m))
    else:
        create(user_id_sell_model)
        edit(user_id_sell_model, get_cache(m))

    bot.register_next_step_handler(msg, s_money)


def s_money(m, ):
    create_cache(m)
    edit_cache(m, m.text)
    del_dict(m)
    if get_cache(m).isdigit() is False:
        msg = bot.reply_to(m, 'Неправильное число, повторите')
        del_cache(m)
        bot.register_next_step_handler(msg, s_money)
        return

    user_id_money = 'money_' + get_user_id(m) + '_'
    user_id_money_model = user_id_money + get_model(m)

    if search(user_id_money_model) == 1:
        add(user_id_money_model, get_cache(m))
        del_model(m)
    else:
        create(user_id_money_model)
        edit(user_id_money_model, get_cache(m))
        del_model(m)

    bot.reply_to(m, 'Вы пополнили казну мстителей на ' + get_cache(m) + 'руб. Поздравляем!')


backup()
bot.polling(none_stop=True, interval=0)
