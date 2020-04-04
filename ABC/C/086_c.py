import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    s = [list(map(int, list(input().split()))) for i in range(N)]
    print(s)


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
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
