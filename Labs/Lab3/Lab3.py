import json

filename = 'tasks.json'

tasks_list = []


def task_reader():
    try:
        with open(filename) as f:
            tasks = json.load(f)
        return tasks
    except Exception as e:
        return e


if __name__ == "__main__":
    tasks_list = task_reader()
    print("текущие задачи из файла: ", tasks_list)


def task_writer(tasks_list):
    try:
        with open(filename, 'w') as f:
            json.dumps(tasks_list, f)
    except Exception as e:
        print(e)


def task_append(tasks_list):
    task = input("Сформулируйте задачу: ")
    category = input("Добавьте категорию к задаче: ")
    time = input("Добавьте время к задаче: ")
    tasks_list.append({'Задача': task, 'Категория': category, 'Время': time})


while True:
    com = int(input('''Простой todo:
        1. Добавить задачу.
        2. Вывести список задач.
        3. Выход.
        Укажите число: '''))
    if com == 1:
        task_append(tasks_list)
    elif com == 2:
        for task in tasks_list:
            print(f'Задача: {task["Задача"]} Категория: {task["Категория"]} Время на выполнение: {task["Время"]}')
    elif com == 3:
        task_writer(tasks_list)
        print('задачи сохранены в файл!')
        break
