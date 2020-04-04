import sys
from io import StringIO
import unittest


def resolve():
    s = input()
    # sは回文
    # n = s.len
    # lenの1文字目から(len - 1)/2 までからなる文字列は回文
    # sの(len + 3 )/2 から　lenまでからなる文字列は回文

    moji1 = s[: int((len(s) - 1) / 2)]
    moji2 = s[int((len(s) + 2) / 2): int(len(s))]

    moji3 = s[: int((len(s) - 1) / 2)]
    moji4 = s[int((len(s) + 2) / 2): int(len(s))]
    while int(len(moji1)) > 1:
        a = moji1[0:1]
        b = moji1[-1]
        if a != b:
            print('No')
            exit()
        moji1 = moji1[1:-1]
    if (moji3 != moji4):
        print('No')
        exit()
    print('Yes')


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
        input = """akasaka"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """level"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
