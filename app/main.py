import datetime
import sys
from worker import Worker
from database import Database
from errorcodes import WorkerNotFoundError

worker_list = []

while True:
    print("Välkommen!")
    print("[1] Stämpla in.")
    print("[2] Stämpla ut.")
    print("[3] Visa tidbank.")
    print("[4] Visa instämplade kollegor.")
    print("[0] Avsluta. ")
    user_choice = input(">: ").strip()

    if user_choice == "1":
        worker_name = input(f"Vem ska stämpla in? ")
        worker_list.append(Worker(worker_name))
        Database.save_to_file(worker_list)
        #worker = Worker.add_worker(new_worker_name, worker_list)
                                                    #här ska man fråga om klockslag arbetaren stämplar in. 
        print(f"Arbetare {worker_name} har nu stämplat in.")
    elif user_choice == "2":
        try:
            worker_name = input("Vem ska stämpla ut? ")
            Worker.remove_worker(worker_name, worker_list)
            print(f"{worker_name} har nu stämplat ut.")
        except KeyError:
            print("Denna koden skrivs inte ut")
        except WorkerNotFoundError:
                print(f"{worker_name} hittades inte. Är personen instämplad?")
        finally:
            Worker.list_workers(worker_list)
    elif user_choice == "4":
        Worker.list_workers(worker_list)
    elif user_choice == "0":
        print("Avslutar.")
        sys.exit()
    else:
        print("Ogiltigt val. Välj ett alternativ i menyn.")
