import cx_Oracle

class DBLoginError(Exception):
    pass

class DBCredentials:
    def __init__(self, userId=None, password=None, sid=None):
	    self.userId = userId
	    self.password = password
	    self.sid = sid

class OracleFacade:
    def __init__(self, dbLogin=None):
	    self.dbLogin = dbLogin
	    self.con = None
	    self.cursor = None

    def login(self):
	    print 'Logging into Oracle'
	    if not self.dbLogin:
	        print 'DB Login credentials seem to be absent'
	        raise DBLoginError
	    else:
	        self.con = cx_Oracle.connect(self.dbLogin.userId, \
		    self.dbLogin.password, self.dbLogin.sid)
	        self.cursor = self.con.cursor()
    
    def logout(self):
	    print 'Logging out of Oracle'
	    if self.cursor:
	        self.cursor.close()
	    if self.con:
	        self.con.close()
    
    def executeQuery(self, query):
	    self.cursor.execute(query)
	    lst = self.cursor.fetchall()
	    return lst
    
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
