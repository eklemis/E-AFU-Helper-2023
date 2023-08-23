import os.path
from pathlib import Path


from databasesqlite import sqlite_cnx, sqlite_cursor

import pandas as pd

excels_dir = Path("D:\queries\#cor_manager")

def parsingChildCommunity():
    sql_create_childrenall_table = """ CREATE TABLE IF NOT EXISTS children_comm(
        child_id text,
        child_full_name,
        comm_id text NOT NULL,
        comm_name text NOT NULL,
        school_id text NOT NULL,
        school_name text NOT NULL,
        status_desc text NOT NULL
    ) """

    sql_drop_childrencomm_table = """ DROP TABLE IF EXISTS children_comm """
    if sqlite_cnx is not None:
        sqlite_cursor.execute(sql_drop_childrencomm_table)
        sqlite_cursor.execute(sql_create_childrenall_table)

    #retrive all data from CHILDREN_ALL.xlsx file
    childrenAllfile = os.path.join(excels_dir, "CHILDREN_ALL.xlsx")
    df = pd.read_excel(childrenAllfile, sheet_name='Sheet1')
    df = df.filter(['Child ID', 'Person Full Name','Community ID','Community Name','School','School Name','Status Description'])
    df = df.rename(columns={"Community ID":"CommunityId","Community Name":"CommunityName","Child ID": "ChildId", "Person Full Name": "FullName","School Name":"SchoolName"})
    df['ChildId'] = df['ChildId'].astype(str)
    df['CommunityId'] = df['CommunityId'].astype(str)
    df['School'] = df['School'].astype(str)
    df = df.drop_duplicates()
    print(df.dtypes)

    #convert dataframe to tuples
    records = df.to_records(index=False)
    #put tuples to list
    result = list(records)

    #push all records to children_all table on corr_manager_local.db
    #print(result)
    sql_insertmanychildren = "INSERT INTO children_comm values (?,?,?,?,?,?,?)"
    sqlite_cursor.executemany(sql_insertmanychildren, result)
    sqlite_cnx.commit()

parsingChildCommunity()

