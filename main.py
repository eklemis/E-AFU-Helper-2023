from appearence import bcolors
from connection import setConnection
from main_actions.general_actions.caseworker_manager import fillCaseWorkerManager
from main_actions.general_actions.photo_tool import PhotoTool
from main_actions.general_actions.afu_house import repairErrorHouses
from helpers.app_config import loadAppSettings, saveAppSettings
from main_actions.general_actions.manual_afu import syncWithReport, copyFrom, getManualAfuDbFormat, profileDataAreValid
from main_actions.by_school_actions.child_attribute import ChildAttribute
from main_actions.general_actions.update_project_codes import updateProjectCode
import os


app_config = loadAppSettings()
current_eafu_path = app_config['eafu_path']
current_school = app_config['school']
current_cursor, current_eafu_path = setConnection(current_eafu_path)
current_caseworker_id = app_config['caseworker_id']
current_manager_id = app_config['manager_id']
current_image_photo_path = app_config['image_photo_path']
manual_afu_path = app_config['manual_afu_path']
latest_profiles_valid = False

while True:
    conn_status = f"{bcolors.BOLD}{bcolors.FAIL}Disconnected{bcolors.ENDC}{bcolors.ENDC}" if current_cursor == -1 else f"{bcolors.BOLD}{bcolors.OKGREEN}Connected{bcolors.ENDC}{bcolors.ENDC}"
    os.system('cls')
    print(f"{bcolors.BOLD}<----------------WELCOME TO E-AFU HELPER (2023)---------------->{bcolors.ENDC}")
    print(f"Current E-AFU Path: {bcolors.BOLD}{bcolors.WARNING}{current_eafu_path}{bcolors.ENDC}{bcolors.ENDC}, status: {conn_status}")
    print(f"Manual AFU path: {bcolors.BOLD}{bcolors.WARNING}{manual_afu_path}{bcolors.ENDC}{bcolors.ENDC}")
    print("\nPlease choose appropriate tasks below:")
    print(f"\n{bcolors.BOLD}## GENERAL PURPOSE TASKS{bcolors.ENDC}")

    print(f"1. Change {bcolors.BOLD}E-AFU App location{bcolors.ENDC} or {bcolors.BOLD}Reconnect{bcolors.ENDC}")
    print(f"2. Set E-AFU {bcolors.BOLD}Caseworker Id{bcolors.ENDC} and {bcolors.BOLD}Manager Id{bcolors.ENDC}")
    print(f"3. Repair {bcolors.BOLD}inconsistent date(completed and imported){bcolors.ENDC} on E-AFU House")
    print(f"4. {bcolors.BOLD}Rotate/Resize{bcolors.ENDC} Images")
    print(f"5. Copy {bcolors.BOLD}Profile Data{bcolors.ENDC} from other manual AFU")
    print(f"6. {bcolors.BOLD}Sync manual afu{bcolors.ENDC} with a ListOfChildrenAFUCollected.xlsx report")
    print(f"\n{bcolors.BOLD}## SCHOOL SPECIFIC TASKS{bcolors.ENDC}")
    print(f"Selected school: {bcolors.BOLD}{bcolors.WARNING}{current_school}{bcolors.ENDC}{bcolors.ENDC}")
    print(f"7. {bcolors.BOLD}Change School{bcolors.ENDC}")
    prof_check_status = f"{bcolors.OKGREEN}Valid{bcolors.ENDC}" if latest_profiles_valid else f"{bcolors.WARNING}Need Re-check{bcolors.ENDC}"
    print(f"8. Validate Profile Data (latest check: {bcolors.UNDERLINE}{prof_check_status}{bcolors.ENDC})")
    print(f"9. Push {bcolors.BOLD}Profile Data to E-AFU{bcolors.ENDC}")
    print(f"10. Push {bcolors.BOLD}New Photos to E-AFU{bcolors.ENDC}")
    print(f"11. {bcolors.BOLD}Zip{bcolors.ENDC} School {bcolors.BOLD}Photos{bcolors.ENDC}")
    print(f"12. Update project codes for selected E-AFU")
    print(f"\n15. Exit App")
    user_choice = input(f"\n{bcolors.BOLD}Enter your choice: {bcolors.ENDC}")
    user_choice = user_choice.strip()

    if user_choice == "1":
        os.system('cls')
        current_cursor, current_eafu_path = setConnection(current_eafu_path)
    elif user_choice == "2":
        current_caseworker_id, current_manager_id = fillCaseWorkerManager(current_cursor)
    elif user_choice == "3":
        if current_cursor != -1:
            repairErrorHouses(current_cursor)
        else:
            input("E-AFU disconnected, please reconnect! press enter to go back")

    elif user_choice == "4":
        photo_tool = PhotoTool(current_image_photo_path)
        current_image_photo_path = photo_tool.getPhotoPath()
    elif user_choice == "5":
        copyFrom(manual_afu_path)
    elif user_choice == "6":
        syncWithReport(manual_afu_path)
    elif user_choice == "7":
        new_school = input(f"Type new {bcolors.BOLD}School Name{bcolors.ENDC}: ")
        if new_school.strip() != "":
            current_school = new_school
            latest_profiles_valid = False
    elif user_choice == "8":
        if current_cursor != -1:
            filtered_manual_afu_db_format = getManualAfuDbFormat(manual_afu_path, current_school)
            latest_profiles_valid = profileDataAreValid(filtered_manual_afu_db_format, current_cursor)
        else:
            input("E-AFU disconnected, please reconnect! press enter to go back")
    elif user_choice == "9":
        if current_cursor != -1:
            child_attributes = ChildAttribute(manual_afu_path, current_school, latest_profiles_valid, current_cursor)
            profile_updated = child_attributes.runWholeProcess()
            if profile_updated:
                print("Successfully push profiles data to E-AFU!")
        else:
            input("E-AFU disconnected, please reconnect! press enter to go back")
    elif user_choice == "12":
        updateProjectCode(current_cursor)
    elif user_choice == "15":
        saveAppSettings({
            'eafu_path': current_eafu_path,
            'school': current_school,
            'caseworker_id': current_caseworker_id,
            'manager_id': current_manager_id,
            'image_photo_path': current_image_photo_path,
            'manual_afu_path': manual_afu_path
        })
        break

