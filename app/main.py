import datetime
import sys
from worker import Worker
from database import Database
from errorcodes import WorkerNotFoundError
from workplace import Workplace

worker_list = Database.load_from_file()

while True:
    print("Välkommen!")
    print("[1] Stämpla in.")
    print("[2] Stämpla ut.")
    print("[3] Visa instämplade kollegor.")
    print("[0] Avsluta. ")
    user_choice = input(">: ").strip()

    if user_choice == "1":
        worker_name = input(f"Vem ska stämpla in? ")
        try:
            time_str = input("När började du? (HH:MM) ")
            time_str_formatted = Workplace.parse_time(time_str)
        except ValueError:
            print("Ogiltig inmatning. Skriv i formatet (HH:MM)")
        worker = Worker(worker_name)
        time_in = Workplace.parse_time(time_str)
        worker.check_in(time_str_formatted)
        worker_list.append(worker)
        print(f"Arbetare {worker_name} har nu stämplat in kl {time_in}")
        Database.save_to_file(worker_list)
    elif user_choice == "2":
        try:
            worker_name = input("Vem ska stämpla ut? ")
            time_out_str = input("När slutade du? (HH:MM) ")
            worker_list = Database.load_from_file("db.json")
            time_out = Workplace.parse_time(time_out_str)
            Database.delete_from_file(worker_name)
            print(f"{worker_name} har stämplat ut kl {time_out_str}.")
            worker_list = Database.load_from_file()
        except KeyError:
            print("Denna koden skrivs inte ut")
        except WorkerNotFoundError:
                print(f"{worker_name} hittades inte. Är personen instämplad?")
        finally:
            Worker.list_workers(worker_list)
    elif user_choice == "3":
        if len(worker_list) < 1:
            print("Inga kollegor jobbar just nu.")
        else:
            print("Incheckade kollegor:")
        for worker in worker_list:
            print(f" - {worker.name}")
    elif user_choice == "0":
        print("Avslutar.")
        sys.exit()
    else:
        print("Ogiltigt val. Välj ett alternativ i menyn.")