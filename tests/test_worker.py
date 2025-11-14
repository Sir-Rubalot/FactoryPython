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

    def test_worker_list(self):
        worker1 = Worker("Maja")
        worker2 = Worker("Charlie")
        self.worker_list.append(worker1)
        self.worker_list.append(worker2)

        self.assertIn(worker1, self.worker_list)
        self.assertIn(worker2, self.worker_list)
        self.assertEqual(len(self.worker_list), 2)

    def test_remove_worker(self):
        worker = Worker("Robin")
        self.worker_list.append(worker)
        self.worker_list.remove(worker)

        self.assertNotIn(worker, self.worker_list)
        self.assertEqual(len(self.worker_list), 0)

if __name__ == '__main__':
    unittest.main()