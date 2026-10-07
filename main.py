from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Adele")

    buddy = Pet("Buddy", "Dog", 3)
    luna = Pet("Luna", "Cat", 2)

    # Add tasks out of order to test sorting
    buddy.add_task(Task("Walk Buddy", "9:00 AM", "Daily"))
    buddy.add_task(Task("Feed Buddy", "8:00 AM", "Daily"))
    luna.add_task(Task("Give Luna medication", "8:00 AM", "Daily"))

    # Mark Feed Buddy as complete
    completed_task = buddy.tasks[1]
    next_task = completed_task.mark_complete()

    # Add the next recurring task
    if next_task is not None:
        buddy.add_task(next_task)

    owner.add_pet(buddy)
    owner.add_pet(luna)

    scheduler = Scheduler(owner)

    print("PawPal+ Pet Schedule")
    print("--------------------")

    print("\nSorted tasks:")
    for task in scheduler.sort_by_time():
        print(f"{task.time} - {task.description} - Completed: {task.completed}")

    print("\nCompleted tasks:")
    for task in scheduler.filter_tasks(completed=True):
        print(f"{task.time} - {task.description}")

    print("\nBuddy's tasks:")
    for task in scheduler.filter_tasks(pet_name="Buddy"):
        print(f"{task.time} - {task.description}")

    print("\nTask conflicts:")
    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for task1, task2 in conflicts:
            print(
                f"Conflict: {task1.description} and "
                f"{task2.description} are both scheduled at {task1.time}"
            )
    else:
        print("No conflicts detected.")

if __name__ == "__main__":
    main()