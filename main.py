import json

import requests

from AvengersModule import get_user_id, create_cache, edit_cache, get_cache, del_cache, create_cache1, edit_cache1, \
    get_cache1, del_cache1, create_model, edit_model, del_model, get_person_id
from FunctionsModule import backup, genlist, gensell, genhands, deepsearch, getvalue
from bot_password import bot

global st
global d
global hd
global nm
global mo
global se

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


def json_save_se():
    with open('sell.json', 'w') as fp:
        json.dump(se, fp)


def json_load_se():
    global se
    with open('sell.json', 'r') as fp:
        se = json.load(fp)


def json_save_mo():
    with open('money.json', 'w') as fp:
        json.dump(mo, fp)


def json_load_mo():
    global mo
    with open('money.json', 'r') as fp:
        mo = json.load(fp)


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


def post_take(m, amount_nm):
    name = nm[get_person_id(m)]
    taken_model = (list(hd[get_user_id(m)].keys())[-1])
    taken_flavour = (list(hd[get_user_id(m)][taken_model].keys())[-1])
    taken_flavour = rusificate_post(taken_flavour)
    taken_model = str(taken_model.replace('_', ' '))

    message = f'{name} взял {amount_nm} {taken_model}{taken_flavour} со склада.'
    requests.post(
        f'https://api.telegram.org/bot5293957385:AAGXrcOkHhcgQXGXkMzitKUcDUI4jDPcd-o/sendMessage?chat_id'
        f'=-1001448891024&text={message}')

    # hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = hd[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    return


# def post_sell(m):
#     name = nm[get_person_id(m)]
#     sold_model = (list(hd[get_user_id(m)].keys())[-1])
#     sold_flavour = (list(hd[get_user_id(m)][sold_model].keys())[-1])
#     amount_nm = str(hd[get_user_id(m)][sold_model].get(sold_flavour))
#     sold_flavour = rusificate_post(sold_flavour)
#     sold_model = str(sold_model.replace('_', ' '))
#
#     message = f'{name} взял {amount_nm} {sold_model}{sold_flavour} со склада.'
#     requests.post(
#         f'https://api.telegram.org/bot5293957385:AAGXrcOkHhcgQXGXkMzitKUcDUI4jDPcd-o/sendMessage?chat_id=-1001448891024&text={message}')

# hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = hd[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
# return


json_load_d()
json_load_st()
json_load_hd()
json_load_nm()
json_load_mo()
json_load_se()

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
    cock = []
    count = 0
    count_m = 0
    try:
        if se[get_user_id(m)] == {}:
            return
    except KeyError:
        bot.send_message(m.chat.id, 'Вы броук.\n🙌 Вы ничего не продавали.')
        return

    for se_model in list(se[get_user_id(m)].keys()):
        for flavour in list(se[get_user_id(m)][se_model].keys()):
            val = se[get_user_id(m)][se_model][flavour]
            count += val
            line = se_model + flavour + str(val)
            cock.append(line)

    try:
        if mo[get_user_id(m)] == {}:
            return
    except KeyError:
        bot.send_message(m.chat.id, 'Вы броук.\n🙌 Вы ничего не продавали.')
        return


    for mo_model in list(mo[get_user_id(m)].keys()):
        for flavour in list(mo[get_user_id(m)][mo_model].keys()):
            val = mo[get_user_id(m)][mo_model][flavour]
            count_m += val

    rusificate_gencock(cock)
    bot.send_message(m.chat.id,
                     f'Вы продали: \n{genhands(cock)}\n💹 Всего: {count} шт.\n💰 Всего выручки: {count_m}')
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

    count = 0
    count_m = 0
    try:
        if se == {}:
            return
    except KeyError:
        bot.send_message(m.chat.id, 'Мы банкоты.')
        return

    for se_id in list(se.keys()):
        for se_model in list(se[se_id].keys()):
            for flavour in list(se[se_id][se_model].keys()):
                val = se[se_id][se_model][flavour]
                count += val

    try:
        if mo == {}:
            return
    except KeyError:
        bot.send_message(m.chat.id, 'Мы банкроты.')
        return

    for mo_id in list(mo.keys()):
        for mo_model in list(mo[mo_id].keys()):
            for flavour in list(mo[mo_id][mo_model].keys()):
                val = mo[mo_id][mo_model][flavour]
                count_m += val


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
    if line is None:
        msg = bot.reply_to(m, 'Склад пуст')
        bot.register_next_step_handler(msg, storage_new_model)
        return

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
    d['Flavours'].append(str(new_name))
    msg = bot.reply_to(m,
                       'Введите название на русском для ' + new_name)
    bot.register_next_step_handler(msg, storage_new_flavour_rus)


def storage_new_flavour_rus(m, ):
    new_name = m.text
    if str(new_name)[0] != '(':
        new_name = '(' + new_name
    if str(new_name)[-1] != ')':
        new_name = new_name + ')'
    if str(new_name)[-1] != '_':
        new_name = new_name + '_'
    if ' ' in new_name:
        new_name = new_name.replace(' ', '_')
    d['Rus_Flavours'].append(str(new_name))
    json_save_d()
    del_cache(m)
    bot.reply_to(m, 'Вы успешно добавили новую модель под названием ' + new_name)


def storage_clear(m, ):
    global d
    global st
    if int(m.text) == 1:
        d = {"Model": [], "Flavours": [], "Rus_Flavours": []}
        st = {}
        json_save_st()
        json_save_d()
        del_cache(m)
        bot.reply_to(m, 'Вы даун.')
    else:
        bot.reply_to(m, 'Команда отменена.')
        del_cache(m)


@bot.message_handler(commands=["take"])
def take_cb(m, ):
    storage_cm(m)  # отображаем склад
    del_model(m)  # удаляем предыдущий кэш модели
    line = list(st.keys())  # перечисляем все модели в хранилище
    for i in range(len(line)):  # удаляем '_' из названий моделей
        line[i] = line[i].replace('_', ' ')
    msg = bot.reply_to(m, 'Введите номер модели: \n' + genlist(line))  # выводим список названий моделей
    # try:
    #     if hd[get_user_id(m)] is dict:  # пытаемся проверить есть ли у пользователя вкладка в hands.json
    #         pass  # если есть пропускаем
    # except KeyError:
    #     hd[get_user_id(m)] = {}  # если нет создаем новую
    #     json_save_hd()  # сохраняем .json
    bot.register_next_step_handler(msg, model)  # переходим к записи номера модели


def model(m, ):
    create_cache(m)  # создаем кэш для номера модели
    edit_cache(m, m.text)  # записываем в кэш номер модели
    line = list(st.keys())  # создаем список моделей
    if (get_cache(m).isdigit() is False) or (int(get_cache(m)) > len(line)) or (
            int(get_cache(m)) == 0):  # проверяем есть ли номер модели в списке
        bot.reply_to(m, '❌Неправильный номер модели\nВведите команду заново')
        del_cache(m)  # если номера нет удаляем кэш
        return
    create_model(m)  # создаем кэш модели
    edit_model(m, line[int(get_cache(m)) - 1])  # добавляем в модель название модели
    edit_cache(m, line[int(get_cache(m)) - 1])  # добавляем в кэш название модели
    line = list(st[get_cache(m)].keys())  # сохраняем список вкусов
    rusificate(line)  # русифицируем список вкусов
    for i in range(len(line)):  # заменяем '_' на пробелмы
        line[i] = line[i].replace('_', ' ')
    msg = bot.reply_to(m, 'Введите номер вкуса:\n' + genlist(line))  # выводим список вкусов

    # try:
    #     if hd[get_user_id(m)][get_cache(m)] is dict:  # существует ли hd['2345432'][CuvieAir]?
    #         pass
    # except KeyError:
    #     hd[get_user_id(m)][get_cache(m)] = {}  # если нет -- создаем(зачем?) TODO проверить
    #     json_save_hd()  # сохраняем в .json

    bot.register_next_step_handler(msg, flavours)  # переходим к записи номера вкуса


def flavours(m, ):
    create_cache1(m)  # создаем доп. кэш
    edit_cache1(m, m.text)  # изменяем доп. кэш на номер вкуса
    line = list(st[get_cache(m)].keys())  # создаем список со вкусами для нужной модели
    if (get_cache1(m).isdigit() is False) or (int(get_cache1(m)) > len(line)) or (
            int(get_cache1(m)) == 0):  # попадаем ли доп. кэш в номер вкуса?
        bot.reply_to(m, '❌Неправильный номер вкуса\nВведите команду заново')
        del_cache(m)  # если нет -- удаляем название модели одноразки
        del_cache1(m)  # удаляем номер вкуса
        del_model(m)  # удаляем модель
        return

    edit_model(m, line[int(get_cache1(m)) - 1])  # добавляем в модель вкус
    edit_cache1(m, line[int(get_cache1(m)) - 1])  # записываем в кэш1 название вкуса

    # try:
    #     if hd[get_user_id(m)][get_cache(m)][get_cache1(m)] is dict:  # существует ли hd[234432][CuvieAir][Strawberry]?
    #         pass
    # except KeyError:
    #     hd[get_user_id(m)][get_cache(m)][
    #         get_cache1(m)] = 0  # Если не существует ставим количество равным нулю TODO зачем?
    #     json_save_hd()  # сохраняем .json
    msg = bot.reply_to(m, 'Введите колличество взятых одноразок:')
    bot.register_next_step_handler(msg, amount)  # переходим ко записи количества взятых одноразок


def amount(m, ):
    if m.text.isdigit() is False or (int(m.text) == 0):  # проверяем правильно ли ввели количество
        bot.reply_to(m, '❌Неправильное число моделей\nВведите команду заново')
        # msg = bot.reply_to(m, 'Неправильное число, повторите')
        del_cache(m)  # удаляем название модели
        del_cache1(m)  # удаляем название вкуса
        del_model(m)  # удаляем модель
        return

    try:
        if hd[get_user_id(m)] is dict:  # пытаемся проверить есть ли у пользователя вкладка в hands.json
            pass  # если есть пропускаем
    except KeyError:
        hd[get_user_id(m)] = {}  # если нет создаем новую
        json_save_hd()  # сохраняем .json

    try:
        if hd[get_user_id(m)][get_cache(m)] is dict:  # существует ли hd['2345432'][CuvieAir]?
            pass
    except KeyError:
        hd[get_user_id(m)][get_cache(m)] = {}  # если нет -- создаем(зачем?)
        json_save_hd()  # сохраняем в .json

    try:
        if hd[get_user_id(m)][get_cache(m)][get_cache1(m)] is dict:  # существует ли hd[234432][CuvieAir][Strawberry]?
            pass
    except KeyError:
        hd[get_user_id(m)][get_cache(m)][
            get_cache1(m)] = 0  # Если не существует ставим количество равным нулю T
        json_save_hd()  # сохраняем .json

    if st[get_cache(m)][get_cache1(m)] == int(m.text):  # если берем моделей столько же сколько в хранилище
        del st[get_cache(m)][get_cache1(m)]  # удаляем st[CuvieAir][Strawberry] из хранилища
        json_save_st()  # сохраняем .json
        if st[get_cache(m)] == {}:  # если st[CuvieAir] пустое
            del st[get_cache(m)]  # удаляем его
            json_save_st()  # сохраняем .json
    elif st[get_cache(m)][get_cache1(m)] < int(m.text):  # если берем больше чем есть на складе
        bot.reply_to(m, '❌Вы просите больше, чем есть на складе!')
        del_cache(m)  # удаляем название модели
        del_cache1(m)  # удаляем вкус модели
        del_model(m)  # удаляем модель
        return
    else:
        st[get_cache(m)][get_cache1(m)] -= int(m.text)  # если все норм то вычитаем со склада взятых одноразки
        json_save_st()  # сохраняем .json

    hd[get_user_id(m)][get_cache(m)][get_cache1(m)] = hd[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    # в строчке сверху мы добавляем к количеству уже взятых одноразок новые
    json_save_hd()  # сохраняем .json

    bot.reply_to(m, f'вы взяли {m.text} одноразок на руки!')
    post_take(m, m.text)  # тут бот отсылает сколько одноразок взяли и постит в канал https://t.me/+r1p8ASGylO8xMzVi


@bot.message_handler(commands=["sell"])
def sell_cb(m, ):
    hand_cm(m)
    try:
        if hd[get_user_id(m)] is dict:
            pass
    except KeyError:
        return

    create_model(m)
    del_cache(m)
    line = list(hd[get_user_id(m)].keys())

    msg = bot.reply_to(m, 'Введите название модели: \n' + gensell(line))

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
    # if get_cache(m).isdigit() is False or int(get_cache(m)) == 0:
    #     bot.reply_to(m, '❌Неправильное число\nВведите команду заново')
    #     del_cache(m)
    #     del_cache1(m)
    #     return
    #
    # if int(get_cache(m)) > hd[get_user_id(m)][Model][Flavour]:
    #     bot.reply_to(m, 'У вас нет столько на руках!')
    # elif int(get_cache(m)) == hd[get_user_id(m)][Model][Flavour]:
    #     del hd[get_user_id(m)][Model][Flavour]
    #     json_save_hd()
    # else:
    #     hd[get_user_id(m)][Model][Flavour] -= int(get_cache(m))
    #     json_save_hd()
    # msg = bot.reply_to(m, f'Сколько вы получили с {get_cache(m)} одноразок этой модели?')
    #
    # # user_id_sell = 'sell_' + get_user_id(m) + '_'
    # # user_id_sell_model = user_id_sell + get_model(m)
    # #
    # # if search(user_id_sell_model) == 1:
    # #     add(user_id_sell_model, get_cache(m))
    # # else:
    # #     create(user_id_sell_model)
    # #     edit(user_id_sell_model, get_cache(m))

    try:
        if se[get_user_id(m)] is dict:  # пытаемся проверить есть ли у пользователя вкладка в hands.json
            pass  # если есть пропускаем
    except KeyError:
        se[get_user_id(m)] = {}  # если нет создаем новую
        json_save_se()  # сохраняем .json

    try:
        if se[get_user_id(m)][get_cache(m)] is dict:  # существует ли hd['2345432'][CuvieAir]?
            pass
    except KeyError:
        se[get_user_id(m)][get_cache(m)] = {}  # если нет -- создаем(зачем?)
        json_save_se()  # сохраняем в .json

    try:
        if se[get_user_id(m)][get_cache(m)][get_cache1(m)] is dict:  # существует ли hd[234432][CuvieAir][Strawberry]?
            pass
    except KeyError:
        se[get_user_id(m)][get_cache(m)][
            get_cache1(m)] = 0  # Если не существует ставим количество равным нулю T
        json_save_se()  # сохраняем .json

    if hd[get_user_id(m)][get_cache(m)][get_cache1(m)] == int(
            m.text):  # если берем моделей столько же сколько в хранилище
        del hd[get_user_id(m)][get_cache(m)][get_cache1(m)]  # удаляем st[CuvieAir][Strawberry] из хранилища
        json_save_hd()  # сохраняем .json
        if hd[get_user_id(m)][get_cache(m)] == {}:  # если st[CuvieAir] пустое
            del hd[get_user_id(m)][get_cache(m)]  # удаляем его
            json_save_hd()  # сохраняем .json
    elif hd[get_user_id(m)][get_cache(m)][get_cache1(m)] < int(m.text):  # если берем больше чем есть на складе
        bot.reply_to(m, '❌Вы просите больше, чем есть на руках!')
        del_cache(m)  # удаляем название модели
        del_cache1(m)  # удаляем вкус модели
        del_model(m)  # удаляем модель
        return
    else:
        hd[get_user_id(m)][get_cache(m)][get_cache1(m)] -= int(
            m.text)  # если все норм то вычитаем со склада взятых одноразки
        json_save_hd()  # сохраняем .json

    se[get_user_id(m)][get_cache(m)][get_cache1(m)] = se[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    # в строчке сверху мы добавляем к количеству уже взятых одноразок новые
    json_save_se()

    msg = bot.reply_to(m, f'Сколько вы получили с {m.text} одноразок этой модели?')
    bot.register_next_step_handler(msg, s_money)


def s_money(m, ):
    if m.text.isdigit() is False:
        msg = bot.reply_to(m, '❌Неправильное число, повторите')
        del_cache(m)
        bot.register_next_step_handler(msg, s_money)
        return

    try:
        if mo[get_user_id(m)] is dict:  # пытаемся проверить есть ли у пользователя вкладка в hands.json
            pass  # если есть пропускаем
    except KeyError:
        mo[get_user_id(m)] = {}  # если нет создаем новую
        json_save_mo()  # сохраняем .json

    try:
        if mo[get_user_id(m)][get_cache(m)] is dict:  # существует ли hd['2345432'][CuvieAir]?
            pass
    except KeyError:
        mo[get_user_id(m)][get_cache(m)] = {}  # если нет -- создаем(зачем?)
        json_save_mo()  # сохраняем в .json

    try:
        if mo[get_user_id(m)][get_cache(m)][get_cache1(m)] is dict:  # существует ли hd[234432][CuvieAir][Strawberry]?
            pass
    except KeyError:
        mo[get_user_id(m)][get_cache(m)][
            get_cache1(m)] = 0  # Если не существует ставим количество равным нулю T
        json_save_mo()  # сохраняем .json

    mo[get_user_id(m)][get_cache(m)][get_cache1(m)] = mo[get_user_id(m)][get_cache(m)][get_cache1(m)] + int(m.text)
    # в строчке сверху мы добавляем к количеству уже взятых одноразок новые
    json_save_mo()

    bot.reply_to(m, f'💰 Вы пополнили казну мстителей на {m.text} руб. Поздравляем!')


backup()
bot.polling(none_stop=True, interval=0)
