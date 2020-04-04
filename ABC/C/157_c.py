import sys
from io import StringIO
import unittest


def resolve():
    # Nが回答の桁数
    # Mが後続入力の行数
    N, M = map(int, input().split())
    s = [list(map(int, list(input().split()))) for i in range(M)]

    ans = [-1] * N

    for i in s:
        if ans[i[0] - 1] != -1 and ans[i[0] - 1] != i[1]:
            print(-1)
            exit()
        ans[i[0] - 1] = i[1]

    if M == 0 and N != 1:
        ans[0] = 1
    tmp = int(''.join((map(str, [int(str(a).replace('-1', '0')) for a in ans]))))
    if N >= 2 and ans[0] == -1:
        ans[0] = 1

    ans = [int(str(a).replace('-1', '0')) for a in ans]

    res = ''.join((map(str, ans)))
    if int(res) >= 0 and len(str(int(res))) == N:
        print(int(res))
    else:
        print(-1)


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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 2
    1 0
    2 1"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """2 3 
        2 0
        2 0
        2 0"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """3 1 
        2 1 """
        output = """110"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
