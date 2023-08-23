from models.children import getAllChildren

### WORKED!!!
def updateProjectCode(cursor):
    i = 1
    all_children = getAllChildren(cursor)
    for children_group in all_children:
        if len(children_group)>0:
            print(f"#Children-{i}: {len(children_group)}")
            print(f"all child_{i} project code is updating...")
            # UPDATE PROJECT CODE PAUD
            sql_string = f"UPDATE AFU_Child SET ch_proj_{i}='33005,33007,33023,33026,33033,33051' WHERE ch_prof_sch_type_{i}=705 " \
                         f"and ch_child_id_{i}<>'' "
            cursor.execute(sql_string)
            cursor.commit()
            # UPDATE PROJECT CODE SD
            sql_string = f"UPDATE AFU_Child SET ch_proj_{i}='33054,33056,33057,33059,33060,33062,33066' WHERE " \
                         f"(ch_prof_sch_type_{i}=718 or ch_prof_sch_type_{i}=702) and ch_child_id_{i}<>'' "
            cursor.execute(sql_string)
            cursor.commit()
            # UPDATE PROJECT CODE SMP
            sql_string = f"UPDATE AFU_Child SET ch_proj_{i}='33064, 33066, 33072' WHERE " \
                         f"ch_prof_sch_type_{i}=722 and ch_child_id_{i}<>'' "
            cursor.execute(sql_string)
            cursor.commit()
        i += 1


"""
ATTRIBUTES:
ch_proj_x,
WHERE:
ch_prof_sch_type_x (PAUD:705, SD: 718/702, SMP: 722)
"""