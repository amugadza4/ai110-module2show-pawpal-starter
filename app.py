import streamlit as st

from pawpal_system import Owner, Pet, Task, Scheduler


st.title("🐾 PawPal+")

st.write("A simple pet care scheduling assistant.")


# Create owner
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")


owner = st.session_state.owner
scheduler = Scheduler(owner)


# -----------------------------
# Add a Pet
# -----------------------------
st.header("Add a Pet")

pet_name = st.text_input("Pet Name")
species = st.selectbox("Species", ["Dog", "Cat", "Other"])

if st.button("Add Pet"):
    if pet_name:
        new_pet = Pet(pet_name, species, 0)
        owner.add_pet(new_pet)
        st.success(f"{pet_name} was added!")
    else:
        st.warning("Please enter a pet name.")


# -----------------------------
# Add a Task
# -----------------------------
st.header("Add a Task")

if owner.pets:
    selected_pet = st.selectbox(
        "Select Pet",
        owner.pets,
        format_func=lambda pet: pet.name
    )

    task_title = st.text_input("Task")

    task_time = st.text_input(
        "Time",
        placeholder="Example: 8:00 AM"
    )

    frequency = st.selectbox(
        "Frequency",
        ["Daily", "Weekly", "One-time"]
    )

    if st.button("Add Task"):
        if task_title and task_time:
            new_task = Task(
                task_title,
                task_time,
                frequency
            )

            selected_pet.add_task(new_task)

            st.success(
                f"{task_title} was added to {selected_pet.name}'s schedule!"
            )
        else:
            st.warning("Please enter both a task and a time.")

else:
    st.info("Add a pet before creating a task.")


# -----------------------------
# Schedule
# -----------------------------
st.header("📅 Pet Schedule")

all_tasks = scheduler.get_all_tasks()

if all_tasks:

    st.subheader("Sorted Schedule")

    sorted_tasks = scheduler.sort_by_time()

    schedule_data = []

    for task in sorted_tasks:
        schedule_data.append(
            {
                "Time": task.time,
                "Task": task.description,
                "Frequency": task.frequency,
                "Completed": task.completed
            }
        )

    st.table(schedule_data)


    # -----------------------------
    # Conflict Warnings
    # -----------------------------
    st.subheader("⚠️ Schedule Conflicts")

    conflicts = scheduler.detect_conflicts()

    if conflicts:
        for task1, task2 in conflicts:
            st.warning(
                f"Schedule conflict: **{task1.description}** and "
                f"**{task2.description}** are both scheduled for "
                f"**{task1.time}**."
            )
    else:
        st.success("No scheduling conflicts detected!")


    # -----------------------------
    # Completed Tasks
    # -----------------------------
    st.subheader("✅ Completed Tasks")

    completed_tasks = scheduler.filter_tasks(completed=True)

    if completed_tasks:
        for task in completed_tasks:
            st.success(
                f"{task.time} - {task.description}"
            )
    else:
        st.info("No completed tasks yet.")


else:
    st.info("No tasks have been scheduled yet.")
