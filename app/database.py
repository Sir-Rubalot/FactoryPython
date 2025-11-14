import json
from worker import Worker
from errorcodes import WorkerNotFoundError

class Database():
    def __init__(self):
        pass
        
    @staticmethod
    def save_to_file(worker_list, filename = "db.json"):
        data = [{"name": worker.name} for worker in worker_list]
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_from_file(filename="db.json") -> list:
        worker_list = []
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for item in data:
                    worker = Worker(item['name'])
                    worker_list.append(worker)
        except FileNotFoundError:
            worker_list = []
            Database.save_to_file(worker_list, filename)
        return worker_list
    
    def update_file(worker_name, filename="db.json"):
        data = [{"name": worker.name} for worker in worker_list]
        with open(filename, 'w') as f:
            json.dump(data, f)

    def delete_from_file(worker_name, filename="db.json"):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            if not any(item.get("name") == worker_name for item in data):
                raise WorkerNotFoundError(f"Anställd {worker_name} kunde inte hittas")
            data = [item for item in data if item.get("name") != worker_name]
            with open(filename, 'w') as f:
                json.dump(data, f)
        except FileNotFoundError:
            print("Fil kunde inte hittas.")