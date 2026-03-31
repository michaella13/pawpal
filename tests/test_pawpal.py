import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from datetime import date, timedelta
from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete_changes_status():
    task = Task("Feed the cat", 5, "daily")
    assert task.is_completed is False
    task.mark_complete()
    assert task.is_completed is True


def test_add_task_increases_pet_task_count():
    pet = Pet("Whiskers", "cat", "Siamese", 3)
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task("Feed the cat", 5, "daily"))
    assert len(pet.get_tasks()) == 1


def test_sort_by_time_returns_chronological_order():
    owner = Owner("Alice", 120)
    pet = Pet("Buddy", "dog", "Labrador", 2)
    owner.add_pet(pet)

    pet.add_task(Task("Evening walk", 60, "daily"))
    pet.add_task(Task("Quick potty break", 10, "daily"))
    pet.add_task(Task("Grooming session", 30, "daily"))

    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()

    durations = [t.time for t in sorted_tasks]
    assert durations == sorted(durations), "Tasks should be sorted shortest to longest"


def test_complete_daily_task_creates_next_day_task():
    today = date.today()
    owner = Owner("Alice", 120)
    pet = Pet("Buddy", "dog", "Labrador", 2)
    owner.add_pet(pet)

    task = Task("Morning walk", 30, "daily", due_date=today)
    pet.add_task(task)

    scheduler = Scheduler(owner)
    scheduler.complete_task(task)

    tasks = pet.get_tasks()
    assert task.is_completed is True
    assert len(tasks) == 2, "A follow-up task should have been added"

    next_task = tasks[1]
    assert next_task.due_date == today + timedelta(days=1)
    assert next_task.description == task.description
    assert next_task.is_completed is False


def test_find_conflicts_flags_overlapping_tasks():
    today = date.today()
    owner = Owner("Alice", 120)
    pet = Pet("Buddy", "dog", "Labrador", 2)
    owner.add_pet(pet)

    # Task A: 9:00 AM (540 min) for 30 min → ends 9:30 AM
    pet.add_task(Task("Morning walk", 30, "daily", due_date=today, start_time=540))
    # Task B: 9:15 AM (555 min) for 20 min → overlaps with Task A
    pet.add_task(Task("Feeding", 20, "daily", due_date=today, start_time=555))

    scheduler = Scheduler(owner)
    conflicts = scheduler.find_conflicts()

    assert len(conflicts) == 1
    assert "Morning walk" in conflicts[0]
    assert "Feeding" in conflicts[0]


def test_find_conflicts_no_false_positives():
    today = date.today()
    owner = Owner("Alice", 120)
    pet = Pet("Buddy", "dog", "Labrador", 2)
    owner.add_pet(pet)

    # Task A: 9:00 AM for 30 min → ends 9:30 AM
    pet.add_task(Task("Morning walk", 30, "daily", due_date=today, start_time=540))
    # Task B: 9:30 AM — starts exactly when A ends, no overlap
    pet.add_task(Task("Feeding", 20, "daily", due_date=today, start_time=570))

    scheduler = Scheduler(owner)
    conflicts = scheduler.find_conflicts()

    assert len(conflicts) == 0, "Back-to-back tasks should not be flagged as conflicts"
