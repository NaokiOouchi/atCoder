import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    s = list(map(int, input().split()))
    s.sort(reverse=True)
    a = []
    b = []
    for i in range(N):
        if i % 2 == 0:
            a.append(s.pop(0))
        else:
            b.append(s.pop(0))
    print(sum(a) - sum(b))


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
3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2 7 4"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
20 18 2 18"""
        output = """18"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
