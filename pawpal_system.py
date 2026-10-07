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
        """Mark the task as completed."""
        pass


@dataclass
class Pet:
    """Represents a pet and its scheduled tasks."""
    name: str
    species: str
    age: int
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to the pet's task list."""
        pass

    def get_tasks(self):
        """Return the pet's tasks."""
        pass


class Owner:
    """Represents the PawPal+ user."""

    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner's pet list."""
        pass

    def get_all_tasks(self):
        """Return all tasks belonging to the owner's pets."""
        pass


class Scheduler:
    """Organizes and manages tasks for an owner."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self):
        """Retrieve all tasks from the owner's pets."""
        pass

    def sort_by_time(self):
        """Sort tasks by their scheduled time."""
        pass

    def filter_tasks(self):
        """Filter tasks based on selected criteria."""
        pass

    def detect_conflicts(self):
        """Detect tasks scheduled at the same time."""
        pass