def resolve():
    a, b = map(int, input().split())
    c = a * b
    if c % 2 == 0:
        print('Even')
    else:
        print('Odd')


import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 4"""
        output = """Even"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 21"""
        output = """Odd"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
