from datetime import date, timedelta


class Task:
    def __init__(self, description: str, time: int, frequency: str, due_date: date = None, start_time: int = None):
        self.description = description
        self.time = time                # duration in minutes
        self.frequency = frequency      # e.g. "daily", "weekly"
        self.due_date = due_date or date.today()
        self.start_time = start_time    # minutes from midnight (e.g. 540 = 9:00 AM)
        self.is_completed = False

    def mark_complete(self):
        """Mark this task as completed."""
        self.is_completed = True


class Pet:
    def __init__(self, name: str, species: str, breed: str, age: int, special_needs: list = None):
        """Initialize a Pet with its basic info and an empty task list."""
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.special_needs = special_needs or []
        self._tasks = []

    def add_task(self, task: Task):
        """Add a care task to this pet's task list."""
        self._tasks.append(task)

    def get_tasks(self) -> list:
        """Return all tasks assigned to this pet."""
        return self._tasks


class Owner:
    def __init__(self, name: str, available_time: int):
        """Initialize an Owner with their name and daily available time in minutes."""
        self.name = name
        self.available_time = available_time  # total minutes free per day
        self._pets = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list of pets."""
        self._pets.append(pet)

    def get_all_tasks(self) -> list:
        """Return all tasks across all of this owner's pets."""
        tasks = []
        for pet in self._pets:
            tasks.extend(pet.get_tasks())
        return tasks


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the Scheduler with an owner whose tasks will be managed."""
        self.owner = owner

    def get_tasks(self) -> list:
        """Retrieve all tasks for the owner's pets."""
        pass

    def sort_by_time(self) -> list:
        """Return all tasks sorted by duration (shortest to longest)."""
        tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda task: task.time)

    def filter_by_frequency(self, frequency: str) -> list:
        """Return only tasks matching the given frequency (e.g. 'daily', 'weekly')."""
        tasks = self.owner.get_all_tasks()
        return [task for task in tasks if task.frequency == frequency]

    def find_conflicts(self) -> list:
        """Return warning strings for any tasks that overlap on the same due date.

        Two tasks conflict when both have a start_time set, share the same due_date,
        and their time windows overlap:
            A.start_time < B.start_time + B.time  AND  B.start_time < A.start_time + A.time
        """
        tasks = [t for t in self.owner.get_all_tasks() if t.start_time is not None]
        warnings = []

        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                a, b = tasks[i], tasks[j]
                if a.due_date != b.due_date:
                    continue
                if a.start_time < b.start_time + b.time and b.start_time < a.start_time + a.time:
                    warnings.append(
                        f"Warning: '{a.description}' and '{b.description}' overlap on {a.due_date}"
                    )

        return warnings

    def organize_tasks(self) -> list:
        """Return tasks sorted or grouped for optimal scheduling."""
        pass

    def complete_task(self, task: Task):
        """Mark the given task as complete and schedule the next occurrence for recurring tasks."""
        task.mark_complete()

        if task.frequency == "daily":
            next_due = task.due_date + timedelta(days=1)
        elif task.frequency == "weekly":
            next_due = task.due_date + timedelta(weeks=1)
        else:
            return

        next_task = Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            due_date=next_due
        )
        for pet in self.owner._pets:
            if task in pet.get_tasks():
                pet.add_task(next_task)
                break
