from yargy.parser import prepare_trees
from yargy import Parser, or_, rule
from yargy import (
    rule,
    and_, or_, not_
)
from yargy.interpretation import fact
from yargy.predicates import (
    eq, gte, lte, length_eq,
    dictionary, normalized,
)
from yargy import (
    Parser,
    or_, rule
)
from yargy.predicates import (
    eq, in_, dictionary,
    type, gram
)
from yargy.parser import prepare_trees
from yargy import Parser, or_, rule
from yargy import (
    rule,
    and_, or_, not_
)
from yargy.interpretation import fact
from yargy.predicates import (
    eq, gte, lte, length_eq,
    dictionary, normalized,
)
from yargy.predicates import (
    eq, in_, dictionary,
    type, gram
)

Date = fact(
    'Date',
    # ['year', 'quater', 'month','week',  'day']
    ['week_ordinal', 'week_cardinal', 'week_modifier', 'week_start_ordinal', 'week_end_ordinal',

     'quarter_ordinal', 'quarter_cardinal', 'quarter_start_ordinal', 'quarter_end_ordinal',

     'month_modifier', 'month_ordinal', 'month_cardinal',

     'year_modifier', 'year_cardinal', 'year_start_modifier', 'year_end_modifier',

     'half_year', 'count',

     'day_ordinal', 'day_cardinal', 'day_modifier',

     'date', 'date_month', 'start_date', 'end_date']
)


class Date(Date):
    @property
    def obj(self):
        from natasha import obj
        return obj.Date(  # self.year ,self.quater, self.month , self.week,self.day ,
            self.week_ordinal, self.week_cardinal, self.week_modifier, self.week_start_ordinal, self.week_end_ordinal,
            self.quarter_ordinal, self.quarter_cardinal, self.quarter_start_ordinal, self.quarter_end_ordinal,
            self.month_modifier,
            self.month_ordinal, self.month_cardinal, self.date_month, self.year_modifier, self.year_cardinal,
            self.year_start_modifier,
            self.half_year, self.count,
            self.year_end_modifier, self.date, self.day_ordinal, self.day_cardinal, self.day_modifier, self.start_date,
            self.end_date
        )


INT = type('INT')
NOUN = gram('NOUN')
ADJF = gram('ADJF')
PRTF = gram('PRTF')
GENT = gram('gent')
NUMR = gram('NUMR')
DOT = eq('.')

MONTHS = {
    'январь': 1,
    'февраль': 2,
    'март': 3,
    'апрель': 4,
    'май': 5,
    'июнь': 6,
    'июль': 7,
    'август': 8,
    'сентябрь': 9,
    'октябрь': 10,
    'ноябрь': 11,
    'декабрь': 12,
    'текущий': 0,
}
MODIFIERS = {
    'текущий': 0,
    'прошлый': -1,
    'позапрошлый': -2,
    'позавчерашний': -2,
    'прошедшее': -1,
    'последний': -0.5,
    'прошлый': -1,
    'предыдущий': -1,
    'вчерашний': -1,
    'истекший': -1,
    'прошлое': -1,
    'прошлого': -1,
    'три': 3,
    'один': 1,
    '2019': 2019,
    'первый': 1,
}

CARDINALS = {
    'второй': 2
}

FROM_STR_TO_INT = {
    'апрель': 4,
    'за': 1,
    'три': 3,

    'первый': 1,
    'третий': 3,
    '4': 4,
    '1': 1,
    '3': 3,
    '2': 2,
    'две': 2,
    '2й': 2,
    '2ю': 2,
    '10': 10,
    'один': 1,
    'прошлый': -1,
    'четвёртый': 4,
    'четыре': 4,
    'два': 2,
    'десять': 10,
    'последний': -0.5,
    'предыдущий': -1,
    'двадцать': 20,
    'сегодня': 0,
    'вчера': -1,
    'позавчера': -2,
    'последнее': -0.5,
    'прошлое': -1,
    'второе': 2,
    'назад': -1,
    'первое': 1,
    'третье': 3,
    'четвертовать': 4
}

YEAR_WORD = or_(
    rule('г', eq('.').optional()),
    rule(normalized('год')),
    rule('года')
)



YEAR_STR = or_(
    ADJF
).interpretation(
    Date.year_modifier.normalized().custom(MODIFIERS.__getitem__)
)
YEAR_INT = or_(
    NUMR
).interpretation(
    Date.year_cardinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)
YEAR = and_(
    gte(1000),
    lte(2100)
).interpretation(
    Date.year_cardinal.custom(int)
)

YEAR_SHORT = and_(
    length_eq(2),
    gte(0),
    lte(99)
).interpretation(
    Date.year_cardinal.custom(lambda _: 1900 + int(_))
)

QUATER_WORD = or_(
    rule(normalized('квартал')),
    rule('квартала')
)

QUATER_INT = or_(
    INT,
    NUMR
).interpretation(
    Date.quarter_cardinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)

QUATER_ADJF = or_(
    ADJF
).interpretation(
    Date.quarter_ordinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)

ADJF_INT_NUMR = or_(
    # ADJF,
    INT,
    NUMR
)

MODIFIER = or_(
    eq(normalized('прошлую')),
    eq(normalized('прошлый')),
    eq(normalized('предыдущий')),
    eq(normalized('прошлого')),
    eq(normalized('прошлое')),
    eq(normalized('последний')),
    eq('последнее')
)

MONTH_MODIFIER = or_(
    eq(normalized('прошлую')),
    eq('прошлый'),
    eq('предыдущий'),
    eq('прошлого'),
    eq('прошлое'),
    eq('последний'),

).interpretation(
    Date.month_modifier.normalized().custom(MODIFIERS.__getitem__)
)

MONTH_NAME = dictionary(MONTHS).interpretation(
    Date.month_ordinal.normalized().custom(MONTHS.__getitem__)
)

MONTH = and_(
    gte(1),
    lte(12)
).interpretation(
    Date.month_ordinal.custom(int)
)

MONTH_WORD = or_(
    rule(normalized('месяц'))
)

MONTH_CARDINAL=rule(
    eq('первый')
).interpretation(
    Date.month_cardinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)


MONTH_STR = not_(
    or_(
        eq(normalized('прошлую')),
        eq('прошлый'),
        eq('предыдущий'),
        eq('прошлого'),
        eq('прошлое'),
        eq('последний'),
        eq('март'),
        eq(normalized('апрель')))

).interpretation(
    Date.month_ordinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)

WEEK_WORD = or_(
    rule(normalized('неделя'))
)

WEEK_MODIFIER = or_(
    eq('прошлую'),
    eq('прошлый'),
    eq('прошлое'),
    eq('последний')
).interpretation(
    Date.week_modifier.normalized().custom(MODIFIERS.__getitem__)
)

WEEK_ORIG = not_(

    or_(
        eq('три'),
        eq('прошлую'),
        eq('прошлый'),
        eq('прошлое'),
        eq('последний'))
).interpretation(
    Date.week_ordinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)
WEEK_CARD = or_(
    eq('три')
).interpretation(
    Date.week_cardinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)

DAY = and_(
    gte(1),
    lte(31)
).interpretation(
    Date.day_ordinal.custom(int)
)

DAY_STR = not_(
    or_(
        eq(normalized('прошлую')),
        eq('прошлый'),
        eq('предыдущий'),
        eq('прошлого'),
        eq('прошлое'),
        eq('последний'))
).interpretation(
    Date.day_cardinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)
DAY_INT = or_(
    NUMR
).interpretation(
    Date.day_cardinal.normalized().custom(FROM_STR_TO_INT.__getitem__)
)
DAY_WORD = or_(
    rule(normalized('день'))
)
PERIOD_START = or_(

)

ALL_WORD = not_(
    eq('fkn')
)

DAY_MODIFIER = or_(
    eq('прошлую'),
    eq('прошлый'),
    eq('прошлое'),
    eq('последний'),
    eq("предыдущий")
).interpretation(
    Date.day_modifier.normalized().custom(MODIFIERS.__getitem__)
)
multipleDATE = or_(
    rule(
        eq('с'),
        ADJF.optional().interpretation(Date.start_date.custom(str)),
        NOUN.optional().interpretation(Date.start_date.custom(str)),

        eq('по'),

        ADJF.optional().interpretation(Date.end_date.custom(str)),
        NOUN.optional().interpretation(Date.end_date.custom(str)),
    ),
    # DATE
)

def normalize_float(val):
    return 1

DATE = or_(
    rule(
        or_(eq('сегодня'), eq("вчера"), eq('позавчера')).interpretation(
            Date.day_ordinal.custom(FROM_STR_TO_INT.__getitem__))

    ),

    rule(
        ADJF_INT_NUMR.interpretation(Date.day_ordinal),
        DAY_MODIFIER,
        DAY_WORD
    ),
    rule(
        ADJF_INT_NUMR.optional(),
        DAY_WORD
    ),

    rule(
        or_(INT, NUMR).optional().interpretation(Date.day_ordinal.custom(FROM_STR_TO_INT.__getitem__)),
        DAY_STR,
        DAY_WORD
    ),
    rule(

        ALL_WORD.interpretation(Date.day_ordinal.normalized().custom(FROM_STR_TO_INT.__getitem__)),
        DAY_WORD
    ),
    rule(
        WEEK_CARD,
        WEEK_WORD
    ),

    rule(
        or_(INT, NUMR).optional().interpretation(Date.week_cardinal.custom(FROM_STR_TO_INT.__getitem__)),
        WEEK_ORIG,
        WEEK_WORD
    ),
    rule(
        eq('за').interpretation(Date.week_cardinal.custom(normalize_float)),
        or_(ADJF),

        WEEK_WORD
    ),
    rule(
        or_(INT, NUMR, ADJF).optional().interpretation(Date.week_cardinal.custom(FROM_STR_TO_INT.__getitem__)),
        WEEK_MODIFIER,
        WEEK_WORD
    ),
    rule(
        #or_(INT, NUMR).optional().interpretation(Date.count.custom(FROM_STR_TO_INT.__getitem__)),
        MONTH_MODIFIER,
        MONTH_WORD
    ),
    rule(
        #or_(INT, NUMR).optional().interpretation(Date.count.custom(FROM_STR_TO_INT.__getitem__)),
        MONTH_STR,
        MONTH_WORD
    ),

    rule(

        MONTH_NAME,
        MONTH_WORD.optional()
    ),
    rule(

        MONTH_CARDINAL,
        MONTH_WORD
    ),
    rule(

        QUATER_INT,
        QUATER_WORD
    ),

    rule(
        or_(INT, NUMR).optional().interpretation(Date.count.custom(FROM_STR_TO_INT.__getitem__)),
        QUATER_ADJF,
        QUATER_WORD
    ),
    rule(
        #or_(INT, NUMR).optional().interpretation(Date.count.custom(FROM_STR_TO_INT.__getitem__)),
        YEAR_STR,
        YEAR_WORD
    ),
    rule(
        ALL_WORD.interpretation(Date.half_year.normalized().custom(FROM_STR_TO_INT.__getitem__)),
        or_(eq('полугодие'), eq('полугодия'))

    ),
    # rule(
    #
    #     YEAR_WORD,
    #     or_(INT, NUMR).interpretation(Date.year_modifier),
    #     eq('назад')
    # ),
    rule(
        #YEAR_INT,
        INT.interpretation(Date.year_cardinal.custom(int)),
        YEAR_WORD
    ),
    rule(
        #YEAR_INT,
        NUMR.interpretation(Date.year_cardinal.custom(FROM_STR_TO_INT.__getitem__)),
        YEAR_WORD
    ),
    # rule(
    #     #or_(INT, NUMR).optional().interpretation(Date.count.custom(FROM_STR_TO_INT.__getitem__)),
    #     YEAR,  # .optional(),
    #     YEAR_WORD
    # ),
    # rule(
    #     YEAR_SHORT,
    #     YEAR_WORD
    # ),
    # rule(
    #     or_(INT, NUMR).optional().interpretation(Date.year_cardinal),
    #     YEAR_WORD,
    #     #eq('назад').optional().interpretation(Date.year_cardinal.custom(FROM_STR_TO_INT.__getitem__))
    # ),
    #rule(
    #     YEAR
    #)
).interpretation(
    Date
)
