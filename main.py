from pawpal_system import Owner, Pet, Task, Scheduler

# --- Setup ---
owner = Owner(name="Jordan", available_time=90)

mochi = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
luna = Pet(name="Luna", species="cat", breed="Siamese", age=5)

# --- Add tasks to Mochi ---
mochi.add_task(Task(description="Morning walk", time=30, frequency="daily"))
mochi.add_task(Task(description="Feeding", time=10, frequency="daily"))

# --- Add tasks to Luna ---
luna.add_task(Task(description="Grooming", time=20, frequency="weekly"))

# --- Register pets with owner ---
owner.add_pet(mochi)
owner.add_pet(luna)

# --- Schedule ---
scheduler = Scheduler(owner)
tasks = scheduler.get_tasks()

# --- Print Today's Schedule ---
print("=== Today's Schedule ===")
print(f"Owner: {owner.name} | Available time: {owner.available_time} min\n")

for pet in owner._pets:
    print(f"[ {pet.name} ]")
    for task in pet.get_tasks():
        status = "Done" if task.is_completed else "Pending"
        print(f"  - {task.description} | {task.time} min | {task.frequency} | {status}")
    print()
