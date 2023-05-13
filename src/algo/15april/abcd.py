#   A
def check_unique(list):
    return len(list) == len(set(list))

s = ['aa', 'a', 'c', 'bb']
if check_unique(s):
    print("List unique!")
else:
    print("List not unique")
    

#   B
s=['aa', 'aa', 'c', 'bb']
def zad_b(s):
    if len(s) == len(set(s)):
        print("List unique.")
    else:
        print("list contains duplicates:")
        duplicates = []
        for i in set(s):
            if s.count(i) > 1:
                duplicates.append(i)
        print(duplicates)
zad_b(s)    
    
#   C

w = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]    
#dla id=5 pojawiają się 2 różne names, dla name='Jane' pojawiają się 2 różne id's
def uniq_id(w):
    l = set([x[0] for x in w])
    if len(l) < len(w):
        print("List id are NOT unique.")
    print("List id are unique.")
uniq_id(w)

#   D
z = [(1,'Adam'), (2,'Jane'), (3, 'Xiao'), (4,'Jade')] 
# dla każdego id przypisany jest unikalny name; dla każdego name przypisany jest unikalny id 
def uniq_name(z):
    l = set([x[1] for x in z])
    if len(l) < len(w):
        print("List names are NOT unique.")
    print("List names are unique.")
uniq_name(z)