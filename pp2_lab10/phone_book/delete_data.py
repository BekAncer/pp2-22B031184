import psycopg2 as ps

sql_delete_name = '''
    DELETE FROM phone_book WHERE id = %s;
'''

sql_delete_phone = '''
    DELETE FROM phone_book WHERE id = %s;
'''

conn = ps.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = 'Barcelona_1899',
                  port = '5432'
)

cur = conn.cursor()

command = input('What info you would like to delete?\n')
id = input('Enter the id of the column to delete\n')
if command == 'phone':
    cur.execute(sql_delete_phone, (id,))
elif command == 'name':
    cur.execute(sql_delete_name, (id,))
else:
    print('No such command')
    
conn.commit()

cur.close()
conn.close