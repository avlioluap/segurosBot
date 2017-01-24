from acessodb import Acessodb


class Seguradoras(object):
    activo = ""
    nome = ""
    username = ""
    password = ""
    url = ""
    seguradorasList = []

    def __init__(self):
        # self.procurarSeguradoras()
        print("procurar seguradoras")

    def procurarSeguradoras(self):
        conn = Acessodb()
        query = conn.cur()
        # obter dados de seguradora
        query.execute('SELECT * FROM seguradoras')
        rows = query.fetchall()

        for row in rows:
            # print(row)
            self.seguradorasList.append(rows)
            return self.seguradorasList

