import psycopg2 as db

conn = db.connect('host=192.168.0.252 dbname=simula user=postgres password=postgres')
cur = conn.cursor()


def get_database_version():
    try:
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, db.DatabaseError) as error:
        print(error)

def close_database():
    conn.close()
    print('Database connection closed.')
