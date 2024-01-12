#!/usr/bin/python3

"""list all states by name starting wih N """

import MySQLdb as db
from sys import argv as ar


if __name__ == "__main__":
    conn = db.connect(host="localhost", port=3306, user=ar[1],
                      passwd=ar[2], db=ar[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    result = cur.fetchall()

    for row in result:
        if row[1].startswith("N"):
            print(row)

    cur.close()
    conn.close()
