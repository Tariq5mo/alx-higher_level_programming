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
        cur.execute("SELECT * FROM states WHERE BINARY `states`.`name` =\
                    %(username)s ORDER BY states.id", {'username': args[4]})
        for row in cur.fetchall():
            print(row)
        con.commit()

    con.close()
