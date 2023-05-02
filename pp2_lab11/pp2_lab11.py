import psycopg2
import csv
from config import host, user, password, db_name
def createtable():
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE phbook(
                    id serial PRIMARY KEY,
                    nickname varchar(50) NOT NULL,
                    number varchar(50) NOT NULL);"""
            )
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()

def addnumber():
    print('введите имя')
    a=input()
    print('введите номер')
    b=int(input())
    values=(a,b)
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO phbook (nickname, number) VALUES (%s, %s)",values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def checktable():
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM phbook;")
            rows=cursor.fetchall()
            for row in rows:
                print(row)


    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def checkcsv():
    print('Введите название файла')
    a=input()
    with open(f'{a}', 'r') as file:
        reader = csv.reader(file)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            for row in reader:
                nickname, number = row
                query = "INSERT INTO my_table (nickname, number) VALUES (%s, %s);"
                values = (nickname, number)
                cursor.execute(query, values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def Changenamefindname():
    print('введите имя')
    a=input()
    print('введите новое имя')
    b=input()
    values=(b,a)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("UPDATE phbook SET nickname = %s WHERE nickname = %s;",values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def Changenamefindnumber():
    print('введите номер')
    a = int(input())
    print('введите новое имя')
    b = input()
    values = (b, a)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("UPDATE phbook SET nickname = %s WHERE number = %s;", values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def Changenumberfindname():
    print('введите имя')
    a = input()
    print('введите номер')
    b = int(input())
    values = (b, a)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("UPDATE phbook SET number = %s WHERE nickname = %s;", values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def Changenumberfindnumber():
    print('введите номер')
    a = int(input())
    print('введите номер')
    b = int(input())
    values = (b, a)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("UPDATE phbook SET number = %s WHERE number = %s;", values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def Deleterowfindnumber():
    print('введите номер')
    m = int(input())
    values=(m,)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM phbook WHERE number = %s;",values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def Deleterowfindname():
    print('введите имя')
    m = input()
    values = (m,)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM phbook WHERE nickname = %s;", values)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
    ChooseAction()
def ChooseAction():
    print('1-добавить новый номер')
    print('2-изменить номер')
    print('3-просмотреть таблицу')
    print('4-удалить строку')
    print('5-выйти')
    a=int(input())
    if a==1:
        print('1-добавить вручную              2-залить из csv файла')
        b=int(input())
        if b==1:
            addnumber()
        if b==2:
            checkcsv()
    if a==2:
        print("изменить имя(1) или номер(2)?")
        c=int(input())
        if c==1:
            print("найти строку по имени(1) или номеру(2)?")
            t=int(input())
            if t==1:
                Changenamefindname()
            else:
                Changenamefindnumber()

        if c==2:
            print(("найти строку по имени(1) или номеру(2)?"))
            t = int(input())
            if t==1:
                Changenumberfindname()
            else:
                Changenumberfindnumber()
    if a==3:
        checktable()
    if a==4:
        print('удалить по номеру(1) или имени(2)?')
        t=int(input())
        if t==1:
            Deleterowfindnumber()
        if t==2:
            Deleterowfindname()
    if a==5:
        pass
ChooseAction()