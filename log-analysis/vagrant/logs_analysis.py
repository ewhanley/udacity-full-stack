#!/usr/bin/python3

import psycopg2
from tabulate import tabulate

DBNAME = "news"

conn = psycopg2.connect(dbname=DBNAME)
cursor = conn.cursor()

sql_query1 = """
        SELECT a.title, count(a.title) as views
        FROM articles a, log l
        WHERE a.slug = SUBSTRING(l.path, '[^/]*$')
            AND l.status like '2%'
        GROUP BY a.title
        ORDER BY views DESC;"""

sql_query2 = """
        SELECT au.name, COUNT(l.path) AS views
        FROM authors au, articles ar, log l
        WHERE ar.slug = SUBSTRING(l.path, '[^/]*$')
            AND ar.author = au.id
            AND l.status like '2%'
        GROUP BY au.name
        ORDER BY views DESC;"""

sql_query3 = """
        SELECT TO_CHAR(date, 'Month dd, YYYY') AS date,
            (ROUND(fraction * 100, 2)::text || '%') AS percent_errors
        FROM(
            SELECT DISTINCT DATE_TRUNC('day', time) AS date, status,
                (COUNT(status) OVER dsw::decimal) / (COUNT(status) OVER dw) AS FRACTION
            FROM log
            WINDOW dsw AS (PARTITION BY DATE_TRUNC('day', time), status),
                dw AS (PARTITION BY DATE_TRUNC('day', time))
            ) as error_counts
        WHERE status like '4%' AND fraction > 0.01
        ORDER BY fraction DESC;"""

cursor.execute(sql_query1)
problem1 = cursor.fetchall()

cursor.execute(sql_query2)
problem2 = cursor.fetchall()

cursor.execute(sql_query3)
problem3 = cursor.fetchall()
conn.close()

print("\n")
print("What are the three most popular articles of all time?")
print(tabulate(problem1, headers=['Title', 'Views'], tablefmt="orgtbl"))
print("\n")
print("Who are the most popular article authors of all time?")
print(tabulate(problem2, headers=['Author', 'Views'], tablefmt="orgtbl"))
print("\n")
print("On which days did more than 1% of requests lead to errors?")
print(tabulate(problem3, headers=['Date', 'Pct Error Response'],
               tablefmt="orgtbl"))
print("\n")
