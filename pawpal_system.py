class Task:
    def __init__(self, description: str, time: int, frequency: str):
        self.description = description
        self.time = time                # duration in minutes
        self.frequency = frequency      # e.g. "daily", "weekly"
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
        pass

    def get_all_tasks(self) -> list:
        """Return all tasks across all of this owner's pets."""
        pass


class Scheduler:
    def __init__(self, owner: Owner):
        """Initialize the Scheduler with an owner whose tasks will be managed."""
        self.owner = owner

    def get_tasks(self) -> list:
        """Retrieve all tasks for the owner's pets."""
        pass

    def organize_tasks(self) -> list:
        """Return tasks sorted or grouped for optimal scheduling."""
        pass

    def complete_task(self, task: Task):
        """Mark the given task as complete."""
        pass
