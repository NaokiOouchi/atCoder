import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())  # 1行目のNを取得する
    s = list(map(int, input().split()))  # 複数行の数値の入力を取得
    count = 0
    tmpListLen = len(s)
    halfList = list(filter(lambda x: x % 2 == 0, s))  # 値が偶数のものだけにフィルター

    while tmpListLen == len(halfList):
        count += 1
        halfList = map(lambda x: x / 2, halfList)
        halfList = list(filter(lambda x: x % 2 == 0, halfList))
    print(count)


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
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
