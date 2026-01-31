class Task:
    def __init__(self,title,description,deadlain):
        self.title = title
        self.description = description
        self.deadlain = deadlain
        self.completed = False

    def mark_completed(self):
        self.completed = True

class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
      
    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Завдання видалено")
                return
        print("Завдання не знайдено")

    def mark_task_completed(self, title):
            for task in self.tasks:
                if task.title == title:
                    task.mark_completed()
                print("Завдання виконано")
                return
            print("Завдання не знайдено")

    def display_tasks(self):
        if not self.tasks:
            print("Список завдань порожній")
            return

        for task in self.tasks:
            status = "Виконано" if task.completed else "Не виконано"
            print(f"Назва: {task.title}")
            print(f"Опис: {task.description}")
            print(f"Дедлайн: {task.deadline}")
            print(f"Стан: {status}")
            print("-" * 20)

Human = TaskManager()

task1 = Task("Математика", "Зробити домашнє завдання", "12.12.2030")
task2 = Task("Python", "Вивчити класи", "11.12.2031")

Human.add_task(task1)
Human.add_task(task2)

Human.display_tasks()

Human.mark_task_completed("Математика")

Human.display_tasks()