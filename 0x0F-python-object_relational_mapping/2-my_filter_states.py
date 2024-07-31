#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    usr = args[1]
    password = args[2]
    database = args[3]
    con = MySQLdb.connect(host="localhost", port=3306, user=usr,
                          passwd=password, db=database, charset="utf8")
    com = """SELECT * FROM states WHERE states.name='{}'
ORDER BY states.id""".format(args[4])
    with con.cursor() as cur:
        cur.execute(com)
        for row in cur.fetchall():
            print(row)
        con.commit()

    con.close()
