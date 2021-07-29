def type_check(type):
    def decorator(func):
        def wrapper(thing):
            if isinstance(thing, type):
                result = func(thing)
                return result
            return "Bad Type"
        return wrapper
    return decorator


# test first zero
import unittest

class TypeCheckTests(unittest.TestCase):
    def test_zero_first(self):
        @type_check(int)
        def times2(num):
            return num*2
        self.assertEqual(times2(2), 4)
        self.assertEqual(times2('Not A Number'), 'Bad Type')

if __name__ == '__main__':
    unittest.main()