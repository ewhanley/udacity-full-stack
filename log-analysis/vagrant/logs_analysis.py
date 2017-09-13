#!/usr/bin/env python3

import psycopg2
from tabulate import tabulate

DBNAME = 'news'


question1 = "What are the three most popular articles of all time?"
query1_header = ["Title", "Views"]
query1 = """
        SELECT a.title, count(a.title) as views
        FROM articles a, log l
        WHERE a.slug = SUBSTRING(l.path, '[^/]*$')
            AND l.status like '2%'
        GROUP BY a.title
        ORDER BY views DESC;"""

question2 = "Who are the most popular article authors of all time?"
query2_header = ["Author", "Views"]
query2 = """
        SELECT au.name, COUNT(l.path) AS views
        FROM authors au, articles ar, log l
        WHERE ar.slug = SUBSTRING(l.path, '[^/]*$')
            AND ar.author = au.id
            AND l.status like '2%'
        GROUP BY au.name
        ORDER BY views DESC;"""

question3 = "On which days did more than 1% of requests lead to errors?"
query3_header = ["Date", "Pct Error"]
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


def get_query_results(db_name, query_string):
    conn = psycopg2.connect(dbname=db_name)
    cursor = conn.cursor()
    cursor.execute(query_string)
    query_result_raw = cursor.fetchall()
    conn.close()
    return query_result_raw


def output_results_to_file(question, query_result, file_name):
    output_string = "\n".join([question, query_result, "\n"])
    with open(file_name, "w") as output_file:
        output_file.write(output_string)


query1_result_raw = get_query_results(DBNAME, query1)
query2_result_raw = get_query_results(DBNAME, query2)
query3_result_raw = get_query_results(DBNAME, query3)

query1_result_tbl = tabulate(query1_result_raw, headers=query1_header,
                             tablefmt="orgtbl")
query2_result_tbl = tabulate(query2_result_raw, headers=query2_header,
                             tablefmt="orgtbl")
query3_result_tbl = tabulate(query3_result_raw, headers=query3_header,
                             tablefmt="orgtbl")

print(question1, query1_result_tbl, "\n", sep="\n")
print(question2, query2_result_tbl, "\n", sep="\n")
print(question3, query3_result_tbl, "\n", sep="\n")
