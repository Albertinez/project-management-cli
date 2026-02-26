from models.task import Task

def test_task_completion():
    task = Task("Implement Feature", "Alex")
    task.complete()
    assert task.status == "Completed"