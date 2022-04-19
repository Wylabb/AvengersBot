import json

import requests

from AvengersModule import get_user_id, create_cache, edit_cache, get_cache, del_cache, create_cache1, edit_cache1, \
    get_cache1, del_cache1, create_model, edit_model, get_model, del_model, get_person_id, \
    del_dict
from FunctionsModule import backup, genlist, gensell, genhands, search, deepsearch, getvalue, create, edit, add
from bot_password import bot

global st
global d
global hd
global nm

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


def json_save_hd():
    with open('hands.json', 'w') as fp:
        json.dump(hd, fp)


def json_load_hd():
    global hd
    with open('hands.json', 'r') as fp:
        hd = json.load(fp)


def json_save_nm():
    with open('names.json', 'w') as fp:
        json.dump(nm, fp)


def json_load_nm():
    global nm
    with open('names.json', 'r') as fp:
        nm = json.load(fp)


def rusificate(line):
    for word in range(len(line)):
        for indeh in range(len(d['Rus_Flavours'])):
            if d['Flavours'][indeh] == line[word]:
                line[word] = d['Rus_Flavours'][indeh][1:]
                line_n = line[word].replace(")", "")
                line[word] = line_n


def rusificate_genlist(line):
    line = line.split()
    for word in range(len(line)):
        for indeh in range(len(d['Rus_Flavours'])):
            if d['Flavours'][indeh][:-1] == line[word]:
                line[word] = d['Rus_Flavours'][indeh][:-1]
    return ' '.join(line)


def rusificate_post(line):
    if line == list:
        ''.join(line)
    for indeh in range(len(d['Rus_Flavours'])):
        if d['Flavours'][indeh] == line:
            return d['Rus_Flavours'][indeh][:-1]


def rusificate_gencock(line):
    for word in range(len(line)):
        for indeh in range(len(d['Rus_Flavours'])):
            if d['Flavours'][indeh][:-1] in line[word]:
                line[word] = line[word].replace(d['Flavours'][indeh][:-1], d['Rus_Flavours'][indeh][:-1])


def post_take(m):
    name = nm[get_person_id(m)]
    taken_model = (list(hd[get_user_id(m)].keys())[-1])
    taken_flavour = (list(hd[get_user_id(m)][taken_model].keys())[-1])
    amount_nm = str(int(hd[get_user_id(m)][taken_model].get(taken_flavour)-1))
    taken_flavour = rusificate_post(taken_flavour)
    taken_model = str(taken_model.replace('_', ' '))

    message = f'{name} взял {amount_nm} {taken_model}{taken_flavour} со склада.'
    requests.post(
        f'https://api.telegram.org/bot5293957385:AAGXrcOkHhcgQXGXkMzitKUcDUI4jDPcd-o/sendMessage?chat_id=-1001448891024&text={message}')

    # hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = hd[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    return

def post_sell(m):
    name = nm[get_person_id(m)]
    sold_model = (list(hd[get_user_id(m)].keys())[-1])
    sold_flavour = (list(hd[get_user_id(m)][sold_model].keys())[-1])
    amount_nm = str(hd[get_user_id(m)][sold_model].get(sold_flavour))
    sold_flavour = rusificate_post(sold_flavour)
    sold_model = str(sold_model.replace('_', ' '))

    message = f'{name} взял {amount_nm} {taken_model}{taken_flavour} со склада.'
    requests.post(
        f'https://api.telegram.org/bot5293957385:AAGXrcOkHhcgQXGXkMzitKUcDUI4jDPcd-o/sendMessage?chat_id=-1001448891024&text={message}')

    # hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = hd[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    return


json_load_d()
json_load_st()
json_load_hd()
json_load_nm()

"""Команды!!!!"""


@bot.message_handler(commands=["start"])
def start_cm(m, ):
    del_cache(m)
    create_cache(m)
    edit_cache(m, m.text)
    msg = bot.send_message(m.chat.id, 'Введите свое имя.')
    bot.register_next_step_handler(msg, set_name)


def set_name(m):
    del_cache(m)
    create_cache(m)
    edit_cache(m, m.text)
    nm[f'{get_person_id(m)}'] = get_cache(m)
    json_save_nm()


@bot.message_handler(commands=["info"])
def info_cm(m, ):
    user_id = get_user_id(m)
    word = 'sell_' + user_id
    inventory = deepsearch(word)
    rusificate_gencock(inventory)
    inventory = (genlist(inventory))
    inventory = inventory.replace("_", " ")
    inventory = inventory.replace("sell", "")
    inventory = inventory.replace(get_user_id(m), "")
    count = 0
    for i in range(len(deepsearch(word))):
        count += getvalue(deepsearch(word)[i])
    money = 'money_' + user_id
    count_m = 0
    for i in range(len(deepsearch(money))):
        count_m += getvalue(deepsearch(money)[i])
    bot.send_message(m.chat.id,
                     'Вы продали: \n' + inventory + '\n💹 Всего: ' + str(count) + 'шт.\n💰 Всего выручки: ' + str(
                         count_m))
    hand_cm(m)


@bot.message_handler(commands=["hand"])
def hand_cm(m, ):
    cock = []
    count = 0
    try:
        if hd[get_user_id(m)] == {}:
            return
    except KeyError:
        bot.send_message(m.chat.id, 'Вы броук.\n🙌 На руках 0 шт.')
        return

    for hd_model in list(hd[get_user_id(m)].keys()):
        for flavour in list(hd[get_user_id(m)][hd_model].keys()):
            val = hd[get_user_id(m)][hd_model][flavour]
            count += val
            line = hd_model + flavour + str(val)
            cock.append(line)
    rusificate_gencock(cock)
    bot.send_message(m.chat.id, 'У вас на руках:\n' + genhands(cock) + '\n🙌 Всего на руках: ' + str(count) + ' шт.')


@bot.message_handler(commands=["stats"])
def stats_cm(m, ):
    hands = 0
    storage = 0

    if hd == {}:
        h_line = 'Все ручки пусты!'
    else:
        for hd_id in list(hd.keys()):
            for st_model in list(hd[hd_id].keys()):
                for flavour in list(hd[hd_id][st_model].keys()):
                    val = hd[hd_id][st_model][flavour]
                    hands += val
        h_line = '🙌Всего на руках: ' + str(hands) + ' шт.\n'

    if st == {}:
        st_line = 'На складе ничего нет!'
    else:
        for st_model in list(st.keys()):
            for flavour in list(st[st_model].keys()):
                val1 = st[st_model][flavour]
                storage += val1
        st_line = '🖊️Всего на складе: ' + str(storage) + ' шт.\n'

    word = 'sell_'
    count = 0
    for i in range(len(deepsearch(word))):
        count += getvalue(deepsearch(word)[i])
    money = 'money_'
    count_m = 0
    for i in range(len(deepsearch(money))):
        count_m += getvalue(deepsearch(money)[i])
    m_line = '\n💹 Всего продано: ' + str(count) + 'шт.\n\n💰 Всего выручки: ' + str(count_m)

    bot.send_message(m.chat.id, st_line + '\n' + h_line + m_line)


@bot.message_handler(commands=["storage"])
def storage_cm(m, ):
    cock = []
    count = 0
    try:
        if st == {}:
            bot.send_message(m.chat.id, 'На складе ничего нет!')
            return
    except KeyError:
        bot.send_message(m.chat.id, 'На складе ничего нет!')
        return

    for st_model in list(st.keys()):
        for flavour in list(st[st_model].keys()):
            val = st[st_model][flavour]
            count += val
            line = st_model + flavour + str(val)
            cock.append(line)
    rusificate_gencock(cock)
    bot.send_message(m.chat.id, 'Сейчас на складе:\n' + genhands(cock) + '\n 🖊️ Всего: ' + str(count) + ' шт.')


@bot.message_handler(commands=["getcache"])
def storage_cb(m, ):
    storage_cm(m)
    del_model(m)
    json_load_d()

    line = d.get('Model')
    msg = bot.reply_to(m, 'Введите номер: \n0. Очистить словарь и хранилище от вкусов и моделей' + genlist(line) + str(
        len(d.get('Model')) + 1) + '. Добавить новую модель.\n' + str(
        len(d.get('Model')) + 2) + '. Добавить новый вкус.')
    bot.register_next_step_handler(msg, storage_model)


def storage_model(m, ):
    del_cache(m)
    create_cache(m)
    edit_cache(m, m.text)
    if (get_cache(m).isdigit() is False) or (int(get_cache(m)) > (len(d.get('Model'))) + 2):
        bot.reply_to(m, '❌Неправильный номер модели\nВведите команду заново')
        del_cache(m)
        del_cache1(m)
        return
    elif int(get_cache(m)) == (len(d.get('Model'))) + 1:
        msg = bot.reply_to(m, 'Введите номер название новой модели.\n\nПример:\n\"Quvie_Air_\" (без кавычек)')
        bot.register_next_step_handler(msg, storage_new_model)
        return
    elif int(m.text) == ((len(d.get('Model'))) + 2):
        msg = bot.reply_to(m, 'Введите название нового вкуса.\n\nПример:\n\"Apple_\" (без кавычек)')
        bot.register_next_step_handler(msg, storage_new_flavour)
        return
    elif int(m.text) == 0:
        msg = bot.reply_to(m,
                           'Уверены что хотите удалить все вкусы и одноразки в словаре и на складе?\n1. Да.\n2. Нет.')
        bot.register_next_step_handler(msg, storage_clear)
        return

    try:
        if st[d.get('Model')[int(get_cache(m)) - 1]] is dict:
            pass
    except KeyError:
        st[d.get('Model')[int(get_cache(m)) - 1]] = {}
        json_save_st()

    line = d.get('Rus_Flavours')

    msg = bot.reply_to(m, 'введите номер вкуса\n' + genlist(line))
    bot.register_next_step_handler(msg, storage_flavours)


def storage_flavours(m, ):
    global d
    create_cache1(m)
    edit_cache1(m, m.text)
    if (get_cache1(m).isdigit() is False) or (int(get_cache1(m)) > len(d.get('Flavours'))) or (int(get_cache1(m)) == 0):
        bot.reply_to(m, '❌Неправильный номер вкуса\nВведите команду заново')
        del_cache(m)
        del_cache1(m)
        return

    try:
        if st[d.get('Model')[int(get_cache(m)) - 1]][d.get('Flavours')[int(get_cache1(m)) - 1]] is dict:
            pass
    except KeyError:
        st[d.get('Model')[int(get_cache(m)) - 1]][d.get('Flavours')[int(get_cache1(m)) - 1]] = 0
        json_save_st()

    msg = bot.reply_to(m, 'Введите колличество одноразок на складе:')
    bot.register_next_step_handler(msg, storage_amount)


def storage_amount(m, ):
    model_st = d.get('Model')[int(get_cache(m)) - 1]
    edit_cache(m, m.text)

    if get_cache(m).isdigit() is False:
        bot.reply_to(m, '❌Неправильное число\nВведите команду заново')
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


def storage_new_model(m, ):
    new_name = m.text
    if str(new_name)[-1] != '_':
        new_name = new_name + '_'
    if ' ' in new_name:
        new_name = new_name.replace(' ', '_')
    d['Model'].append(str(new_name))
    json_save_d()
    bot.reply_to(m,
                 'Вы успешно добавили новую модель под названием ' + new_name)
    del_cache(m)


def storage_new_flavour(m, ):
    new_name = m.text
    if str(new_name)[-1] != '_':
        new_name = new_name + '_'
    if ' ' in new_name:
        new_name = new_name.replace(' ', '')
    d['Model']['Flavours'].append(str(new_name))
    msg = bot.reply_to(m,
                       'Введите название на русском для ' + new_name)
    bot.register_next_step_handler(msg, storage_new_flavour_rus)


def storage_new_flavour_rus(m, ):
    new_name = m.text
    if str(new_name)[-1] != '_':
        new_name = new_name + '_'
    if str(new_name)[-2] != ')':
        new_name = new_name + ')'
    if str(new_name)[-2] != '(':
        new_name = new_name + '('
    if ' ' in new_name:
        new_name = new_name.replace(' ', '_')
    d['Model']['Rus_Flavours'].append(str(new_name))
    json_save_d()
    del_cache(m)
    bot.reply_to(m, 'Вы успешно добавили новую модель под названием ' + new_name)


def storage_clear(m, ):
    global d
    global st
    if int(m.text) == 1:
        d = {}
        st = {}
        del_cache(m)
    else:
        bot.reply_to(m, 'Команда отменена.')
        del_cache(m)


@bot.message_handler(commands=["take"])
def take_cb(m, ):
    storage_cm(m)
    del_model(m)
    line = list(st.keys())
    for i in range(len(line)):
        line[i] = line[i].replace('_', ' ')
    msg = bot.reply_to(m, 'Введите номер модели: \n' + genlist(line))
    try:
        if hd[get_user_id(m)] is dict:
            pass
    except KeyError:
        hd[get_user_id(m)] = {}
        json_save_hd()
    bot.register_next_step_handler(msg, model)


def model(m, ):
    create_cache(m)
    edit_cache(m, m.text)
    create_model(m)
    line = list(st.keys())
    if (get_cache(m).isdigit() is False) or (int(get_cache(m)) > len(line)) or (int(get_cache(m)) == 0):
        bot.reply_to(m, '❌Неправильный номер модели\nВведите команду заново')
        del_cache(m)
        del_model(m)
        del hd[get_cache(m)]
        return

    edit_model(m, line[int(get_cache(m)) - 1])
    edit_cache(m, line[int(get_cache(m)) - 1])
    line = list(st[get_cache(m)].keys())
    rusificate(line)
    for i in range(len(line)):
        line[i] = line[i].replace('_', ' ')
    msg = bot.reply_to(m, 'Введите номер вкуса:\n' + genlist(line))

    try:
        if hd[get_user_id(m)][get_cache(m)] is dict:
            pass
    except KeyError:
        hd[get_user_id(m)][get_cache(m)] = {}
        json_save_hd()

    bot.register_next_step_handler(msg, flavours)


def flavours(m, ):
    create_cache1(m)
    edit_cache1(m, m.text)
    line = list(st[get_cache(m)].keys())
    if (get_cache1(m).isdigit() is False) or (int(get_cache1(m)) > len(line)) or (int(get_cache1(m)) == 0):
        bot.reply_to(m, '❌Неправильный номер вкуса\nВведите команду заново')
        del_cache(m)
        del_cache1(m)
        del_model(m)
        del st[get_cache(m)][get_cache(m)]
        return

    edit_model(m, line[int(get_cache1(m)) - 1])
    edit_cache1(m, line[int(get_cache1(m)) - 1])

    try:
        if hd[get_user_id(m)][get_cache(m)][get_cache1(m)] is dict:
            pass
    except KeyError:
        hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = 0
        json_save_hd()
    msg = bot.reply_to(m, 'Введите колличество взятых одноразок:')
    bot.register_next_step_handler(msg, amount)


def amount(m, ):
    if m.text.isdigit() is False or (int(m.text) == 0):
        bot.reply_to(m, '❌Неправильное число моделей\nВведите команду заново')
        # msg = bot.reply_to(m, 'Неправильное число, повторите')
        del st[get_cache(m)][get_cache1(m)]
        del_cache(m)
        del_cache1(m)
        del_model(m)

    if st[get_cache(m)][get_cache1(m)] == int(m.text):
        del st[get_cache(m)][get_cache1(m)]
        json_save_st()
        if st[get_cache(m)] == {}:
            del st[get_cache(m)]
            json_save_st()
    elif st[get_cache(m)][get_cache1(m)] < int(m.text):
        bot.reply_to(m, '❌Вы просите больше, чем есть на складе!')
        del_cache(m)
        del_cache1(m)
        del_model(m)
        return
    else:
        st[get_cache(m)][get_cache1(m)] -= int(m.text)
        json_save_st()

    hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = hd[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    json_save_hd()

    bot.reply_to(m, 'вы взяли ' + m.text + ' одноразок на руки!')
    post_take(m)


@bot.message_handler(commands=["sell"])
def sell_cb(m, ):
    del_model(m)
    hand_cm(m)
    try:
        if hd[get_user_id(m)] is dict:
            return
    except KeyError:
        return

    line = list(hd[get_user_id(m)].keys())

    msg = bot.reply_to(m, 'Введите название модели: \n' + gensell(line))

    create_model(m)
    del_cache(m)
    bot.register_next_step_handler(msg, s_model)


def s_model(m, ):
    create_cache(m)
    edit_cache(m, m.text)

    if (get_cache(m).isdigit() is False) or int(get_cache(m)) > len(list(hd[get_user_id(m)].keys())) or int(
            get_cache(m)) == 0:
        bot.reply_to(m, '❌Неправильный номер модели\nВведите команду заново')
        del_cache(m)
        del_model(m)
        return
    line = list(hd[get_user_id(m)].keys())
    edit_cache(m, line[int(get_cache(m)) - 1])
    edit_model(m, get_cache(m))
    line = list(hd[get_user_id(m)][get_cache(m)].keys())
    rusificate(line)
    msg = bot.reply_to(m, 'Введите номер вкуса:\n' + gensell(line))
    bot.register_next_step_handler(msg, s_flavours)


def s_flavours(m, ):
    create_cache1(m)
    edit_cache1(m, m.text)
    if (get_cache1(m).isdigit() is False) or int(get_cache1(m)) > len(
            list(hd[get_user_id(m)][get_cache(m)].keys())) or int(get_cache1(m)) == 0:
        bot.reply_to(m, '❌Неправильный номер вкуса\nВведите команду заново')
        del_cache(m)
        del_model(m)
        return

    line = list(hd[get_user_id(m)][get_cache(m)].keys())
    edit_cache1(m, line[int(get_cache1(m)) - 1])
    edit_model(m, get_cache1(m))
    msg = bot.reply_to(m, 'Введите количество проданных одноразок:')
    bot.register_next_step_handler(msg, s_amount)


def s_amount(m, ):
    Model = get_cache(m)
    Flavour = get_cache1(m)
    edit_cache(m, m.text)

    if get_cache(m).isdigit() is False or int(get_cache(m)) == 0:
        bot.reply_to(m, '❌Неправильное число\nВведите команду заново')
        del_cache(m)
        del_model(m)
        return

    if int(get_cache(m)) > hd[get_user_id(m)][Model][Flavour]:
        bot.reply_to(m, 'У вас нет столько на руках!')
    elif int(get_cache(m)) == hd[get_user_id(m)][Model][Flavour]:
        del hd[get_user_id(m)][Model][Flavour]
        json_save_hd()
    else:
        hd[get_user_id(m)][Model][Flavour] -= int(get_cache(m))
        json_save_hd()
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
        msg = bot.reply_to(m, '❌Неправильное число, повторите')
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
    bot.reply_to(m, '💰 Вы пополнили казну мстителей на ' + get_cache(m) + ' руб. Поздравляем!')


backup()
bot.polling(none_stop=True, interval=0)
