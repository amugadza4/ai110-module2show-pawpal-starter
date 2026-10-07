from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """Represents a single pet care task."""
    description: str
    time: str
    frequency: str
    completed: bool = False

    def mark_complete(self):
        """Mark the task as completed and create the next recurring occurrence."""
        self.completed = True

        if self.frequency == "Daily":
            return Task(
                self.description,
                self.time,
                self.frequency
            )

        if self.frequency == "Weekly":
            return Task(
                self.description,
                self.time,
                self.frequency
            )

        return None


@dataclass
class Pet:
    """Represents a pet and its scheduled tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return the pet's tasks."""
        return self.tasks


class Owner:
    """Represents the PawPal+ user."""

    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks belonging to the owner's pets."""
        return [task for pet in self.pets for task in pet.get_tasks()]


class Scheduler:
    """Organizes and manages tasks for an owner."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self):
        """Retrieve all tasks from the owner's pets."""
        return self.owner.get_all_tasks()

    def sort_by_time(self):
        """Sort tasks by their scheduled time."""
        return sorted(self.get_all_tasks(), key=lambda task: task.time)

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        tasks = self.get_all_tasks()

        if pet_name is not None:
            filtered_tasks = []

            for pet in self.owner.pets:
                if pet.name == pet_name:
                    filtered_tasks.extend(pet.get_tasks())

            tasks = filtered_tasks

        if completed is not None:
            tasks = [task for task in tasks if task.completed == completed]

        return tasks

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        tasks = self.get_all_tasks()
        conflicts = []

        for i, task in enumerate(tasks):
            for other_task in tasks[i + 1:]:
                if task.time == other_task.time:
                    conflicts.append((task, other_task))

        return conflicts