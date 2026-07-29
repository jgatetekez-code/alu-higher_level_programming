# 0-list_databases.sql

## Description

This SQL script lists all databases available on a MySQL server using the `SHOW DATABASES;` statement. It is useful for viewing the databases that exist on the server and verifying that the MySQL server is accessible.

## SQL Statement Used

```sql
SHOW DATABASES;
```

## How to Run

```bash
cat 0-list_databases.sql | mysql -u root -p
```

When prompted, enter your MySQL password (or press **Enter** if no password is set).

## Expected Output

The script displays a list of all databases on the MySQL server, for example:

```
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```
