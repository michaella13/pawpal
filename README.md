# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Smarter Scheduling

The `Scheduler` class goes beyond a simple task list to bring structure and awareness to daily pet care planning:

- **Conflict detection** — `find_conflicts()` scans tasks with assigned start times and flags any that overlap on the same day, so you never double-book Mochi's walk and grooming session.
- **Duration-based sorting** — `sort_by_time()` orders tasks from shortest to longest, making it easy to fit quick wins into tight windows first.
- **Frequency filtering** — `filter_by_frequency()` lets you isolate just the daily tasks, weekly tasks, or any other cadence, keeping the schedule view focused.
- **Auto-rescheduling of recurring tasks** — `complete_task()` marks a task done and immediately creates the next occurrence at the right due date (tomorrow for daily, next week for weekly), so recurring care never falls off the radar.

Together these features turn a flat to-do list into a schedule that respects the owner's time, avoids conflicts, and keeps recurring care on track automatically.

## Testing PawPal+

### Run the tests

```bash
python -m pytest
```

### What my tests cover

I wrote six tests that target the most critical behaviors in the scheduling system:

- **Task completion** — I verify that calling `mark_complete()` actually flips the task's status, since the whole rescheduling flow depends on this being reliable.
- **Pet task list** — I confirm that adding a task to a pet is tracked correctly, so I can trust `get_tasks()` throughout the app.
- **Duration sorting** — I check that `sort_by_time()` returns tasks in shortest-to-longest order, which is how I prioritize fitting tasks into tight time windows.
- **Auto-rescheduling** — I test that completing a daily task automatically creates the next occurrence for tomorrow, which is the feature I'm most proud of.
- **Conflict detection** — I verify that two overlapping tasks are correctly flagged, and that back-to-back tasks (no gap, no overlap) are *not* flagged as a false positive.

### Confidence Level

**4 / 5 stars**

I feel solid about the core scheduling logic — every key method has a test, and I covered edge cases like exact boundary timing. What keeps me from 5 stars is that I haven't tested the Streamlit UI layer or written a full end-to-end test that walks through an entire owner-pet-schedule workflow. That's the next thing I'd add.

---

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
