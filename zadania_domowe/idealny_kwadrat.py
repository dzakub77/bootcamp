import math
def perfect_square(x):
    try:
        y = math.sqrt(x)
        if y == int(y):
            return True
        else:
            return False
    except TypeError:
        return TypeError
    except ValueError:
        return False




def test_perfect_square():
    assert perfect_square(9) == True
    assert perfect_square(-3) == False
    assert perfect_square("asdasdasd") == TypeError
    assert perfect_square(4624000000000000) == True
    assert perfect_square(15) == False