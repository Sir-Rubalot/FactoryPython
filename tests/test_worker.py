import unittest
from app.worker import add_worker, list_workers

class TestWorker(unittest.TestCase):

    def test_add_worker(self):
        worker_list = []
        add_worker("Maja", worker_list)
        add_worker("Charlie", worker_list)

        result = list_workers(worker_list)
        self.assertIn("Maja", result)
        self.assertIn("Charlie", result)
        self.assertEqual(len(result), 2)


if __name__ == '__main__':
    unittest.main()