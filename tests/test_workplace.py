import unittest
from workplace import Workplace

class TestWorkplace(unittest.TestCase):
    def test_worker_list(self):
        w1 = Worker("Maja")
        w2 = Worker("Charlie")
        worker_list = [w1, w2]

        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output

        output = captured_output.getvalue()
        self.assertIn("Maja", output)
        self.assertIn("Charlie", output)

if __name__ == '__name__':
    unittest.main()