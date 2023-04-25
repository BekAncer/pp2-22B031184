import psycopg2 as ps

sql_select_all_records = '''
    SELECT * FROM phone_book;
'''

sql_select_record_by_id = '''
    SELECT * FROM phone_book WHERE id = %s;
'''

sql_select_record_by_name = '''
    SELECT * FROM phone_book WHERE name = %s;
'''

conn = ps.connect(host = 'localhost',
                  user = 'postgres',
                  dbname = 'postgres',
                  password = 'Barcelona_1899',
                  port = '5432'
)

cur = conn.cursor()


command = input("What kind of query do you want to execute?[all/id/name]:")
if command == 'all':
    cur.execute(sql_select_all_records)
    print(cur.fetchall())
elif command == 'id':
    id = input("Input id of the record:")
    cur.execute(sql_select_record_by_id, (id,))
    print(cur.fetchone())
elif command == 'name':
    name = input("Input the user name of the record:")
    cur.execute(sql_select_record_by_name, (name,))
    print(cur.fetchall())
else:
    print("There is no such command")


conn.commit()

cur.close()
conn.close()