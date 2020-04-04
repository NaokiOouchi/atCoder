import sys
from io import StringIO
import unittest


def resolve():
    # 3 * 3 の配列ができる
    bingoArr = [list(map(int, list(input().split()))) for i in range(3)]

    # 試行回数
    N = int(input())

    # ターゲット
    target = [int(input()) for i in range(N)]

    # [84 97 66]
    for i in range(0, len(bingoArr)):
        for y in range(0, len(bingoArr[i])):
            for t in target:
                if bingoArr[i][y] == t:
                    bingoArr[i][y] = -1
    res = 'No'
    if bingoArr[0][0] == -1 and bingoArr[0][1] == -1 and bingoArr[0][2] == -1:
        res = 'Yes'

    if bingoArr[1][0] == -1 and bingoArr[1][1] == -1 and bingoArr[1][2] == -1:
        res = 'Yes'

    if bingoArr[2][0] == -1 and bingoArr[2][1] == -1 and bingoArr[2][2] == -1:
        res = 'Yes'

    if bingoArr[0][0] == -1 and bingoArr[1][0] == -1 and bingoArr[2][0] == -1:
        res = 'Yes'

    if bingoArr[0][1] == -1 and bingoArr[1][1] == -1 and bingoArr[2][1] == -1:
        res = 'Yes'

    if bingoArr[0][2] == -1 and bingoArr[1][2] == -1 and bingoArr[2][2] == -1:
        res = 'Yes'

    if bingoArr[0][0] == -1 and bingoArr[1][1] == -1 and bingoArr[2][2] == -1:
        res = 'Yes'

    if bingoArr[0][2] == -1 and bingoArr[1][1] == -1 and bingoArr[2][0] == -1:
        res = 'Yes'

    print(res)


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
        input = """84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """41 7 46
26 89 2
78 92 8
5
6
45
16
57
17"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """60 88 34
92 41 43
65 73 48
10
60
43
88
11
48
73
65
41
92
34"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
