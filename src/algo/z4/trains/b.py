

"""
zadanie2:
 Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
 z miasta "a" do miasta "b" (bez przesiadek).

"""

def is_connected(train_data: list[tuple[int,int]], a: int, b: int) -> bool:
    return train_data.count((a,b)) > 0

    # Alternatywnie
    for i in train_data:
        if i == (a, b):
            return True
    return False