
---

## Script (`0-list_databases.py`)

```python
#!/usr/bin/python3
"""Script that lists all databases in a MySQL server."""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2]
    )

    cursor = db.cursor()

    cursor.execute("SHOW DATABASES")

    for database in cursor.fetchall():
        print(database[0])

    cursor.close()
    db.close()
