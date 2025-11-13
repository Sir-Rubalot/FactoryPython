import datetime

class Factory():
    def __init__(self, name):
    
    

    def worker_list(worker_list, filename = "db.json"):
        data = [{"name": worker.name} for worker in worker_list]
        save_to_file(data, filename)