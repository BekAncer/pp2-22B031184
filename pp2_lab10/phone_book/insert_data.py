import psycopg2 as ps
import csv

sql = """
    INSERT INTO phone_book VALUES(DEFAULT, %s, %s);
"""

conn = ps.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = 'Barcelona_1899',
                  port = '5432' 
)

cur = conn.cursor()


with open("input.csv", "r") as f:
    data = csv.reader(f, delimiter=',')
    for row in data:
        cur.execute(sql, row)

name = input("Input the name: ")
phone = input("Input the names phone number: ")
cur.execute(sql,(name,phone))

conn.commit()


cur.close()
conn.close()