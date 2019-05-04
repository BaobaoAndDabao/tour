def get_db_url(dbinfo):
    ENGINE=dbinfo.get('ENGINE') or 'mysql'
    DRIVER=dbinfo.get('DRIVER') or 'mysqlconnector'
    USER= dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or 'wen123'
    HOST= dbinfo.get('HOST') or 'localhost'
    PORT= dbinfo.get('PORT') or '3306'
    NAME= dbinfo.get('NAME') or 'test'

    return "{}+{}://{}:{}@{}:{}/{}".format(ENGINE,DRIVER,USER,PASSWORD,HOST,PORT,NAME)


class devDBConfig():
    DEBUG = True
    DATABASE ={
        "ENGINE":"mysql",
        "DRIVER":"mysqlconnector",
        "USER":"root",
        "PASSWORD":"wen123",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"tour"
    }

    SQLALCHEMY_DATABASE_URI=get_db_url(DATABASE)


class stgDBConfig():
    DEBUG = True
    DATABASE ={
        "ENGINE":"mysql",
        "DRIVER":"mysqlconnector",
        "USER":"root",
        "PASSWORD":"wen123",
        "HOST":"localhost",
        "PORT":"3306",
        "NAME":"tour"
    }

    DB_URL=get_db_url(DATABASE)

class envs:
    def get(name):
        if(name=='dev'):
            return  devDBConfig
        if(name=='stg'):
            return stgDBConfig
