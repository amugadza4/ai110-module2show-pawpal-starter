# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

* Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
* Consider constraints (time available, priority, owner preferences)
* Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

* Let a user enter basic owner + pet info
* Let a user add/edit tasks (duration + priority at minimum)
* Generate a daily schedule/plan based on constraints and priorities
* Display the plan clearly (and ideally explain the reasoning)
* Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

The current CLI displays the pet schedule and sorts tasks by their scheduled time.

Run the CLI with:

```bash
python3 main.py
```

Example output:

```text
PawPal+ Pet Schedule
--------------------
8:00 AM - Feed Buddy (Daily)
8:00 AM - Give Luna medication (Daily)
9:00 AM - Walk Buddy (Daily)
```

## 🧪 Testing PawPal+

Run the full test suite with:

```bash
python3 -m pytest
```

The test suite verifies:

* Tasks can be marked as complete.
* Tasks can be added to a pet.
* Tasks are sorted by scheduled time.
* Completing a Daily task creates a new incomplete recurring task.
* Scheduling conflicts are detected when tasks have the same time.

Sample test output:

```text
=============== test session starts ================
platform darwin -- Python 3.12.1, pytest-9.1.1, pluggy-1.6.0
collected 5 items

tests/test_pawpal_system.py .....            [100%]

================ 5 passed in 0.01s =================
```

**Confidence Level:** ⭐⭐⭐⭐⭐

The test suite covers the core functionality of the PawPal+ system, including task management, sorting, recurring tasks, and conflict detection. The five passing tests give me confidence that the main scheduling functionality is working as expected.

## 📐 Smarter Scheduling

| Feature           | Method(s)                      | Notes                                                                   |
| ----------------- | ------------------------------ | ----------------------------------------------------------------------- |
| Task sorting      | `Scheduler.sort_by_time()`     | Sorts tasks by their scheduled time.                                    |
| Filtering         | `Scheduler.filter_tasks()`     | Filters tasks by pet name or completion status.                         |
| Conflict handling | `Scheduler.detect_conflicts()` | Identifies tasks scheduled at the same time.                            |
| Recurring tasks   | `Task.mark_complete()`         | Creates a new task for Daily and Weekly recurring tasks when completed. |

## ✨ Features

PawPal+ includes the following scheduling features:

- **Pet Management** — Add pets and store basic pet information.
- **Task Management** — Add pet-care tasks with a scheduled time and frequency.
- **Sorting by Time** — Tasks are automatically sorted by their scheduled time.
- **Task Filtering** — View tasks by pet or completion status.
- **Recurring Tasks** — Completing a Daily or Weekly task creates a new incomplete recurring task.
- **Conflict Detection** — The scheduler identifies tasks that are scheduled for the same time.
- **Streamlit UI** — Users can add pets, create tasks, view their schedule, and receive conflict warnings through the web interface.

## 📸 Demo Walkthrough

The PawPal+ Streamlit interface allows a pet owner to manage their pets and organize their care schedule.

### 1. Add a Pet

The user enters a pet's name and selects its species. After selecting **Add Pet**, the pet is added to the owner's PawPal+ profile.

### 2. Add a Task

After adding a pet, the user can select the pet and create a task. Each task includes:

- Task description
- Scheduled time
- Frequency

For example, a user could add **Feed Buddy** at **8:00 AM** with a Daily frequency.

### 3. View the Sorted Schedule

PawPal+ uses the `Scheduler.sort_by_time()` method to organize tasks by their scheduled time. The Streamlit interface displays the sorted tasks in a table so the owner can easily see what needs to be completed.

### 4. Identify Schedule Conflicts

PawPal+ uses `Scheduler.detect_conflicts()` to identify tasks scheduled at the same time.

When a conflict is found, the UI displays a warning explaining which tasks overlap. This helps the pet owner recognize scheduling issues before following the daily plan.

### 5. View Completed Tasks

The UI uses `Scheduler.filter_tasks(completed=True)` to display tasks that have already been completed.

### 6. Example CLI Output

The same scheduling logic can also be demonstrated through the command-line interface by running:

```bash
python3 main.py

PawPal+ Pet Schedule
--------------------

Sorted tasks:
8:00 AM - Feed Buddy - Completed: True
8:00 AM - Feed Buddy - Completed: False
8:00 AM - Give Luna medication - Completed: False
9:00 AM - Walk Buddy - Completed: False

Completed tasks:
8:00 AM - Feed Buddy

Buddy's tasks:
9:00 AM - Walk Buddy
8:00 AM - Feed Buddy
8:00 AM - Feed Buddy

Task conflicts:
Conflict: Feed Buddy and Feed Buddy are both scheduled at 8:00 AM
Conflict: Feed Buddy and Give Luna medication are both scheduled at 8:00 AM
Conflict: Feed Buddy and Give Luna medication are both scheduled at 8:00 AM