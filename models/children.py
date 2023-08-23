def getAllChildren(cursor):
    print("Collecting and grouping children data from database...")
    cursor.execute("select ch_child_id_1 from AFU_Child where ch_child_id_1 <>''")
    all_child_1 = cursor.fetchall()

    cursor.execute("select ch_child_id_2 from AFU_Child where ch_child_id_2 <>''")
    all_child_2 = cursor.fetchall()

    cursor.execute("select ch_child_id_3 from AFU_Child where ch_child_id_3 <>''")
    all_child_3 = cursor.fetchall()

    cursor.execute("select ch_child_id_4 from AFU_Child where ch_child_id_4 <>''")
    all_child_4 = cursor.fetchall()

    cursor.execute("select ch_child_id_5 from AFU_Child where ch_child_id_5 <>''")
    all_child_5 = cursor.fetchall()

    cursor.execute("select ch_child_id_6 from AFU_Child where ch_child_id_6 <>''")
    all_child_6 = cursor.fetchall()

    cursor.execute("select ch_child_id_7 from AFU_Child where ch_child_id_7 <>''")
    all_child_7 = cursor.fetchall()

    cursor.execute("select ch_child_id_8 from AFU_Child where ch_child_id_8 <>''")
    all_child_8 = cursor.fetchall()

    all_children = [all_child_1, all_child_2, all_child_3, all_child_4, all_child_5, all_child_6, all_child_7,
                    all_child_8]
    return all_children


def numChildrenFromDb(all_children):
    new_all_children = []
    for children_group in all_children:
        new_group = []
        for child_tuple in children_group:
            child_id = child_tuple[0]
            new_group.append(child_id)
        new_all_children.append(new_group)

    all_children = new_all_children

    count_children = 0
    for group in all_children:
        count_children += len(group)
    return count_children
