#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

args = sys.argv
usr = args[1]
password = args[2]
database = args[3]
con = MySQLdb.connect(host="localhost", port=3306, user=usr,
                      passwd=password, db=database, charset="utf8")
cur = con.cursor()
cur.execute("SELECT * FROM `hbtn_0e_0_usa`.`states` ORDER BY `states`.`id`")
for row in cur.fetchall():
    print(row)

con.commit()
cur.close()
con.close()

if __name__ == "__main__":
    """  """
