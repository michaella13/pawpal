from datetime import date
from pawpal_system import Owner, Pet, Task, Scheduler

today = date.today()

# --- Setup ---
owner = Owner(name="Jordan", available_time=120)

mochi = Pet(name="Mochi", species="dog", breed="Shiba Inu", age=3)
luna  = Pet(name="Luna",  species="cat", breed="Siamese",   age=5)

# --- Add tasks OUT OF ORDER (longest first, then short, then medium) ---
mochi.add_task(Task(description="Vet checkup",    time=60, frequency="weekly", start_time=480))   # 8:00 AM
mochi.add_task(Task(description="Morning walk",   time=30, frequency="daily",  start_time=540))   # 9:00 AM
mochi.add_task(Task(description="Feeding",        time=10, frequency="daily",  start_time=555))   # 9:15 AM (overlaps walk)

luna.add_task(Task(description="Grooming",        time=45, frequency="weekly", start_time=660))   # 11:00 AM
luna.add_task(Task(description="Playtime",        time=15, frequency="daily",  start_time=720))   # 12:00 PM
luna.add_task(Task(description="Litter cleaning", time=5,  frequency="daily",  start_time=690))   # 11:30 AM (overlaps grooming)

# --- Register pets with owner ---
owner.add_pet(mochi)
owner.add_pet(luna)

# --- Schedule ---
scheduler = Scheduler(owner)

# --- Print sorted by time ---
print("=== Sorted by Duration (shortest to longest) ===")
for task in scheduler.sort_by_time():
    print(f"  {task.time:>3} min | {task.frequency:<8} | {task.description}")

print()

# --- Print filtered by frequency ---
print("=== Daily Tasks Only ===")
for task in scheduler.filter_by_frequency("daily"):
    status = "Done" if task.is_completed else "Pending"
    print(f"  {task.description} | {task.time} min | {status}")

print()

print("=== Weekly Tasks Only ===")
for task in scheduler.filter_by_frequency("weekly"):
    status = "Done" if task.is_completed else "Pending"
    print(f"  {task.description} | {task.time} min | {status}")

print()

# --- Conflict detection ---
print("=== Conflict Detection ===")
warnings = scheduler.find_conflicts()
if warnings:
    for warning in warnings:
        print(f"  {warning}")
else:
    print("  No conflicts found.")
