import sqlite3


class DBProxy:
    def __init__(self, db_name: str):

        # Nome para criação do DB
        self.db_name = db_name

        #Conexão ao DB
        self.connection = sqlite3.connect(db_name)

        #Criação da tabela
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS scores(
                                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   time INTEGER NOT NULL,
                                   date TEXT NOT NULL)
                                '''
                                )

    def save(self, score_dict: dict):
        #Inserir no DB
        self.connection.execute('INSERT INTO dados (name, time, date) VALUES (:name, :time, :date)', score_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        #Retorna o top 10 dos resultados (os mais rápidos)
        return self.connection.execute('SELECT * FROM dados ORDER BY time DESC LIMIT 10').fetchall()

    def close(self):
        #Fechar conexão com DB
        return self.connection.close()
