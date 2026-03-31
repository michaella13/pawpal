import streamlit as st
from pawpal_system import Task, Pet, Owner, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Add a Pet")

owner_name = st.text_input("Owner name", value="Jordan")
available_time = st.number_input("Owner's available time (minutes/day)", min_value=1, max_value=1440, value=120)
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
breed = st.text_input("Breed", value="Mixed")
age = st.number_input("Age (years)", min_value=0, max_value=30, value=3)

if "pet" not in st.session_state:
    st.session_state.pet = None

if st.button("Save Pet"):
    st.session_state.pet = Pet(name=pet_name, species=species, breed=breed, age=int(age))
    st.success(f"Pet '{pet_name}' saved.")

st.markdown("### Schedule a Task")
st.caption("Tasks are added to the saved pet above.")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task description", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    frequency = st.selectbox("Frequency", ["daily", "weekly", "as-needed"])

if st.button("Add task"):
    if st.session_state.pet is None:
        st.warning("Save a pet first before adding tasks.")
    else:
        task = Task(description=task_title, time=int(duration), frequency=frequency)
        st.session_state.pet.add_task(task)
        st.success(f"Task '{task_title}' added to {st.session_state.pet.name}.")

if st.session_state.pet and st.session_state.pet.get_tasks():
    st.write(f"Current tasks for {st.session_state.pet.name}:")
    st.table([
        {"description": t.description, "duration_minutes": t.time, "frequency": t.frequency, "completed": t.is_completed}
        for t in st.session_state.pet.get_tasks()
    ])
elif st.session_state.pet:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    if st.session_state.pet is None or not st.session_state.pet.get_tasks():
        st.warning("Save a pet and add at least one task before generating a schedule.")
    else:
        owner = Owner(name=owner_name, available_time=int(available_time))
        owner.add_pet(st.session_state.pet)
        scheduler = Scheduler(owner)
        scheduled = scheduler.organize_tasks()
        if scheduled:
            st.success("Schedule generated!")
            st.table([
                {"description": t.description, "duration_minutes": t.time, "frequency": t.frequency}
                for t in scheduled
            ])
        else:
            st.info("Scheduler returned no results. Implement organize_tasks() in pawpal_system.py to see the schedule.")
