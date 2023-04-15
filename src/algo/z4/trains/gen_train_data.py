"""
System "pocigągów" ... de facto połączeń między miastami reprezentowanymi przez liczby

[(4,8), (1,3), (2,2), (3, 1), (1,10)]


"""
from collections import defaultdict
from random import randint, seed
from a import *
from b import *
from c import *
from d import *
from collections import defaultdict
import pprint

N_CITIES = 10
seed(111)


def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res

def generate_data_alt(data_size):
    res = defaultdict(set)
    for i in range(data_size):
        res[randint(0, N_CITIES - 1)].add(randint(0, N_CITIES - 1))
    return res



def show_schedule(schedule):
    print ("Train schedule:")
    schedule = sorted(set(schedule))
    
    p = 0
    for i in schedule:
        if p != i[0]:
            print()
            p = i[0]
        print (i, end=' ')
    print()

if __name__ == '__main__':
    train_schedule = generate_data(20)
    print (train_schedule)
    show_schedule(train_schedule)
    #Zadanie A
    print ("Zadanie A: \n", get_city_most_connections(train_schedule))
    #Zadanie B 
    print ("Zadanie B: \n", is_connected(train_schedule, 14, 4))
    #Zadanie C 
    print ("Zadanie C: \n", is_connected_with_stopover(train_schedule, 17, 11))
    #Zadanie D 
    print ("Zadanie D: \n", find_longest_trip(train_schedule))
    
    train_schedule_2 = generate_data_alt(20)
    pprint.pprint (train_schedule_2)
    
    # Zadanie A
    print ("Zadanie A: \n", get_city_most_connections_alt(train_schedule_2))
    #Zadanie B 
    # print ("Zadanie B: \n", is_connected_alt(train_schedule, 14, 4))
    # #Zadanie C 
    # print ("Zadanie C: \n", is_connected_with_stopover_alt(train_schedule, 17, 11))
    # #Zadanie D 
    # print ("Zadanie D: \n", find_longest_trip_alt(train_schedule))
    
    # train_schedule = generate_data(10)
    # print(train_schedule)
