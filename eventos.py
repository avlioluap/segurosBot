from acessodb import Acessodb


class Eventos():
    id = ""
    userId = ""
    data = ""
    bot = False
    evento = []

    def __init__(self):
        # TODO gestao de eventos x em x sec
        self.verificarEvento()

    def verificarEvento(self):
        conn = Acessodb()
        query = conn.cur()
        # obter dados de evento
        query.execute('SELECT * FROM events WHERE bot = false ORDER BY id ASC LIMIT 1')
        row = query.fetchone()

        while row is not None:
            # print(row)
            self.id = row[0]
            self.userId = row[1]
            self.data = row[2]
            self.bot = row[3]
            return True

    def __del__(self):
        del self
