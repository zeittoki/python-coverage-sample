import io
import sys
import unittest

from main import main


def stub_stdin(testcase_inst, inputs):
    stdin = sys.stdin

    def cleanup():
        sys.stdin = stdin

    testcase_inst.addCleanup(cleanup)
    sys.stdin = io.StringIO(inputs)


def stub_stdouts(testcase_inst):
    stdout = sys.stdout

    def cleanup():
        sys.stdout = stdout

    testcase_inst.addCleanup(cleanup)
    sys.stdout = io.StringIO()


class MainTestCase(unittest.TestCase):
    def test_main(self):
        input_value = ""

        with open("./input.txt") as f:
            input_value = f.read()

        # 標準入力をモック
        stub_stdin(self, input_value)
        # 標準出力をモック
        stub_stdouts(self)

        main()


if __name__ == "__main__":
    unittest.main()
