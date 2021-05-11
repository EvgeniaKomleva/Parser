

# dict_ = {}
# dict_ = {}
def skip_none(arr):
  #print("arr", arr)
  out = ''
  for el in arr:
    #print(el)
    if el != None:
      out = el
  return out


def viz(str_num, date, line, matches, dict_num_day_ordinal,
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
        dict_week_modifier, dict_count, dict_day_modifier, dict_half_year):
    for match in matches:
        date.day_modifier.append(match.fact.day_modifier)
        date.half_year.append(match.fact.half_year)
        date.quarter_cardinal.append(match.fact.quarter_cardinal)
        date.quarter_ordinal.append(match.fact.quarter_ordinal)
        date.year_modifier.append(match.fact.year_modifier)
        date.year_cardinal.append(match.fact.year_cardinal)
        date.week_modifier.append(match.fact.week_modifier)
        date.week_ordinal.append(match.fact.week_ordinal)
        date.week_cardinal.append(match.fact.week_cardinal)
        date.month_ordinal.append(match.fact.month_ordinal)
        date.month_cardinal.append(match.fact.month_cardinal)
        date.month_modifier.append(match.fact.month_modifier)
        date.day_cardinal.append(match.fact.day_cardinal)
        date.day_ordinal.append(match.fact.day_ordinal)
        date.start_date.append(match.fact.start_date)
        date.end_date.append(match.fact.end_date)
        date.day_modifier.append(match.fact.day_modifier)
        date.half_year.append(match.fact.half_year)
        date.count.append(match.fact.count)
        date.date.append(match.fact.date)
        # date.day.append(match.fact.day)
    if len(str(skip_none(date.quarter_cardinal))) > 0:
        print("quarter_cardinal: ", skip_none(date.quarter_cardinal))
        dict_quarter_cardinal["{}".format(line)] = skip_none(date.quarter_cardinal)
    if len(str(skip_none(date.quarter_ordinal))) > 0:
        print("quarter_ordinal: ", skip_none(date.quarter_ordinal))
        dict_quarter_ordinal["{}".format(line)] = skip_none(date.quarter_ordinal)
    if len(str(skip_none(date.year_modifier))) > 0:
        print("year_modifier: ", skip_none(date.year_modifier))
        dict_year_modifier["{}".format(line)] = skip_none(date.year_modifier)
    if len(str(skip_none(date.year_cardinal))) > 0:
        print("year_cardinal: ", skip_none(date.year_cardinal))
        dict_year_cardinal["{}".format(line)] = skip_none(date.year_cardinal)

    if len(str(skip_none(date.date))) > 0:
        print("date: ", skip_none(date.date))
        dict_date["{}".format(line)] = skip_none(date.date)
    if len(str(skip_none(date.week_ordinal))) > 0:
        print("week_ordinal: ", skip_none(date.week_ordinal))
        dict_week_ordinal["{}".format(line)] = skip_none(date.week_ordinal)
    if len(str(skip_none(date.week_cardinal))) > 0:
        print("week_cardinal: ", skip_none(date.week_cardinal))
        dict_week_cardinal["{}".format(line)] = skip_none(date.week_cardinal)
    if len(str(skip_none(date.week_modifier))) > 0:
        print("week_modifier: ", skip_none(date.week_modifier))
        dict_week_modifier["{}".format(line)] = skip_none(date.week_modifier)
    if len(str(skip_none(date.month_ordinal))) > 0:
        print("month_ordinal: ", skip_none(date.month_ordinal))
        dict_month_ordinal["{}".format(line)] = skip_none(date.month_ordinal)
    if len(str(skip_none(date.month_cardinal))) > 0:
        print("month_cardinal: ", skip_none(date.month_cardinal))
        dict_month_cardinal["{}".format(line)] = skip_none(date.month_cardinal)
    if len(str(skip_none(date.month_modifier))) > 0:
        print("month_modifier: ", skip_none(date.month_modifier))
        dict_month_modifier["{}".format(line)] = skip_none(date.month_modifier)
    if len(str(skip_none(date.day_cardinal))) > 0:
        print("day_cardinal: ", skip_none(date.day_cardinal))
        dict_day_cardinal["{}".format(line)] = skip_none(date.day_cardinal)
    if len(str(skip_none(date.day_ordinal))) > 0:
        print("day_ordinal: ", skip_none(date.day_ordinal))
        dict_num_day_ordinal["{}".format(line)] = skip_none(date.day_ordinal)
    if len(str(skip_none(date.start_date))) > 0:
        print("start_date: ", skip_none(date.start_date))
        dict_start_date["{}".format(line)] = skip_none(date.start_date)
    if len(str(skip_none(date.end_date))) > 0:
        print("end_date: ", skip_none(date.end_date))
        dict_end_date["{}".format(line)] = skip_none(date.end_date)
    if len(str(skip_none(date.day_modifier))) > 0:
        print("day_modifier: ", skip_none(date.day_modifier))
        dict_day_modifier["{}".format(line)] = skip_none(date.day_modifier)
    if len(str(skip_none(date.half_year))) > 0:
        print("half_year: ", skip_none(date.half_year))
        dict_half_year["{}".format(line)] = skip_none(date.half_year)
    if len(str(skip_none(date.count))) > 0:
        print("count: ", skip_none(date.count))
        dict_count["{}".format(line)] = skip_none(date.count)
