import sys
from io import StringIO
import unittest


def resolve():
    a = int(input())
    b = [i for i in range(a)]
    x, y, z = 0, 0, 0
    an = 0
    # x * y * zの答えが一番でかい数字を出力
    for x in b:
        if x * y * z > an:
            an = x * y * z
        if x > 0:
            x = x - 1
        for y in range(x):
            if x * y * z > an:
                an = x * y * z
            if y > 0:
                y = y - 1
            for z in range(y):
                if x * y * z > an:
                    an = x * y * z
    print(an)


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
        input = """3"""
        output = """1.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """999"""
        output = """36926037.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
