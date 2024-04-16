# Менеджер задач
#
# Задача: Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и статус
# (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки
# выполненных задач и вывода списка текущих (не выполненных) задач.

task_list = []


class Task ():

    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def change_status(self):
        if not self.status:
            self.status = True
            print('Задача отмечена выполненной.')
            print()
            task_list.remove(self)
        else:
            self.status = False
            print('Задача отмечена не выполненной.')
            print()
            task_list.append(self)

    def info(self):
        print(f'Задача: {self.description}.')
        print(f'Срок выполнения: {self.deadline}.')
        if not self.status:
            print('Задача не выполнена.')
        else:
            print('Задача выполнена.')
        print()


def add_task(description, deadline, status):
    new_task = Task(description, deadline, status)
    task_list.append(new_task)
    print(f'Вы добавили новую задачу: {description}.')
    print(f'Срок выполнения: {deadline}.')
    print('Задача не выполнена.')
    print()
    return new_task


def make_list():
    for i, task in enumerate(task_list):
        print(i + 1, task.description)
    print()


task1 = add_task('разработать эскиз фасада', 'до пятницы', False)
task2 = add_task('поправить планировку', 'до вечера', False)
task3 = add_task('съездить на встречу', 'в среду в 13:00', False)
task4 = add_task('убраться в квартире', 'в субботу', False)
task5 = add_task('нагнать учебу', 'до конца каникул', False)

make_list()

task2.info()

task2.change_status()

task2.info()

make_list()
