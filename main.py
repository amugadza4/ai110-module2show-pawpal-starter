from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Adele")

    buddy = Pet("Buddy", "Dog", 3)
    luna = Pet("Luna", "Cat", 2)

    buddy.add_task(Task("Feed Buddy", "8:00 AM", "Daily"))
    buddy.add_task(Task("Walk Buddy", "9:00 AM", "Daily"))
    luna.add_task(Task("Give Luna medication", "8:00 AM", "Daily"))

    owner.add_pet(buddy)
    owner.add_pet(luna)

    scheduler = Scheduler(owner)

    print("PawPal+ Pet Schedule")
    print("--------------------")

    for task in scheduler.sort_by_time():
        print(f"{task.time} - {task.description} ({task.frequency})")


if __name__ == "__main__":
    main()