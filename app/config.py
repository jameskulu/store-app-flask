import os

mssql = {'host': 'dbhost',
         'user': 'dbuser',
         'passwd': 'dbPwd',
         'db': 'db'
         }

postgresql = {
                'host': 'localhost',
                'user': os.environ.get('POSTGRES_USER'),
                'passwd': os.environ.get('POSTGRES_PASSWORD'),
                'db': os.environ.get('POSTGRES_DB')
            }

mssqlConfig = "mssql+pyodbc://{}:{}@{}:1433/{}?driver=SQL+Server+Native+Client+10.0".format(mssql['user'], mssql['passwd'], mssql['host'], mssql['db'])
postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

