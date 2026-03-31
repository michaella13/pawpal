from datetime import date


class Owner:
    def __init__(self, name: str, available_time: int, preferences: list = None):
        self.name = name
        self.available_time = available_time  # total minutes free per day
        self.preferences = preferences or []
        self.pet = None

    def set_availability(self, minutes: int):
        pass


class Pet:
    def __init__(self, name: str, species: str, breed: str, age: int, special_needs: list = None):
        self.name = name
        self.species = species
        self.breed = breed
        self.age = age
        self.special_needs = special_needs or []
        self._tasks = []

    def add_task(self, task):
        pass

    def get_tasks(self) -> list:
        pass


class CareTask:
    def __init__(self, name: str, duration: int, priority: str, category: str):
        self.name = name
        self.duration = duration        # minutes
        self.priority = priority        # "low", "medium", or "high"
        self.category = category        # "walk", "feeding", "meds", "grooming", "enrichment"
        self.is_completed = False

    def mark_complete(self):
        pass


class DailySchedule:
    def __init__(self, schedule_date: date = None):
        self.date = schedule_date or date.today()
        self.tasks = []
        self.total_time_used = 0
        self.reasoning = ""

    def display(self):
        pass

    def get_summary(self) -> dict:
        pass


class Scheduler:
    def __init__(self, owner: Owner, pet: Pet):
        self.owner = owner
        self.pet = pet

    def generate_plan(self) -> DailySchedule:
        pass

    def apply_constraints(self, tasks: list) -> list:
        pass

    def prioritize_tasks(self) -> list:
        pass

    def explain_reasoning(self, tasks: list) -> str:
        pass
