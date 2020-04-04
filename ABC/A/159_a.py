import sys
from io import StringIO
import unittest


def resolve():
    guusuu, kisuu = map(int, input().split())
    guusuuhairetu = [i for i in range(2, guusuu * 2 + 1, 2)]
    kisuuhairetu = [i for i in range(1, kisuu * 2, 2)]
    count = 0
    haiiretu = guusuuhairetu + kisuuhairetu
    hairetu2 = guusuuhairetu + kisuuhairetu
    for i in hairetu2:
        haiiretu.remove(i)
        for u in haiiretu:
            if (i + u) % 2 == 0:
                count += 1
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
        input = """2 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """13 3"""
        output = """81"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """0 3"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
