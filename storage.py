import pickle


class Storage(object):
    def __init__(self):
        self.__database = Storage.from_db()

    def add_message(self, message):
        self.__database['count'] += 1
        db_ib = self.__database['count']
        self.__database[db_ib] = message
        Storage.to_db(self.__database)

    def get_db(self):
        return self.__database

    def find_message(self, mes):
        ids = []
        db = self.__database
        for k in db:
            if k == 'count':
                continue
            if mes in db[k]:
                ids.append(k)
        return ids

    @classmethod
    def to_db(cls, database):
        with open('database', 'wb') as f:
            pickle.dump(database, f)

    @classmethod
    def from_db(cls):
        try:
            with open('database', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            database = {'count': 0}
            Storage.to_db(database)
            return database


if __name__ == '__main__':
    storage = Storage()
    print(storage.get_db())
    print(storage.find_message('My First'))
