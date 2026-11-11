tasks = []
next_id = 1


def add_task(title: str) -> int:
    global next_id
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    next_id += 1
    return task["id"]


def list_tasks() -> list:
    return tasks


def mark_done(task_id: int) -> bool:
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return True
    return False


def delete_task(task_id: int) -> bool:
    global tasks
    before = len(tasks)
    tasks = [task for task in tasks if task["id"] != task_id]
    return len(tasks) < before


def print_menu() -> None:
    print("\n1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу")
    print("0. Выход")


def main() -> None:
    while True:
        print_menu()
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            title = input("Название задачи: ").strip()
            task_id = add_task(title)
            print(f"Добавлена задача #{task_id}")
        elif choice == "2":
            for task in list_tasks():
                status = "✓" if task["done"] else "✗"
                print(f"[{status}] #{task['id']} {task['title']}")
        elif choice == "3":
            try:
                task_id = int(input("ID задачи: "))
                if mark_done(task_id):
                    print("Задача выполнена")
                else:
                    print("Задача не найдена")
            except ValueError:
                print("Нужно ввести число")
        elif choice == "4":
            try:
                task_id = int(input("ID задачи для удаления: "))
                if delete_task(task_id):
                    print("Задача удалена")
                else:
                    print("Задача не найдена")
            except ValueError:
                print("Нужно ввести число")
        elif choice == "0":
            break
        else:
            print("Неверный пункт меню")


if __name__ == "__main__":
    main()