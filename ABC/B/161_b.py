import sys
from io import StringIO
import unittest


def resolve():
    # N種類の商品
    # i 商品
    # 得票数はA[i]
    # 人気商品をM個えらぶ
    # 得票数の1/4 * 　M未満はNo それ以外はYes
    # 1 <= M <= N <= 100

    N, M = map(int, input().split())
    listA = list(map(int, input().split()))
    i = len(listA)
    tokuhyousuu = sum(listA)
    a = -(-tokuhyousuu // (4 * M))
    ninnkiList = [i for i in listA if not i < a]
    ninnkisyouhinn = len(ninnkiList)
    if ninnkisyouhinn < M:
        print('No')
    else:
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
        input = """4 1
5 4 2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
380 19 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 3
4 56 78 901 2 345 67 890 123 45 6 789"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 2
1000 2"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
