import datetime
import json
from pydantic import BaseModel
from errorcodes import WorkerNotFoundError

class Worker():
    def __init__(self, name):
        self.name = name
        self.time_in = None
        self.time_out = None

    def __str__(self):
        return f"Anställd: {self.name}"

    @staticmethod
    def add_worker( name, worker_list):
        new_worker = Worker(name)
        worker_list.append(new_worker)
        return new_worker
    
    @staticmethod
    def remove_worker( worker_name, worker_list):
        for worker in worker_list:
            if worker.name == worker_name:
                #worker.check_out(datetime.time())
                #work_time = worker.get_work_time()
                worker_list.remove(worker)
                return
        raise WorkerNotFoundError(f"{worker_name} hittades inte. Är personen instämplad?")
    
    @staticmethod
    def worker_list( name, worker_list):
        new_worker = Worker(name)
        worker_list.append(new_worker)
        return new_worker
    
    @staticmethod
    def list_workers(worker_list):
        print("Instämplade kollegor:")
        for worker in worker_list:
            print(worker)
    
    def check_in(self):
        self.time_in = datetime.datetime()

    def check_out(self):
        self.time_out = datetime.datetime()


    