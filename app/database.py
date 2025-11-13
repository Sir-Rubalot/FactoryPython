import json

class Database():
    def __init__(self):
        pass
        
    @staticmethod
    def save_to_file(worker_list, filename = "db.json"):
        data = [{"name": worker.name} for worker in worker_list]
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_from_file(filename="db.json"):
        worker_list = []
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                for item in data:
                    worker = worker(item['name'])
                    worker_list.append(worker)
        except FileNotFoundError:
            pass
        return worker_list
    
    def update_file(worker_list, filename="db.json"):
        data = [{"name": worker.name} for worker in worker_list]
        with open(filename, 'w') as f:
            json.dump(data, f)

    def delete_from_file(worker_list, filename="db.json"):
        try:
            with open(filename, 'r') as f:
                data = json.liad(f)
            data = [item for item in data if item.get("name") != target_name]
            with open(filename, 'w') as f:
                json.dump(data, f)
            print(f"Arbetare '{target_name}' har tagits bort.")
        except FileNotFoundError:
            print("Fil kunde inte hittas.")
