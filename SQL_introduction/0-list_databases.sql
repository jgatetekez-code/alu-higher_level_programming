#!/usr/bin/python3
"""Script that lists all databases."""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2]
    )

    cursor = db.cursor()

    cursor.execute("SHOW DATABASES")

    for row in cursor.fetchall():
        print(row[0])

    cursor.close()
    db.close()
