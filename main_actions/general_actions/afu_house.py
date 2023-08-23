from appearence import bcolors


def fillCaseWorkerManager(cursor, caseworker_id='33285', manager_id='33285'):
    try:
        cursor.execute(
            f"UPDATE AFU_House SET caseworker_id={caseworker_id}, manager_id={manager_id} WHERE caseworker_id=''")
        cursor.commit()
        return True
    except Exception as inst:
        print(f"{bcolors.FAIL}Update House Failed{bcolors.ENDC}: {inst}")
        return False


def repairErrorHouses(cursor):
    print("Getting the failed house ids...")
    cursor.execute(
        "SELECT house_id FROM AFU_House WHERE Len([date_completed])>0 and IsNull(Len(date_imported_to_ASISt)) = -1")
    res = cursor.fetchall()
    failed_afu_ids = [item[0] for item in res]
    content = ""
    count = 1
    for house_id in failed_afu_ids:
        print(f"Found error on house {house_id} ({count}/{len(failed_afu_ids)})")
        content = content + f"{house_id},"
    content = content[0:len(content) - 1]
    str_failed_afu_ids = "(" + content + ")"

    if len(failed_afu_ids) > 0:
        print("Start repairing...")
        print(str_failed_afu_ids)
        cursor.execute("UPDATE AFU_House SET proc_status='NEW' where house_id in " + str_failed_afu_ids)
        cursor.commit()
        print("Done repairing!")
    else:
        print("No problem found!")

