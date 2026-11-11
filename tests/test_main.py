from src.main import add_task, list_tasks, mark_done


def test_add_task():
    task_id = add_task("Тестовая задача")
    assert task_id > 0
    assert any(t["title"] == "Тестовая задача" for t in list_tasks())


def test_mark_done():
    task_id = add_task("Выполнить")
    assert mark_done(task_id) is True