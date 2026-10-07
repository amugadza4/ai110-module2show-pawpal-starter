from pawpal_system import Pet, Task


def test_mark_complete():
    task = Task("Feed Buddy", "8:00 AM", "Daily")

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Walk Buddy", "9:00 AM", "Daily")

    pet.add_task(task)

    assert task in pet.get_tasks()