import psycopg2 as ps


sql_update_name = '''
    UPDATE phone_book SET name = %s WHERE id = %s;
'''

sql_update_phone = '''
    UPDATE phone_book SET phone_number = %s WHERE id = %s;
'''

conn = ps.connect(host = 'localhost',
                  dbname = 'postgres',
                  user = 'postgres',
                  password = 'Barcelona_1899',
                  port = '5432'
)

cur = conn.cursor()

command = input('What do you want to change?\n')
id = input('Enter the id of the phone to update\n')
if command == 'phone':
    phone = input('Input the new phone number\n')
    cur.execute(sql_update_phone, (phone, id))
elif command == 'name':
    name = input('Input the new name to update\n')
    cur.execute(sql_update_name, (name, id))
else:
    print('Error, try again')
    
conn.commit()

cur.close()
conn.close()