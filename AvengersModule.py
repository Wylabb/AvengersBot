def get_user_id(m, ):
    return str(m.from_user.id)


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