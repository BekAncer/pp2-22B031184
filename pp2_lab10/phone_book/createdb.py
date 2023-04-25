import psycopg2 as ps
import csv



conn = ps.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = 'Barcelona_1899',
                  port = '5432' 
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE phone_book (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
);
""")


    
conn.commit()


cur.close()
conn.close()