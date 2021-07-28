def solution():

    def integers():
        current_num = 1
        while True:
            yield current_num
            current_num += 1

    def halves():
        for i in integers():
            yield i/2

    def take(n, sequence):
        result = []
        for i in range(n):
            result.append(next(sequence))
        return result

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))


# test zero
import unittest

class TakeHalvesTests(unittest.TestCase):
    def test_zero(self):
        take = solution()[0]
        halves = solution()[1]
        result = take(5, halves())
        self.assertEqual(result, [0.5, 1.0, 1.5, 2.0, 2.5])

if __name__ == '__main__':
    unittest.main()