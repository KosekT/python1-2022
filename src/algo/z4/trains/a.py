"""
zadanie1:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
 połączeń wychodzących.

"""

def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    return max([x[0] for x in train_data], key = [x[0] for x in train_data].count)

from collections import defaultdict
import pprint
def get_city_most_connections_alt(train_data: defaultdict(set)) -> int:
    print (train_data)
    pprint.pprint (train_data)
    for x,y  in train_data:
        print (x)
    return 2
    return max(x.count for x in train_data)

from collections import Counter
def get_city_most_connections_socrates(train_data: list[tuple[int,int]]) -> int:
    return Counter(map(lambda x:x[0] ,train_data)).most_common(1)[0][0]