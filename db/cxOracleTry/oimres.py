# Create OIM resource object using the oracledb infrastructure
#
import sys
from ora import *

OBJ_TABLE = 'obj'
OST_TABLE = 'ost'
OBI_TABLE = 'obi'
OIO_TABLE = 'oio'
ORC_TABLE = 'orc'
SCH_TABLE = 'sch'
OSI_TABLE = 'osi'
OSH_TABLE = 'osh'
OUG_TABLE = 'oug'
OBA_TABLE = 'oba'

OST_STATUS_LIST = [
    '\'Waiting\'',
    '\'None\'',
    '\'Provide Information\'',
    '\'Disabled\'',
    '\'Provisioning\'',
    '\'Revoked\''
    '\'Ready\'',
    '\'Enabled\'',
    '\'Provisioned\''
]

obj = {
    'OBJ_KEY' : '',
    'OBJ_ORDER_FOR' : "\'U\'",
    'OBJ_TYPE' : "\'Application\'",
    'OBJ_ALLOW_MULTIPLE' : "\'1\'",
    'OBJ_SELF_REQUEST_ALLOWED' : "\'1\'",
    'OBJ_NAME' : '',
    'OBJ_AUTOSAVE' : "\'1\'",
    'OBJ_ALLOWALL' : "\'1\'",
    'OBJ_AUTOLAUNCH' : "\'1\'",
    'OBJ_OBJADMINONLY' : "\'0\'",
    'OBJ_AUTO_PREPOP' : "\'0\'",
    'OBJ_CREATE' : 'SYSDATE',
    'OBJ_CREATEBY' : '1',
    'OBJ_UPDATE' : 'SYSDATE',
    'OBJ_UPDATEBY' : '1',
    'OBJ_FINANCIALLY_SIGNIFICANT' : '1',
    'OBJ_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

ost = {
    'OST_KEY' : '',
    'OBJ_KEY' : '',
    'OST_STATUS' : '',
    'OST_LAUNCH_DEPENDENT' : '0',
    'OST_CREATE' : 'SYSDATE',
    'OST_CREATEBY' : '1',
    'OST_UPDATE' : 'SYSDATE',
    'OST_UPDATEBY' : '1',
    'OST_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

obi = {
    'OBI_KEY' : '',
    'OBJ_KEY' : '',
    'OBI_STATUS' : '\'Approved\'',
    'OBI_STAGE_FLAG' : '2',
    'OBI_CREATE' : 'SYSDATE',
    'OBI_CREATEBY' : '1',
    'OBI_UPDATE' : 'SYSDATE',
    'OBI_UPDATEBY' : '1',
    'OBI_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

oio = {
    'OIO_KEY' : '',
    'OBI_KEY' : '',
    'ACT_KEY' : '',
    'OST_KEY' : '',
    'OIO_CREATE' : 'SYSDATE',
    'OIO_CREATEBY' : '1',
    'OIO_UPDATE' : 'SYSDATE',
    'OIO_UPDATEBY' : '1',
    'OIO_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

orc = {
    'ORC_KEY' : '',
    'TOS_KEY' : '',
    'ORD_KEY' : '',
    'PKG_KEY' : '',
    'ORC_SUPPCODE' : '\'00\'',
    'ACT_KEY' : '',
    'ORC_ASSIGNED_TO' : '1',
    'ORC_STATUS' : '\'P\'',
    'ORC_TOS_INSTANCE_KEY' : '',
    'ORC_LAST_UPDATE' : 'SYSDATE',
    'ORC_LAST_UPDATEBY' : '1',
    'ORC_REQUIRED_COMPLETE' : '0',
    'ORC_TARGET' : '1',
    'ORC_CREATE' : 'SYSDATE',
    'ORC_CREATEBY' : '1',
    'ORC_UPDATEBY' :  '1',
    'ORC_UPDATE' : 'SYSDATE',
    'ORC_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

sch = {
    'SCH_KEY' : '',
    'SCH_STATUS' : '\'P\'',
    'SCH_PROJ_START' : 'SYSDATE',
    'SCH_PROJ_END' : 'SYSDATE',
    'SCH_ACTUAL_START' : 'SYSDATE',
    'SCH_CREATE' : 'SYSDATE',
    'SCH_CREATEBY' : '1',
    'SCH_UPDATEBY' : '1',
    'SCH_UPDATE' : 'SYSDATE',
    'SCH_ROWVER': 'HEXTORAW(\'0000000000000000\')'
}

osi = {
    'SCH_KEY' : '',
    'ORC_KEY' : '',
    'MIL_KEY' : '',
    'TOS_KEY' : '',
    'PKG_KEY' : '',
    'ACT_KEY' : '',
    'ORD_KEY' : '',
    'ORC_SUPPCODE' : '\'00\'',
    'OSI_ASSIGN_TYPE' : '\'Default task assignment\'',
    'OSI_ASSIGNED_TO_USR_KEY' : '1',
    'OSI_ASSIGNED_DATE' : 'SYSDATE',
    'OSI_CREATE' : 'SYSDATE',
    'OSI_CREATEBY' : '1',
    'OSI_UPDATE' : 'SYSDATE',
    'OSI_UPDATEBY' : '1',
    'OSI_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

osh = {
    'OSH_KEY' : '',
    'SCH_KEY' : '',
    'STA_KEY' : '',
    'OSH_ACTION' : '\'Engine\'',
    'OSH_ASSIGN_TYPE' : '\'Default task assignment\'',
    'OSH_ASSIGNED_TO_USR_KEY' : '1',
    'OSH_ASSIGN_DATE' : 'SYSDATE',
    'OSH_CREATE' : 'SYSDATE',
    'OSH_CREATEBY' : '1',
    'OSH_UPDATE' : 'SYSDATE',
    'OSH_UPDATEBY' : '1',
    'OSH_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

oug = {
    'OBJ_KEY' : '',
    'UGP_KEY' : '',
    'OUG_WRITE' : '1',
    'OUG_DELETE' : '1',
    'OUG_CREATE' : 'SYSDATE',
    'OUG_CREATEBY' : '1',
    'OUG_UPDATE' : 'SYSDATE',
    'OUG_UPDATEBY' : '1',
    'OUG_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}                

oba = {
    'OBJ_KEY' : '',
    'UGP_KEY' : '',
    'OBA_PRIORITY' : '1',
    'OBA_CREATE' : 'SYSDATE',
    'OBA_CREATEBY' : '1',
    'OBA_UPDATE' : 'SYSDATE',
    'OBA_UPDATEBY' : '1',
    'OBA_ROWVER' : 'HEXTORAW(\'0000000000000000\')'
}

if __name__ == '__main__':
    dbLogin = DBCredentials('oim90', 'oim90', 'orcl')
    oracledb = OracleFacade(dbLogin)
    oracledb.login()

    # Create entry in OBJ
    objKey = oracledb.nextVal('obj_seq')
    objName = sys.argv[1]

    obj['OBJ_KEY'] = str(objKey)
    obj['OBJ_NAME'] = "\'" + objName + "\'"

    oracledb.executeInsertFromHash(OBJ_TABLE, obj)

    # Create OST entries
    for status in OST_STATUS_LIST:
        ostKey = oracledb.nextVal('ost_seq')
        ost['OBJ_KEY'] = objKey
        ost['OST_KEY'] = ostKey
        ost['OST_STATUS'] = status
        
        oracledb.executeInsertFromHash(OST_TABLE, ost)

    # Create OBI entries
    # Get 'Installation' object key
    sql = 'select obj_key from obj where obj_name=\'Installation\''
    lst = oracledb.executeQuery(sql)
    installationROKey = lst[0][0]
    obiKey = oracledb.nextVal('obi_seq')
    obi['OBJ_KEY'] = installationROKey
    obi['OBI_KEY'] = obiKey

    oracledb.executeInsertFromHash(OBI_TABLE, obi)

    # Create OIO entries
    # Get 'Requests' Organization Key
    sql = 'select act_key from act where act_name=\'Requests\''
    lst = oracledb.executeQuery(sql)
    requestsOrgKey = lst[0][0]
    oioKey = oracledb.nextVal('oio_seq')
    # Get 'Ready' status key for 'Installation' resource
    sql = 'select ost_key from ost where ost_status=\'Ready\' and obj_key=' + str(installationROKey)
    lst = oracledb.executeQuery(sql)
    readyStatusKey = lst[0][0]

    oio['OIO_KEY'] = oioKey
    oio['ACT_KEY'] = requestsOrgKey
    oio['OBI_KEY'] = obiKey
    oio['OST_KEY'] = readyStatusKey

    oracledb.executeInsertFromHash(OIO_TABLE, oio)

    # Create ORC entries
    orcKey = oracledb.nextVal('orc_seq')
    sql = 'select pkg_key from pkg where pkg_name=\'Installation Process\''
    lst = oracledb.executeQuery(sql)
    installationPkgKey = lst[0][0]
    sql = 'select tos_key from tos where pkg_key=' + str(installationPkgKey)
    lst = oracledb.executeQuery(sql)
    tosKey = lst[0][0]
    sql = 'select ord_key from ord where act_key=' + str(requestsOrgKey)
    lst = oracledb.executeQuery(sql)
    ordKey = lst[0][0]

    orc['ORC_KEY'] = orcKey
    orc['TOS_KEY'] = tosKey
    orc['ORD_KEY'] = ordKey
    orc['PKG_KEY'] = installationPkgKey
    orc['ACT_KEY'] = requestsOrgKey
    orc['ORC_TOS_INSTANCE_KEY'] = "\'" + objName + "\'"

    oracledb.executeInsertFromHash(ORC_TABLE, orc)

    # Create sch, osi, osh entries
    # First entry in sch, osi, osh
    schKey = oracledb.nextVal('sch_seq')
    firstSch = schKey
    oshKey = oracledb.nextVal('osh_seq')
    sql = 'select mil_key from mil where mil_name=\'System Validation\' and tos_key=' + str(tosKey)
    lst = oracledb.executeQuery(sql)
    milKey = lst[0][0]
    sql = 'select sta_key from sta where sta_status=\'P\''
    lst = oracledb.executeQuery(sql)
    staKey = lst[0][0]
    
    sch['SCH_KEY'] = schKey
    oracledb.executeInsertFromHash(SCH_TABLE, sch)

    osi['SCH_KEY'] = schKey
    osi['ORC_KEY'] = orcKey
    osi['MIL_KEY'] = milKey
    osi['TOS_KEY'] = tosKey
    osi['PKG_KEY'] = installationPkgKey
    osi['ACT_KEY'] = requestsOrgKey
    osi['ORD_KEY'] = ordKey
    oracledb.executeInsertFromHash(OSI_TABLE, osi)

    osh['OSH_KEY'] = oshKey
    osh['SCH_KEY'] = schKey
    osh['STA_KEY'] = staKey
    oracledb.executeInsertFromHash(OSH_TABLE, osh)

    # Second entry in sch, osi, osh
    schKey = oracledb.nextVal('sch_seq')
    oshKey = oracledb.nextVal('osh_seq')
    sql = 'select mil_key from mil where mil_name=\'Install Application\' and tos_key=' + str(tosKey)
    lst = oracledb.executeQuery(sql)
    milKey = lst[0][0]    

    sch['SCH_KEY'] = schKey
    oracledb.executeInsertFromHash(SCH_TABLE, sch)

    osi['SCH_KEY'] = schKey
    osi['ORC_KEY'] = orcKey
    osi['MIL_KEY'] = milKey
    osi['TOS_KEY'] = tosKey
    osi['PKG_KEY'] = installationPkgKey
    osi['ACT_KEY'] = requestsOrgKey
    osi['ORD_KEY'] = ordKey
    oracledb.executeInsertFromHash(OSI_TABLE, osi)

    osh['OSH_KEY'] = oshKey
    osh['SCH_KEY'] = schKey
    osh['STA_KEY'] = staKey
    oracledb.executeInsertFromHash(OSH_TABLE, osh)

    # Thord entry in sch, osi, osh
    schKey = oracledb.nextVal('sch_seq')
    oshKey = oracledb.nextVal('osh_seq')
    sql = 'select mil_key from mil where mil_name=\'Enter Info into Xellerate\' and tos_key=' + str(tosKey)
    lst = oracledb.executeQuery(sql)
    milKey = lst[0][0]    

    sch['SCH_KEY'] = schKey
    oracledb.executeInsertFromHash(SCH_TABLE, sch)

    osi['SCH_KEY'] = schKey
    osi['ORC_KEY'] = orcKey
    osi['MIL_KEY'] = milKey
    osi['TOS_KEY'] = tosKey
    osi['PKG_KEY'] = installationPkgKey
    osi['ACT_KEY'] = requestsOrgKey
    osi['ORD_KEY'] = ordKey
    oracledb.executeInsertFromHash(OSI_TABLE, osi)

    osh['OSH_KEY'] = oshKey
    osh['SCH_KEY'] = schKey
    osh['STA_KEY'] = staKey
    oracledb.executeInsertFromHash(OSH_TABLE, osh)

    # Update SCH to complete
    sql = 'update sch set SCH_STATUS=\'C\', SCH_ACTUAL_END=SYSDATE, SCH_UPDATE=SYSDATE, SCH_ROWVER=HEXTORAW(\'0000000000000001\') where sch_key=' + str(firstSch) + ' and sch_rowver=HEXTORAW(\'0000000000000000\')'
    oracledb.executeUpdate(sql)

    # Update ORC 
    sql = 'update orc set ORC_PACKAGE_INSTANCE_KEY=' + str(orcKey) + ', ORC_UPDATE=SYSDATE, ORC_ROWVER=HEXTORAW(\'0000000000000001\') where orc_key=' + str(orcKey) + ' and orc_rowver=HEXTORAW(\'0000000000000000\')'
    oracledb.executeUpdate(sql)

    # Update OIO 
    sql = 'update oio set ORC_KEY=' + str(orcKey) + ', OIO_UPDATE=SYSDATE, OIO_ROWVER=HEXTORAW(\'0000000000000001\') where oio_key=' + str(oioKey) +  ' and oio_rowver=HEXTORAW(\'0000000000000000\')'
    oracledb.executeUpdate(sql)

    # Create OUG entry
    sql = 'select ugp_key from ugp where ugp_name=\'SYSTEM ADMINISTRATORS\''
    lst = oracledb.executeQuery(sql)
    sysadmUgpKey = lst[0][0]
    oug['OBJ_KEY'] = objKey
    oug['UGP_KEY'] = sysadmUgpKey

    oracledb.executeInsertFromHash(OUG_TABLE, oug)

    # Create OBA entry
    oba['OBJ_KEY'] = objKey
    oba['UGP_KEY'] = sysadmUgpKey

    oracledb.executeInsertFromHash(OBA_TABLE, oba)

    oracledb.logout()

