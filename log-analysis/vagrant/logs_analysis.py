#!/usr/bin/env python3

import psycopg2
from tabulate import tabulate


class QuestionQueryResponse():

    """This class stores a question, a query to answer it,
    and the corresponsding answer.

    This class takes a db name, a question about data in the db, a SQL
    query string that will yield the answer to said question. It
    executes the query and returns the response in both raw and
    tabulated form.

    Attributes:
        db_name: The name of the database being queried.
        question: A string defining the question being asked of the db.
        query: A string containing a SQL query that answers question.
        result_raw: The query response as a list of tuples.
        result_tbl: The query response formatted as a table.

    Todo:
        * Add error handling via try/except
        * Add method to save output to file
    """

    def __init__(self, db_name, question, query, header=""):
        """Inits QuestionQueryResponse with db_name, question, query,
        result_raw, and result_tbl.

        Args:
            db_name (str): Name of database to be queried
            question (str): Question being answered with query
            query (str): SQL query string to be executed
            header (list): Optional list of strings for table header
        """

        result_raw = self.get_result_raw(db_name, query)

        self.db_name = db_name
        self.question = question
        self.query = query
        self.result_raw = result_raw
        self.result_tbl = self.get_result_tbl(result_raw, header)

    def get_result_raw(self, db_name, query):
        """This method executes the query against db and returns result

        This method connects to the db (db_name), executes the SQL
        query, and returns the result without any formatting.

        Args:
            db_name (str): Name of database to be queried
            query (str): SQL query string to be executed
        """

        conn = psycopg2.connect(dbname=db_name)
        cursor = conn.cursor()
        cursor.execute(query)
        result_raw = cursor.fetchall()
        conn.close()

        return result_raw

    def get_result_tbl(self, result_raw, header):
        """This method formats the raw query result as a table.

        Args:
            results_raw (list): Query response as list of tuples
            header (list): Optional list of strings for table header
        """

        result_tbl = tabulate(result_raw, headers=header,
                              tablefmt="orgtbl")
        return result_tbl


# Specify questions, headers, and queries for each of the three
# assignment problems.
question1 = "What are the three most popular articles of all time?"
header1 = ["Title", "Views"]
query1 = """
        SELECT a.title, count(a.title) as views
        FROM articles a, log l
        WHERE a.slug = SUBSTRING(l.path, '[^/]*$')
            AND l.status like '2%'
        GROUP BY a.title
        ORDER BY views DESC;"""

question2 = "Who are the most popular article authors of all time?"
header2 = ["Author", "Views"]
query2 = """
        SELECT au.name, COUNT(l.path) AS views
        FROM authors au, articles ar, log l
        WHERE ar.slug = SUBSTRING(l.path, '[^/]*$')
            AND ar.author = au.id
            AND l.status like '2%'
        GROUP BY au.name
        ORDER BY views DESC;"""

question3 = "On which days did more than 1% of requests lead to errors?"
header3 = ["Date", "Pct Error"]
query3 = """
        SELECT TO_CHAR(s.date, 'Month dd, YYYY') AS date,
        (ROUND(s.status_count::decimal/t.total_count*100, 2)::text || '%')
            as percent_error
        FROM
            (SELECT DATE_TRUNC('day', time) AS date, status,
            count(status) AS status_count
            FROM log
            WHERE status LIKE '4%'
            GROUP BY DATE_TRUNC('day', time), status) s,
            (SELECT DATE_TRUNC('day', time) AS date, COUNT(status) AS
                total_count
            FROM log
            GROUP BY DATE_TRUNC('day', time)) t
        WHERE s.date = t.date AND
        (s.status_count::decimal/t.total_count) > 0.01
        ORDER BY percent_error DESC;"""

q1 = QuestionQueryResponse("news", question1, query1, header1)
q2 = QuestionQueryResponse("news", question2, query2, header2)
q3 = QuestionQueryResponse("news", question3, query3, header3)

questions = [q1, q2, q3]

# Concatenate all of the questions and result tables for printing
output_string = ""
for question in questions:
    q_and_a = "\n".join([question.question, question.result_tbl, "\n"])
    output_string += q_and_a

# Print to terminal
print(output_string)

# Write to file, creating a file if none exists or overwriting existing
with open("output.txt", "w") as output_file:
    output_file.write(output_string)
