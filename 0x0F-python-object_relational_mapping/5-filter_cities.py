#!/usr/bin/python3
"""list states"""

import MySQLdb as sql
from sys import argv as arg


if __name__ == "__main__":
    conn = sql.connect(host="localhost", port=3306, user=arg[1],
                       passwd=arg[2], db=arg[3], charset="utf8")

    cur = conn.cursor()

    query = """SELECT cities.name From cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC"""

    cur.execute(query, (arg[4],))
    result = cur.fetchall()
    final_list = map(lambda x: x[0], result)
    print(", ".join(final_list))
    cur.close()
    conn.close()
