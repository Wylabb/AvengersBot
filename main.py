import importlib
from importlib import reload

import id
import json
import telebot

global st
global d
importlib.reload(id)

bot = telebot.TeleBot('5293957385:AAGXrcOkHhcgQXGXkMzitKUcDUI4jDPcd-o')

"""ХУЙНЯ ЕБУЧАЯ"""


def get_user_id(m, ):
    return str(m.from_user.id)


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

"""МОДУЛЬ ФУНКЦИЙ КЭШ"""


def cache_f(m, ):
    return 'cache_' + get_user_id(m)


def create_cache(m, ):
    if cache_f(m) not in globals():
        globals()[cache_f(m)] = 0


def edit_cache(m, value, ):
    cache_n = cache_f(m)
    value = "'" + value + "'"
    exec(cache_n + ' = ' + str(value), globals())


def get_cache(m, ):
    cache_n = cache_f(m)
    result_cache = eval(cache_n)
    return result_cache


def del_cache(m, ):
    if cache_f(m) in globals():
        cache_n = cache_f(m)
        exec(cache_n + " = 0 ", globals())


def cache_f1(m, ):
    return 'cache1_' + get_user_id(m)


def create_cache1(m, ):
    if cache_f1(m) not in globals():
        globals()[cache_f1(m)] = 0


def edit_cache1(m, value, ):
    cache_n1 = cache_f1(m)
    value = "'" + value + "'"
    exec(cache_n1 + ' = ' + str(value), globals())


def get_cache1(m, ):
    cache_n1 = cache_f1(m)
    result_cache1 = eval(cache_n1)
    return result_cache1


def del_cache1(m, ):
    if cache_f1(m) in globals():
        cache_n1 = cache_f1(m)
        exec(cache_n1 + " = 0 ", globals())


"""МОДУЛЬ ФУНКЦИЙ МОДЕЛЬ"""


def model_f(m, ):
    return 'model_' + get_user_id(m)


def create_model(m, ):
    if model_f(m) not in globals():
        globals()[model_f(m)] = ''


def edit_model(m, value, ):
    global d
    model_n = model_f(m)
    inf = "'" + value + "'"
    exec(model_n + ' += ' + str(inf), globals())


def edit_model_sell(m, value, key, ):
    model_n = model_f(m)
    inf = "'" + get_dict(m).get(key)[value] + "_'"
    exec(model_n + ' += ' + str(inf), globals())


def get_model(m, ):
    model_n = model_f(m)
    result_model = eval(model_n)
    return result_model


def del_model(m, ):
    if model_f(m) in globals():
        model_n = model_f(m)
        exec(model_n + " = '' ", globals())


"""МОДУЛЬ СЛОВАРЬ"""


def dict_f(m, ):
    return 'dict_' + get_user_id(m)


def create_dict(m, ):
    if dict_f(m) not in globals():
        globals()[dict_f(m)] = {'Model': [], 'Flavours': []}


def edit_dict(m, value, key, ):
    global d
    dict_n = dict_f(m)
    inf = "'" + value + "'"
    exec(dict_n + "['" + key + "'].append(" + str(inf) + ")", globals())


def get_dict(m, ):
    dict_n = dict_f(m)
    result_dict = eval(dict_n)
    return result_dict


def del_dict(m, ):
    if dict_f(m) in globals():
        dict_n = dict_f(m)
        exec(dict_n + " = {'Model':[],'Flavours':[]}", globals())


"""ОБЩИЕ ФУНКЦИИ"""


def backup():
    f = open('id.py')
    data = f.read()
    f.close()
    f = open('backup.py', 'w')
    f.write(data)
    f.close()


def genlist(line):
    c = '\n'
    for i in range(len(line)):
        k = i + 1
        c += str(k) + '. ' + line[i][:-1] + '\n'
    return c


def geninfo(line):
    c = '\n'
    for i in range(len(line)):
        line[i] = line[i].replace('_', ' ')
        k = i + 1
        c += str(k) + '. ' + line[i][16:] + '\n'
    return c


def gensell(line):
    c = '\n'
    for i in range(len(line)):
        line[i] = line[i].replace('_', ' ')
        k = i + 1
        c += str(k) + '. ' + line[i] + '\n'
    return c


def search(line):
    importlib.reload(id)
    if hasattr(id, str(line)):
        return 1
    else:
        return 0


def deepsearch(word):
    deeplist = [line for line in open('id.py') if word in line]
    for i in range(len(deeplist)):
        deeplist[i] = deeplist[i][:-1]
    if deeplist:
        return deeplist
    else:
        return ['________________Пусто_']


def getvalue(word):
    reload(id)
    var = list(word.split(sep=' '))
    var = str(var[-1])
    return int(var)


def create(line):
    f = open('id.py', 'a+')
    line = line + ' = 0\n'
    f.write(line)
    f.close()
    reload(id)


def edit(line, newvalue):
    f = open('id.py')
    data = f.read()
    oldvalue = getattr(id, line)
    data = data.replace(line + ' = ' + str(oldvalue), line + ' = ' + str(newvalue))
    f.close()
    f = open('id.py', 'w')
    f.write(data)
    f.close()


def add(line, change):
    reload(id)
    f = open('id.py')
    data = f.read()

    oldvalue = getattr(id, line)
    newvalue = oldvalue + int(change)
    data = data.replace(line + ' = ' + str(oldvalue), line + ' = ' + str(newvalue))
    f.close()
    f = open('id.py', 'w')
    f.write(data)
    f.close()


def delite(line):
    f = open('id.py')
    data = f.read()
    oldvalue = getattr(id, line)
    data = data.replace(line + ' = ' + str(oldvalue), '')
    f.close()

    f = open('id.py', 'w')
    f.write(data)
    f.close()


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
    if search(user_id_model) == 0:
        bot.reply_to(m, 'У вас нет этой модели с таким вкусом')
        return

    if int(getattr(id, user_id_model)) == int(get_cache(m)):
        bot.reply_to(m, 'Вы  продали все одноразки этой модели с рук! Сколько вы получили?')
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