from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_complete():
    task = Task("Feed Buddy", "8:00 AM", "Daily")

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    pet = Pet("Buddy", "Dog", 3)
    task = Task("Walk Buddy", "9:00 AM", "Daily")

    pet.add_task(task)

    assert task in pet.get_tasks()

def test_sort_by_time():
    owner = Owner("Adele")
    pet = Pet("Buddy", "Dog", 3)

    pet.add_task(Task("Walk Buddy", "9:00 AM", "Daily"))
    pet.add_task(Task("Feed Buddy", "8:00 AM", "Daily"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    assert sorted_tasks[0].description == "Feed Buddy"
    assert sorted_tasks[1].description == "Walk Buddy"
def test_recurring_task():
    task = Task("Feed Buddy", "8:00 AM", "Daily")

    next_task = task.mark_complete()

    assert task.completed is True
    assert next_task is not None
    assert next_task.description == "Feed Buddy"
    assert next_task.frequency == "Daily"
    assert next_task.completed is False
def test_detect_conflicts():
    owner = Owner("Adele")
    pet = Pet("Buddy", "Dog", 3)

    pet.add_task(Task("Feed Buddy", "8:00 AM", "Daily"))
    pet.add_task(Task("Give Buddy medication", "8:00 AM", "Daily"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()

    assert len(conflicts) == 1
    assert conflicts[0][0].description == "Feed Buddy"
    assert conflicts[0][1].description == "Give Buddy medication"