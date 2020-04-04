import sys
from io import StringIO
import unittest


def resolve():
    import fractions

    n, k = map(int, input().split())
    if (n > abs(n - k)):
        n = fractions.gcd(n, k)
    while n > abs(n - k):
        n = abs(n - k)
    if n == k:
        print('0')
    else:
        print(n)


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
        input = """7 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1000 1000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
