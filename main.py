import json

from date_extractor import ExtractDate
from parser import DATE
from natasha import (
    MorphVocab,
    DatesExtractor
)
from IPython.display import display
from yargy.parser import prepare_trees

import re
from yargy.tokenizer import MorphTokenizer
from yargy import (
    Parser,
    or_, rule
)
from viz import viz
import test, test_all_date

#from test_all_date import make_test
lines = ['с февраля по апрель позапрошлого года' ,
'за второй квартал предыдущего года',
'за вторую неделю прошлого месяца',
'за первую неделю сентября прошлого года',
'за второй день третьей недели второго квартала',
'за первый месяц 2020 года',
'за три недели первого квартала 2019 года',
'за 4 квартал 2020 года',
'за три дня',
'за прошлую неделю',
'за предыдущий месяц',
'с апреля 2010 года',
'после апреля 2010 года',
'за апрель 2010 года',
'с мая по июнь 2020 года',
'с февраля по апрель позапрошлого года',
'до июня текущего года',
'за последние три года',
'в 2018 году',
'с 01.10 по 01.12',
'со второй по четвертую неделю первого квартала',
'со второго квартала 2019 по третий квартал 2020',
'с января по май 2019 и с первого по третий квартал прошлого года'
]


all_tests = [
' со второго квартала 2019 по третий квартал 2020 ' ,
' за сегодня ' ,
' за вчера ' ,
' за позавчера ' ,
' за последний день ' ,
' за последнюю неделю ' ,
' за последний месяц ' ,
' за последний квартал ' ,
' за последнее полугодие ' ,
' за последний год ' ,
' за последние два дня ' ,
' за последние три недели ' ,
' за последние четыре месяца ' ,
' за последние два квартал ' ,
' за последние три года ' ,
' за прошлый день ' ,
' за прошлую неделю ' ,
' за прошлый месяц ' ,
' за прошлый квартал ' ,
' за прошлое полугодие ' ,
' за прошлый год ' ,
' за два прошлых дня ' ,
' за две прошлых недели ' ,
' за три прошлых месяца ' ,
' за четыре прошлых года ' ,
' за предыдущий день ' ,
' за предыдущую неделю ' ,
' за предыдущий месяц ' ,
' за предыдущий квартал ' ,
' за предыдущее полугодие ' ,
' за предыдущий год ' ,
' за два предыдущих дня ' ,
' за две предыдущих недели ' ,
' за три предыдущих месяца ' ,
' за четыре предыдущих года ' ,
' за день ' ,
' за один день ' ,
' за три дня ' ,
' за десять дней ' ,
' за двадцать дней ' ,
' за 1 день ' ,
' за 3 дня ' ,
' за 10 дней ' ,
' за неделю ' ,
' за одну неделю ' ,
' за три недели ' ,
' за десять недель ' ,
' за 1 неделю ' ,
' за 3 недели ' ,
' за 10 недель ' ,
' за месяц ' ,
' за один месяц ' ,
' за три месяца ' ,
' за десять месяцев ' ,
' за 1 месяц ' ,
' за 2 месяца ' ,
' за 3 месяца ' ,
' за 10 месяцев ' ,
' за квартал ' ,
' за один квартал ' ,
' за три квартала ' ,
' за 1 квартал ' ,
' за 3 месяца ' ,
' за полугодие ' ,
' за два полугодия ' ,
' за 2 полугодя ' ,
' за год ' ,
' за один год ' ,
' за три года ' ,
' за десять лет ' ,
' за 1 год ' ,
' за 3 года ' ,
' три дня назад ' ,
' две недели назад ' ,
' два месяца назад ' ,
' полгода назад ' ,
' год назад ' ,
' на прошлой неделе ' ,
' за январь ' ,
' за март 2012го ' ,
' за апрель 2008 ' ,
' за август 2019 года ' ,
' за 2011 год ' ,
' за 2012й ' ,
' за 2021 ' ,
' за второй квартал ' ,
' за июнь прошлого года ' ,
' за август позапрошлого года ' ,
' за первый квартал текущего года ' ,
' за третий квартал позапрошлого года ' ,
' за 2 квартал прошлого года ' ,
' за третий квартал предыдущего года ' ,
' за март месяц прошедшего года ' ,
' за февраль прошлого года ' ,
' за второе полугодие прошлого года ' ,
' за 2 неделю прошлого месяца ' ,
' за первую неделю сентября прошлого года ' ,
' за первый месяц 2020 года ' ,
' за второй день третьей недели второго квартала ' ,
' за 4 квартал 2020 года ' ,
' за три недели первого квартала 2019 года ' ,
' за вторую неделю сентября 2020 года ' ,
' с апреля 2010 года ' ,
' после апреля 2010 года ' ,
' за апрель 2010 года ' ,
' с мая по июнь 2020 года ' ,
' с февраля по апрель позапрошлого года ' ,
' до июня текущего года ' ,
' с января 2011 года по март 2012го ' ,
' с июня по декабрь ' ,
' с 2001 по 2012 гг ' ,
' с первого до десятого апреля 2019 года ' ,
' с августа по октябрь ' ,
' в апреле ' ,
' в марте 2012 года ' ,
' в апреле прошлого года ' ,
' в мае позапрошлого года ' ,
' во втором квартале ' ,
' в прошлом месяце ' ,
' в прошлом году ' ,
' в позапрошлом году ' ,
' в 2018 году ' ,
' в 2005-2010 годах ' ,
' в 2012-2013 гг ' ,
' с 2012 по 2013 ' ,
' c 01.10 по 01.12 ' ,
' с 01.02.2003 по 21.12.2012 ' ,
' с 01.02 по 21.12 ' ,
' с первого октября по первое декабря 2012 года ' ,
' с двадцать второго числа апреля месяца ' ,
' с первого полугодия прошлого года ' ,
' с третьего квартала текущего года ' ,
' со второй по четвертую неделю первого квартала ' ,
' с первого по третий квартал прошлого года ' ,
' с 1 по 3 неделю сентября 2013 года ' ,
' со второго квартала 2019 по третий квартал 2020 ' ,
' с января по май 2019 и с первого по третий квартал прошлого года ' ,
' отчет Павлова на портале за прошлую неделю ' ,
' отчет Иванов вики xlsx за прошлый месяц ' ,
' Иванов справка о доходах за прошлый год ' ,
' справка Сидорова pdf три дня назад ' ,
' квитанция от Ивана Петровича на прошлой неделе pdf ' ,
' квартальный отчет Светланы docx за прошлый квартал '
]

dict_num_day_ordinal = {}
dict_quarter_ordinal = {}
dict_quarter_cardinal = {}
dict_year_modifier = {}
dict_year_cardinal = {}
dict_week_ordinal = {}
dict_week_cardinal = {}
dict_month_modifier = {}
dict_date = {}
dict_day_cardinal = {}
dict_month_ordinal = {}
dict_month_cardinal = {}
dict_week_modifier = {}
dict_count ={}
dict_day_modifier = {}
dict_half_year = {}
dict_year_ordinal = {}
dict_quarter_modifier = {}
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--n', default=0,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
if __name__=="__main__":
    TOKENIZER = MorphTokenizer()
    morph_vocab = MorphVocab()
    parser = Parser(DATE)
    num_day_ordinal = []
    str_num = 0
    pred_day_ordinal = []
    n = int(args.n)
    print("Введите ", n, " строк с датами:")
    new_lines = []
    for i in range(n):
        line = input()
        new_lines.append(line)

    # new_lines - для ввода с консоли
    for line in all_tests:

        print(str_num, "Исходный текст: ", line)
        f = open(("output/{}.json").format(str_num), "w+")
        f.seek(0)

        str_num = str_num + 1
        split_on_date = re.split(r'с |по | до ', line)
        z = {}
        for split in [line]:#split_on_date:
            date = ExtractDate()
            matches = parser.extract(split)
            dict_result, date_dict, result, r = viz(str_num, date, split, matches, dict_num_day_ordinal,
             dict_quarter_ordinal,
             dict_quarter_cardinal,
             dict_year_modifier,
             dict_year_cardinal,
             dict_week_ordinal,
             dict_week_cardinal,
             dict_month_modifier,
             dict_date,
             dict_day_cardinal,
             dict_month_ordinal,
             dict_month_cardinal,
             dict_week_modifier, dict_count, dict_day_modifier, dict_half_year, dict_year_ordinal,
             dict_quarter_modifier)
            #print("DICT R", dict_result)
            #try:
            z = z.copy()
            z.update(dict_result)
        #if result["id_interval"]
        #print("QQQQQQ", dict_quarter_modifier)
        # Remove duplicate values in dictionary
        # Using loop
        temp = []
        res = dict()
        for key, val in dict_result.items():
            if val not in temp:
                temp.append(val)
                res[key] = val
        temp = []
        res_date = dict()
        for key, val in r.items():
            if val not in temp:
                temp.append(val)
                res_date[key] = val
        f.write(json.dumps(res_date,  indent=4, ensure_ascii=False))
        f.write('\n')
        print("RESULT", r)
        final = {}
        #print(r["DateIntervals"].popitem())
        #for ent in r["DateIntervals"]:
            #print(r.keys()[-1] )
        #    print(r["DateIntervals"].popitem())
        print("DATE", res_date)
        print("========================")
        f.close()
    test_all_date.make_test( dict_num_day_ordinal,
             dict_quarter_ordinal,
             dict_quarter_cardinal,
             dict_year_modifier,
             dict_year_cardinal,
             dict_week_ordinal,
             dict_week_cardinal,
             dict_month_modifier,
             #dict_date,
             dict_day_cardinal,
             dict_day_modifier,
             dict_month_ordinal,
             dict_month_cardinal,
             dict_week_modifier,
             dict_year_ordinal,
             dict_quarter_modifier)

