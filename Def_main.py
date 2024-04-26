def test(a, b):
    print(a, b)

def test2(c, d, e):
    print(c, d, e)

test(1, 2)
test2(3, 4, 5)

def test3(a=3, b=6, c=9):
    print(a, b, c)
    print(a+b+c)

test3()


def test4(a='a', b='and', c='b'): # сидели на трубе
    print(a, b, c)

test4(a='a-упало,', b='b-пропало,', c='что осталось?')