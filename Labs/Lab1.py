documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def doc_owner(number):
    for doc in documents:
        if doc['number'] == number:
            return f"Владелец документа: {doc['name']}"
        return "Владелец документа не найден в базе"


def doc_direct(number):
    for directory in directories:
        if number in directories[directory]:
            return directory
    return None


def docs_info():
    for doc in documents:
        print(
            f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {doc_direct(doc['number'])}")
    return


def add_direct(number):
    if number in directories.keys:
        return f"Такая полка уже существует. Текущий перечень полок: {list(directories.keys())}"
    else:
        directories[number] = []
        return f"Полка добавлена. Текущий перечень полок: {list(directories.keys())}"


def del_direct(number):
    if number not in directories.keys:
        return f"Такой полки не существует. Текущий перечень полок:{list(directories.keys())}"
    elif directories[number].len > 0:
        return f"На полке есть документы, удалите их перед удалением полки. Текущий перечень полок:{list(directories.keys())}"
    else:
        del directories[number]
        return f"Полка удалена. Текущий перечень полок:{list(directories.keys())}"


def add_doc(type_, number, name, direct):
    if direct not in directories.keys():
        return f"Такой полки не существует. Добавьте полку командой as."
    else:
        doc = {'type': type_, 'number': number, 'name': name}
        documents.append(doc)
        directories[direct].append(doc['number'])
        return f"Документ добавлен. Текущий список документов: {docs_info()}"


def del_doc(number):
    for doc in documents:
        if doc['number'] == number:
            documents.remove(doc)
            return f'Документ удален. Текущий список документов: {docs_info()}'
    return f'Документ не найден в базе. Текущий список документов: {docs_info()}'


def move_doc(number, new_dir):
    if new_dir not in directories.keys:
        return f"Такой полки не существует. Текущий перечень полок: {list(directories.keys())}"
    for doc in documents:
        if doc['number'] == number:
            directories[new_dir].append(doc['number'])
            directories[doc_direct(number)].remove(number)
            return f"Документ перемещен. Текущий список документов: {docs_info()}"
    return f"Документ не найден в базе. Текущий список документов: {docs_info()}"


while True:
    command = input("Введите команду: ")
    if command == "q":
        break

    elif command == "l":
        docs_info()

    elif command == "p":
        p_number = input("Введите номер документа ")
        doc_owner(p_number)

    elif command == "ad":
        ad_type = input("Введите тип документа ")
        ad_number = input("Введите номер документа ")
        ad_name = input("Введите владельца документа ")
        ad_direct = input("Введите номер полки ")
        add_doc(ad_type, ad_number, ad_name, ad_direct)

    elif command == "d":
        d_number = input("Введите номер документа ")
        del_doc(d_number)

    elif command == "s":
        s_number = input("Введите номер документа ")
        if doc_direct(s_number) is None:
            print("Документ не найден в базе")
        else:
            print(f"Документ хранится на полке {doc_direct(s_number)}")

    elif command == "m":
        m_number = input("Введите номер документа ")
        m_new_dir = input("Введите номер полки ")
        move_doc(m_number, m_new_dir)

    elif command == "ads":
        ads_number = input("Введите номер полки ")
        add_direct(ads_number)

    elif command == "ds":
        ds_number = input("Введите номер полки ")
        del_direct(ds_number)
