from datetime import time
from database import Database

class Workplace():
    def __init__(self, name):
        self.name = name

    @staticmethod
    def worker_list(worker_list, filename = "db.json"):
        data = [{"name": worker.name} for worker in worker_list]
        Database.save_to_file(data, filename)

    @staticmethod
    def parse_time(time_str):
        hour, minute = map(int, time_str.split(":"))
    
        return time(hour, minute)
    