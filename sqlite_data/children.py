from sqlite_data.databasesqlite import sqlite_cnx, sqlite_cursor


def getChild(child_id):
    sql_get_child = f"select * from children_comm where child_id='{child_id}'"
    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_get_child)
        record = sqlite_cursor.fetchone()
        if record:
            return record
    return "Empty record"


def getCommunity(child_id):
    sql_get_child = f"select * from children_comm where child_id='{child_id}'"
    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_get_child)
        record = sqlite_cursor.fetchone()
        if record:
            print(record[1])
            if record[6].strip() != "Eligible":
                return "Ineligible"
            return record[3]
    return "Empty record"


def getSchool(child_id):
    sql_get_child = f"select school_name from children_comm where child_id='{child_id}'"
    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_get_child)
        record = sqlite_cursor.fetchone()
        if record:
            return record[0]
    return "Empty record"

