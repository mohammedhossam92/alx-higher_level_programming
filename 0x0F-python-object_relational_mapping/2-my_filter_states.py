#!/usr/bin/python3

import MySQLdb as sql
from sys import argv as arg

if __name__ == "__main__":
    conn = sql.connect(host="localhost", port=3306, user=arg[1],
                       passwd=arg[2], db=arg[3], charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'"
                " ORDER BY states.id ASC".format(arg[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)
