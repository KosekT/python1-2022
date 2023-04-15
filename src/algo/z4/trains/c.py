"""
zadanie3:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" z dokładnie jedną przesiadką, czyli czy istnieje para połączeń typu (a,c),(c,b).

"""


def is_connected_with_stopover(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    a_l, b_l = [], []
    for i in train_data:
        if i[0] == a:
            if i[1] in b_l:
                return True
            a_l.append(i[1])
        if i[1] == b:
            if i[0] in a_l:
                return True
            b_l.append(i[0])
    return False
