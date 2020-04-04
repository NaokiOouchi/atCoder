import sys
from io import StringIO
import unittest
from Practice import WelcomeToAtCoder


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        WelcomeToAtCoder.resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """1
2 3
test"""
        output = """6 test"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """72
128 256
myonmyon"""
        output = """456 myonmyon"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
