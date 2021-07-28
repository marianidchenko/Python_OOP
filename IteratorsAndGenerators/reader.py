def read_next(*args):
    current_arg_i = 0
    current_index = 0
    current_arg = args[current_arg_i]
    while current_index < len(current_arg) and current_arg_i < len(args):
        current_arg = args[current_arg_i]
        if isinstance(current_arg, dict):
            current_arg = list(current_arg.items())
        yield str(current_arg[current_index])
        current_index += 1
        if not current_index < len(current_arg):
            current_arg_i += 1
            current_index = 0


# test zero
import unittest

class Tests(unittest.TestCase):
    def test_zero(self):
        res = ''
        for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
            res += item
        self.assertEqual(res, 'string2dict')

if __name__ == '__main__':
    unittest.main()