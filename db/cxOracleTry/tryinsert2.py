import ora   

from ora import *

if __name__ == '__main__':
    dbLogin = DBCredentials('oim90', 'oim90', 'orcl')
    oracledb = OracleFacade(dbLogin)
    oracledb.login()
    h = {
        't1' : "\'bags\'",
        't2' : "\'lokare\'"
    }

    oracledb.executeInsertFromHash('t', h)

    oracledb.logout()
