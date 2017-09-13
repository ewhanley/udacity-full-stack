#!/usr/bin/python3

import psycopg2
from tabulate import tabulate

conn = psycopg2.connect(dbname='news')
cursor = conn.cursor()

question1 = "What are the three most popular articles of all time?"
query1 = """
        SELECT a.title, count(a.title) as views
        FROM articles a, log l
        WHERE a.slug = SUBSTRING(l.path, '[^/]*$')
            AND l.status like '2%'
        GROUP BY a.title
        ORDER BY views DESC;"""

cursor.execute(query1)
query1_out_raw = cursor.fetchall()
query1_out_tbl = tabulate(query1_out_raw, headers=['Title', 'Views'],
                          tablefmt="orgtbl")

question2 = "Who are the most popular article authors of all time?"
query2 = """
        SELECT au.name, COUNT(l.path) AS views
        FROM authors au, articles ar, log l
        WHERE ar.slug = SUBSTRING(l.path, '[^/]*$')
            AND ar.author = au.id
            AND l.status like '2%'
        GROUP BY au.name
        ORDER BY views DESC;"""

cursor.execute(query2)
query2_out_raw = cursor.fetchall()
query2_out_tbl = tabulate(query2_out_raw, headers=['Author', 'Views'],
                          tablefmt="orgtbl")

question3 = "On which days did more than 1% of requests lead to errors?"
query3 = """
        SELECT TO_CHAR(date, 'Month dd, YYYY') AS date,
            (ROUND(fraction * 100, 2)::text || '%') AS percent_errors
        FROM
        (
        SELECT DISTINCT DATE_TRUNC('day', time) AS date, status,
        (COUNT(status) OVER dsw::decimal) / (COUNT(status) OVER dw) AS FRACTION
        FROM log
        WINDOW dsw AS (PARTITION BY DATE_TRUNC('day', time), status),
            dw AS (PARTITION BY DATE_TRUNC('day', time))
        ) as error_counts
        WHERE status like '4%' AND fraction > 0.01
        ORDER BY fraction DESC;"""

cursor.execute(query3)
query3_out_raw = cursor.fetchall()
query3_out_tbl = tabulate(query3_out_raw, headers=['Date', 'Pct Error Response'],
                          tablefmt="orgtbl")

conn.close()

print("\n")
print(question1)
print("=" * len(question1))
print(tabulate(query1_out_raw, headers=['Title', 'Views'], tablefmt="orgtbl"))
print("\n")
print(question2)
print("=" * len(question2))
print(tabulate(query2_out_raw, headers=['Author', 'Views'], tablefmt="orgtbl"))
print("\n")
print(question3)
print("=" * len(question3))
print(tabulate(query3_out_raw, headers=['Date', 'Pct Error Response'],
               tablefmt="orgtbl"))
print("\n")
