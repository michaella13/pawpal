import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from pawpal_system import Task, Pet


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
