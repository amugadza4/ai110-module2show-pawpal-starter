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

## 📸 Demo Walkthrough

The PawPal+ CLI demonstrates the scheduling features through the following steps:

1. Create an owner and add pets to the system.
2. Add pet-care tasks with scheduled times and frequencies.
3. Mark a recurring task as complete, which creates a new incomplete occurrence.
4. View the schedule with tasks sorted by time and filter tasks by pet or completion status.
5. Detect scheduling conflicts when multiple tasks are scheduled at the same time.

**Screenshot or video** *(optional)*: Add a screenshot or link to a demo video here.

