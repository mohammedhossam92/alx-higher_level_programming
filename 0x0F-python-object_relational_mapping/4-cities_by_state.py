#!/usr/bin/python3

"""list all states from cities"""

import MySQLdb as sql
from sys import argv as arg

if __name__ == "__main__":
    conn = sql.connect(host="localhost", port=3306, user=arg[1],
                       passwd=arg[2], db=arg[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC")
    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    conn.close()
