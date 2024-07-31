#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
in a safe way.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    usr = args[1]
    password = args[2]
    database = args[3]
    con = MySQLdb.connect(host="localhost", port=3306, user=usr,
                          passwd=password, db=database, charset="utf8")
    with con.cursor() as cur:
        cur.execute("""SELECT `cities`.`name`
                    FROM `cities` INNER JOIN `states` ON
                    `cities`.`state_id` = `states`.`id` WHERE
                    `states`.`name` = "{}" ORDER BY
                    `cities`.`id`;""".format(args[4]))
        li = []
        for row in list(cur.fetchall()):
            li.append(str(*row))
        print(", ".join(li))
        con.commit()

    con.close()
