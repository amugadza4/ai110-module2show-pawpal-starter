# PawPal+ Project Reflection

## 1. System Design
Three Core Actions

The three core actions a user should be able to perform are:

Add a pet: The user should be able to add a pet and enter the pet's information.
Schedule a task: The user should be able to create tasks for their pets, such as feedings, walks, medications, or appointments.
View the pet schedule: The user should be able to view the tasks scheduled for their pets and see what needs to be completed.

The Four Main Building Blocks
Owner: The person using PawPal+.
Attributes: Name,pets 
Methods: add a pet, get all pets, get all tasks
Pet: The owner's dog, cat, or other pet.
Attributes: name,species,age,tasks
Methods: add a task, get tasks
Task: Something that needs to be completed for a pet.
Attributes: description, time, frequency, completion status
Mehods: mark complete
Scheduler: The system that organizes the tasks.
Attributes: owner
Methods: get all tasks,sort tasks, filter tasks,detect conflicts
**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design was based on four main classes: Owner, Pet, Task, and Scheduler. The design shows how the owner manages their pets, each pet has tasks, and the scheduler manages the tasks for the owner.

- What classes did you include, and what responsibilities did you assign to each?
I included four classes: Owner, Pet, Task, and Scheduler. The Owner class represents the person using PawPal+ and manages their pets. The Pet class stores information about each pet and their assigned tasks. The Task class represents individual pet-care activities and stores information such as the description, time, frequency, and completion status. The Scheduler class organizes the owner's tasks and handles functions such as sorting tasks, filtering tasks, and detecting scheduling conflicts.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
No, my design did not change during the initial implementation. I kept the four classes and their original responsibilities from my UML design while creating the class skeletons. I may make changes later as I add more functionality and identify areas that could be improved.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
The scheduler currently considers the scheduled time, pet name, completion status, and task frequency. The most important constraint was time because the main purpose of PawPal+ is to organize pet-care tasks into a clear schedule. I also considered completion status and pet name because they make it easier for the owner to filter and manage tasks.

- How did you decide which constraints mattered most?
I prioritized keeping the scheduling logic simple and focused on the features I had already designed in my UML diagram. Although the original project scenario mentioned priorities and other constraints, I did not add them because they were not part of my final class structure. Instead, I focused on sorting tasks by time, filtering tasks, detecting conflicts, and handling recurring tasks.
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is using exact time matches to detect conflicts. This means that two tasks are only considered a conflict if they are scheduled at the same time.
- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable because PawPal+ currently focuses on scheduling tasks by their scheduled time and does not include task durations. Using exact time matches keeps the conflict detection simple while still identifying tasks that are scheduled at the same time.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI throughout the project for design brainstorming, writing and improving Python code, debugging errors, creating automated tests, and connecting my backend logic to the Streamlit interface. I also used AI to help review my UML diagram and make sure it matched the classes and methods in my final implementation.
- What kinds of prompts or questions were most helpful?
The most helpful prompts were specific questions about the code I was currently working on. For example, asking how to implement sorting, filtering, recurring tasks, and conflict detection helped me understand how each feature could fit into my existing classes. Asking AI to explain errors and provide full replacement code was also helpful when I needed to make changes without accidentally leaving parts of the old code behind.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One example where I did not accept an AI suggestion as-is was the recurring-task logic. One approach suggested adding more date-based functionality so that a recurring task could specifically create an occurrence for the following day. I decided not to expand the system that way because my `Task` class did not have a date attribute and adding one would have changed the design I had already created.

Instead, I kept the implementation focused on creating a new incomplete task for Daily and Weekly tasks when the current task is completed. I verified the decision by running my automated tests and checking that the new recurring task had the correct description and frequency and was marked as incomplete.
- How did you evaluate or verify what the AI suggested?
I learned that I should not automatically accept AI-generated code just because it works. I need to make sure the suggestion fits the architecture and requirements of my project.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I created five automated tests for the main behaviors of the PawPal+ scheduler:

- Marking a task as complete.
- Adding a task to a pet.
- Sorting tasks by scheduled time.
- Creating a new incomplete task for a Daily recurring task.
- Detecting conflicts when two tasks have the same scheduled time.

- Why were these tests important?
These tests were important because they verified the core functionality of the system instead of only checking whether the application could run. In particular, the sorting, recurring-task, and conflict-detection tests helped verify the main scheduling behaviors I implemented.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am very confident that the current scheduler works correctly for the behaviors I implemented. All five automated tests passed, and I also tested the Streamlit interface by adding a pet and creating tasks.

- What edge cases would you test next if you had more time?
If I had more time, I would test additional edge cases such as multiple pets with overlapping tasks, multiple tasks at the same time, filtering when no tasks match, empty task lists, and different recurring-task frequencies. I would also test more complex time formats and eventually add date-based scheduling.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
The part of the project I am most satisfied with is how the system developed from a basic class design into a working scheduler with a Streamlit interface. I was able to connect the `Owner`, `Pet`, `Task`, and `Scheduler` classes and then use the scheduler's methods in the UI. I am also satisfied that I created automated tests and used them to verify that the core scheduling behaviors were working.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduling system by adding dates, task duration, and priority. This would allow PawPal+ to create more realistic daily schedules instead of primarily organizing tasks by their scheduled time. I would also improve the conflict detection so that it could consider task duration instead of only identifying tasks with the exact same time.

I would also improve the Streamlit interface by allowing users to edit and delete tasks and by giving users more control over their scheduling preferences.
**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned is that designing a system is more than just getting the code to work. I needed to think about how the classes, methods, tests, and user interface all connected to each other. Working with AI also taught me that I should treat AI as a development tool rather than letting it make every design decision for me. I need to understand the suggestions, test them, and decide whether they actually fit the system I am building.