from appearence import bcolors


def fillCaseWorkerManager(cursor):

    caseworker_id = input(f"Type {bcolors.BOLD}Caseworker Id{bcolors.ENDC}: ").strip()
    manager_id = input(f"Type {bcolors.BOLD}Manager Id{bcolors.ENDC}: ").strip()
    try:
        cursor.execute(
            f"UPDATE AFU_House SET caseworker_id={caseworker_id}, manager_id={manager_id} WHERE caseworker_id=''")
        cursor.commit()
        print("Update Caseworker and Manager SUCCESS!")
    except Exception as inst:
        print(f"{bcolors.FAIL}Update House Failed{bcolors.ENDC}: {inst}")
    input("\nPress enter to continue")
    return caseworker_id, manager_id
