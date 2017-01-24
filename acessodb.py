import psycopg2 as db


class Acessodb:

    host = "192.168.0.252"
    user = "postgres"
    passwd = "postgres"
    dbname = "simula"

    def __init__(self):
        try:
            conn = db.connect(host=self.host,
                                    user=self.user,
                                    password=self.passwd,
                                    dbname=self.dbname)

            self.cur = conn.cursor
        except:
            print("Erro de conexao a BD")

    def __del__(self):
        del self

    # def get_database_version(self):
    #    try:
    #        print('PostgreSQL database version:')
    #        self.cur.execute('SELECT version()')

            # display the PostgreSQL database server version
    #        db_version = self.cur.fetchone()
    #        print(db_version)

            # close the communication with the PostgreSQL
    #        self.cur.close()
    #    except (Exception, db.DatabaseError) as error:
    #        print(error)
