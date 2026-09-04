from calculator import add, subtract, multiply, divide, power

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False, "Expected an error but didn't get one"
    except ValueError:
        assert True
def test_power():
    assert power(2, 3) == 8