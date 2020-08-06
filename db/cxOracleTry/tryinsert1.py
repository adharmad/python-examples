import ora   

from ora import *

if __name__ == '__main__':
    dbLogin = DBCredentials('oim90', 'oim90', 'orcl')
    oracledb = OracleFacade(dbLogin)
    oracledb.login()
    #sql = 'insert into t (t1, t2) values (\'kashmira\', \'dharma\')'
    sql = 'update t set t1=\'amol123\' where t1=\'amol\''
    lst = oracledb.executeUpdate(sql)
    oracledb.logout()
