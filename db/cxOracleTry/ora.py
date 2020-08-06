# Python oracle interface package
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

    def executeInsert(self, sql):         
        self.cursor.execute(sql)
        self.con.commit() 

    def executeUpdate(self, sql): 
        self.cursor.execute(sql)
        self.con.commit() 

    # This method will take tablename and the values as a hash.
    # The query will be generated from this information and then 
    # executed
    def executeInsertFromHash(self, tableName, hash):
        sql = self.genInsertSQL(tableName, hash)
        print sql
        self.executeInsert(sql)

    def genInsertSQL(self, tableName, hash):
        sql = ''
        cols = ''
        vals = ''
        sql += "insert into " + tableName + " "
        k = hash.keys()
        for i in range(len(k)):
            key = k[i]
            cols += key
            vals += str(hash[key])
            if i < len(k)-1:
                cols += ', '
                vals += ', '
        sql += "(" + cols + ") values (" + vals +")"
        
        return sql

    def nextVal(self, seqName):
        query = 'select ' + seqName + '.nextval from dual'
        lst = self.executeQuery(query)

        return lst[0][0]
