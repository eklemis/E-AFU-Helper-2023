import pyodbc
from os import path
import getpass

from appearence import bcolors
from os.path import basename

def setConnection(db_path):
    print(f"{bcolors.HEADER}{bcolors.BOLD}##SETUP E-AFU CONNECTION##{bcolors.ENDC}{bcolors.ENDC}")

    try:
        #db_path = ACCESS_DB_PATH
        print(f"Default db path: {bcolors.WARNING}{db_path}{bcolors.ENDC}")
        new_path = input(f"Type new path or {bcolors.BOLD}*press Enter to skip{bcolors.ENDC}: ")
        if new_path == "":
            print(f"New path is {bcolors.BOLD}EMPTY{bcolors.ENDC}, using default path")
        elif path.exists(new_path):
            db_path = new_path
        else:
            print(f"New path is {bcolors.BOLD}NOT EXIST{bcolors.ENDC}, using default path")
        encrypted_key = getpass.getpass(prompt='Encryption key: ')
        conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=' + db_path + f";PWD={encrypted_key}")
        cursor = conn.cursor()
        print(f"Connected to: {bcolors.BOLD}{basename(db_path)}{bcolors.ENDC}")
        return cursor, db_path
    except Exception as inst:
        print("Connection failed! Please check your connection string!")
        print(inst)
        return -1, db_path

# TESTED MANUALLY

