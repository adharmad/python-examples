import cx_Oracle

def queryDB():
    connection = cx_Oracle.connect('oim90/oim90@orcl')
    cursor = connection.cursor()

    query = 'SELECT USR_LOGIN FROM USR'
    cursor.execute(query)
    lst = cursor.fetchall()

    for elem in lst:
        print elem

    cursor.close()
    connection.close()

if __name__ == '__main__':
    queryDB()

