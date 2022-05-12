x = 2
if x <= 0:
    raise Exception('x should be positive')

assert (x <= 5), 'x is less than 1'

try:
    a = 5 / 2
    b = a + int('10')
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up')


class ValueTooHighError(Exception):
    pass


class ValueTooSmallError(Exception):
    def __int__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value too small', x)


try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e)
