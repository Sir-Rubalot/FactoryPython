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
    
    def check_in(self, time_in):
        self.time_in = time_in

    def check_out(self, time_out):
        self.time_out = time_out

