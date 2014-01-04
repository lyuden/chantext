import pickle
from storage_class import Storage, to_db, from_db


#API
storage = Storage()


def get_db():
    return storage.get_db()


def get_message(mes_id):
    return storage.get_message(mes_id)


def find_messages(words):
    return storage.find_messages(words)[2]


def create_message(mes_text):
    storage.add_message(mes_text)
    return True


def update_message(mes_id, mes_text):
    storage.update_message(mes_id, mes_text)
    return True


if __name__ == '__main__':
    print(get_db())
    print(get_message(2))
    print(find_messages(['My', 'Updated', 'Message', 'Second']))
    #create_message('Test Test Test')
    #update_message(4, 'Test2 Test2 Test2')
    print(get_db())
