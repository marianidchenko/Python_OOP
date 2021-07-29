def logged(func):
    def wrapper(*args):
        function_as_text = func.__name__ + str(args)
        result = func(*args)
        return f"you called {function_as_text}\nit returned {result}"
    return wrapper


# test zero
import unittest

class LoggedTests(unittest.TestCase):
    def test_zero(self):
        @logged
        def func(*args):
            return 3 + len(args)
        result = func(4, 4, 4)
        self.assertEqual(result, 'you called func(4, 4, 4)\nit returned 6')

if __name__ == '__main__':
    unittest.main()