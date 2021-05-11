from test import accuracy


def acc(dict):
    true_day_ordinal = {'за второй день третьей недели второго квартала': 2}
    print(accuracy(true_day_ordinal, dict))