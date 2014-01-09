import pickle


class Storage(object):
    def __init__(self):
        self.__database = from_db()

    def add_message(self, message):
        self.__database['count'] += 1
        db_ib = self.__database['count']
        self.__database[db_ib] = message
        to_db(self.__database)
        return True

    def get_db(self):
        return self.__database

    def get_message(self, mes_id):
        return {"id": mes_id, "message": self.__database[mes_id]}

    def find_message(self, mes):
        ids = []
        db = self.__database
        for k in db:
            if k == 'count':
                continue
            if mes in db[k]:
                ids.append(k)
        return ids

    def find_messages(self, words):
        temp_dict = {}
        for world in words:
            temp_dict[world] = self.find_message(world)
        id_dict = {}
        for world, list_id in temp_dict.items():
            for mes_id in list_id:
                if mes_id not in id_dict:
                    id_dict[mes_id] = 1
                    continue
                id_dict[mes_id] += 1
        sorted_list_id = sorted(id_dict.items(), key=lambda x: x[1])
        sorted_list_id = [i[0] for i in sorted_list_id][::-1]
        return temp_dict, id_dict, sorted_list_id

    def update_message(self, mes_id, mes_text):
        database = self.get_db()
        database[mes_id] = mes_text
        self.__database = database
        to_db(database)
        return True

    def get_messages_list(self, limit=50):
        temp = self.get_db()
        temp.pop('count')
        temp = list(temp.items())[0:limit]
        return [{'id': mes[0], 'message': mes[1]} for mes in temp]


def to_db(database):
    with open('database', 'wb') as f:
        pickle.dump(database, f)
        return True


def from_db():
    try:
        with open('database', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        database = {'count': 0}
        to_db(database)
        return database
