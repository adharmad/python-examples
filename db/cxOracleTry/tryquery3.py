import ora   

from ora import *

if __name__ == '__main__':
    dbLogin = DBCredentials('oim90', 'oim90', 'orcl')
    oracledb = OracleFacade(dbLogin)
    oracledb.login()
    query = 'select usr_login, usr_password from usr' 
    query1 = 'select * from usr'
    query2 = 'select usr_login, usr_password from usr order by usr_login'
    lst = oracledb.executeQuery(query2)
    for elem in lst:
	    print elem
    oracledb.logout()
