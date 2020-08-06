import cx_Oracle

def queryDB():
    connection = cx_Oracle.connect('oim90/oim90@orcl')
    cursor = connection.cursor()

    query = 'SELECT xsd_seq.nextval from dual'
    cursor.execute(query)
    lst = cursor.fetchall()

    for elem in lst:
	    print elem[0]

    cursor.close()
    connection.close()

if __name__ == '__main__':
    queryDB()
