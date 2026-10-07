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
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is using exact time matches to detect conflicts. This means that two tasks are only considered a conflict if they are scheduled at the same time.
- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable because PawPal+ currently focuses on scheduling tasks by their scheduled time and does not include task durations. Using exact time matches keeps the conflict detection simple while still identifying tasks that are scheduled at the same time.
---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
